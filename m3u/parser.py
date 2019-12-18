class Parser:
    # extended m3u file directives
    FILE_HEADER = "EXTM3U"
    TRACK_INFO="EXTINF"
    ALBUM_INFORMATION = "EXTALB"
    ALBUM_ARTIST = "EXTART"
    ALBUM_GENRE = "EXTGENRE"
    ALBUM_GROUP = "EXTGRP"
    PLAYLIST_DISPLAY_TITLE = "PLAYLIST"
    PLAYLIST_TRACKS = "EXTM3A"
    FILE_SIZE = "EXTBYT"
    BIN_DATA_FOLLOWS="EXTBIN"
    TEXT_ENCODING="EXTENC"
    COVER_IMAGE="EXTIMG"

    # HLS M3U Extensions file directives
    START="EXT-X-START"
    INDEP_SEG="EXT-X-INDEPENDENT-SEGMENTS"
    PLAYLIST_TYPE="EXT-X-PLAYLIST-TYPE"
    TARGET_DURATION="EXT-X-TARGETDURATION"
    VERSION = "EXT-X-VERSION"
    MEDIA_SEQ="EXT-X-MEDIA-SEQUENCE"
    MEDIA="EXT-X-MEDIA"
    STREAM_INF="EXT-X-STREAM-INF"
    BYTE_RANGE="EXT-X-BYTERANGE"
    DISCONTINUITY="EXT-X-DISONTINUITY"
    DISCONTINUITY_SEQ="EXT-X-DISCONTINUITY-SEQUENCE"
    KEY="EXT-X-KEY"
    MAP="EXT-X-MAP"
    PROG_DATE_TIME="EXT-X-PROGRAM-DATE-TIME"
    DATERANGE="EXT-X-DATERANGE"
    I_FRAMES_ONLY="EXT-X-I-FRAMES-ONLY"
    SESSION_DATA="EXT-X-SESSION-DATA"
    SESSION_KEY="EXT-X-SESSION-KEY"
    ENDLIST="EXT-X-ENDLIST"

    def __init__(self, filepath):
        self.file = open(filepath, "r")
        self.contents = self.file.read().split("#")
    
    def header(self)->bool:
        return self.contents[1].strip("\n") == Parser.FILE_HEADER

    def version(self) -> str:
        for x in self.contents:
            if Parser.VERSION in x:
                x = x.strip(Parser.VERSION+":")
                return x.strip("\n")
        return "Version could not be found."
    
    def targe_duration(self) -> str:
        for x in self.contents:
            if Parser.TARGET_DURATION in x:
                x=x.strip(Parser.TARGET_DURATION+":")
                return x.strip("\n")
        return "Target Duration is not mentioned in the file."
    
    def playlist_type(self) -> str:
        for x in self.contents:
            if Parser.PLAYLIST_TYPE in x:
                x=x.strip(Parser.PLAYLIST_TYPE+":")
                return x.strip("\n")
        return "Playlist type is not mention in the file."
    
    def track_Information(self) -> {}:
        d={}
        for x in self.contents:
            if Parser.TRACK_INFO in x:
                (runtime, track_info) = x.split(",")
                info=track_info.split("\n")
                d[runtime.split(Parser.TRACK_INFO+":")[1]]={"title":info[0], "url":info[1]}
        return d

    def album_info(self) -> str:
        for x in self.contents:
            if Parser.ALBUM_INFORMATION in x:
                x=x.strip(Parser.ALBUM_INFORMATION+":")
                return x.strip("\n")
        return "Album information not found."
    
    def album_artist(self) -> str:
        for x in self.contents:
            if Parser.ALBUM_ARTIST in x:
                x=x.strip(Parser.ALBUM_ARTIST+":")
                return x.strip("\n")
        return "Album artisit not found"

    def genre(self) -> str:
        for x in self.contents:
            if Parser.ALBUM_GENRE in x:
                x=x.strip(Parser.ALBUM_GENRE+":")
                return x.strip("\n")
        return "Album info not found"

    def group(self) -> str:
        for x in self.contents:
            if Parser.ALBUM_GROUP in x:
                x=x.strip(Parser.ALBUM_GROUP+":")
                return x.strip("\n")
        return "Album group not found"
    
    def display_title(self) ->str:
        for x in self.contents:
            if Parser.PLAYLIST_DISPLAY_TITLE in x:
                x=x.strip(Parser.PLAYLIST_DISPLAY_TITLE+":")
                return x.strip("\n")
        return "Playlist disply title not found."
    
    def playlist(self)->str:
        for x in self.contents:
            if Parser.PLAYLIST_TRACKS in x:
                x=x.strip(Parser.PLAYLIST_TRACKS+":")
                return x.strip("\n")
        return "Playlist for tracks or chapter of an album is not found."
    
    def file_size(self)->str:
        for x in self.contents:
            if Parser.FILE_SIZE in x:
                x=x.strip(Parser.FILE_SIZE+":")
                return x.strip("\n")+" bytes"
        return "File size not mentioned in the file."
    
    def bin_data(self)->str:
        for x in self.contents:
            if Parser.BIN_DATA_FOLLOWS in x:
                x=x.strip(Parser.BIN_DATA_FOLLOWS+":")
                return x.strip("\n")
        return "Binary data follows not found."
    
    def text_encoding(self)->str:
        for x in self.contents:
            if Parser.TEXT_ENCODING in x:
                x=x.strip(Parser.TEXT_ENCODING+":")
                return x.strip("\n")
        return "Text encoding not mentioned in the file."

    def cover_image(self)->str:
        for x in self.contents:
            if Parser.COVER_IMAGE in x:
                x=x.strip(Parser.COVER_IMAGE+":")
                return x.strip("\n")
        return "Cover image or logo not provided in the file."
    
if __name__ == "__main__":
    p = Parser("file.m3u8")
    print(p.version())
    print(p.track_Information())