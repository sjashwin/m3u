# Python: M3U Parser
<p>
<b>M3U</b> is a computer file format for a multimedia playlist.
One common use of the M3U file format is creating a single-entry playlist file pointing to stream on the internet.
The created file provides easy access to that stream and is often used in downloads from a website, for emailing,
and for listening to Internet radio.
</p>

## File Format

There is no specific formal specification for the M3U format; it is a de facto standard.
An M3U file is a plain text file that specifies the location of one or more media files.
The file saved with the "m3u" filename extension if the text is encoded in the local system's default non-Unicode endoding or with "m3u8" extension if the text is UTF-8 encoded. More information can be found [here](https://en.wikipedia.org/wiki/M3U "wikipedia").

## Extended M3U

These are the funtions supported and directives support in this python package.
<table>
    <thead>
        <tr>
            <td>Directives</td>
            <td>Description</td>
            <td>Example</td>
            <td>Function</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>#EXTM3U</td>
            <td>file header, ust be the fist line of the file.</td>
            <td>#EXTM3U</td>
            <td>header()</td>
        <tr>
        <tr>
            <td>#EXTINF:</td>
            <td>track information: runtime in seconds and display title of the following recources</td>
            <td>#EXTINF:123, Artist Name<br>- Track Title</td>
            <td>track_information()</td>
        </tr>
        <tr>
            <td>#EXTLAB:</td>
            <td>album information, title in particular</td>
            <td>#EXTALB: Album Title(2019)</td>
            <td>album_info()</td>
        </tr>
        <tr>
            <td>#EXTART:</td>
            <td>album artist</td>
            <td>#EXTART:Various</td>
            <td>album_artist()</td>
        </tr>
        <tr>
            <td>#EXTGENRE:</td>
            <td>album genre</td>
            <td>#EXTGENRE:Jazz Function</td>
            <td>genre()</td>
        </tr>
        <tr>
            <td>#EXTGRP:</td>
            <td>group</td>
            <td>#EXTGRP:</td>
            <td>group()</td>
        </tr>
        <tr>
            <td>#PLAYLIST:</td>
            <td>playlist display title</td>
            <td>#PLAYLIST:</td>
            <td>display_title()</td>
        </tr>
        <tr>
            <td>#EXTM3A:</td>
            <td>playlist for tracks or chapters of an album in a single file</td>
            <td>#EXTM3A</td>
            <td>playlist()</td>
        </tr>
        <tr>
            <td>#EXTBYT:</td>
            <td>file size in bytes</td>
            <td>#EXTBYT: 2000</td>
            <td>file_size()</td>
        </tr>
        <tr>
            <td>#EXTBIN:</td>
            <td>binary data follows, usually concatented MP3s</td>
            <td>#EXTBIN:</td>
            <td>bin_data()</td>
        </tr>
        <tr>
            <td>#EXTENC:</td>
            <td>text encoding, must be the second line of the file</td>
            <td>#EXTENC: UTF-8</td>
            <td>text_encoding()</td>
        </tr>
        <tr>
            <td>#EXTIMG:</td>
            <td>cover, logo or other image</td>
            <td>#EXTIMG: front cover cover.jpg</td>
            <td>cover_image()</td>
        </tr>
    </tbody>
</table>

## HLS M3U Extensions

<table>
    <thead>
        <tr>
            <td>Directive</td>
            <td>Example</td>
            <td>Description</td>
            <td>Function</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>#EXT-X-START:</td>
            <td>TIME-OFFSET=0</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>#EXT-X-INDEPENDENT-SEGMENTS</td>
            <td>toggle without parameters</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>#EXT-X-PLAYLIST-TYPE:</td>
            <td>VOD or EVENT</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>#EXT-X-TARGETDURATION:</td>
            <td>10</td>
            <td>in seconds</td>
            <td></td>
        </tr>
        <tr>
            <td>#EXT-X-VERSION:</td>
            <td>4</td>
            <td></td>
            <td>version()</td>
        </tr>
        <tr>
            <td>#EXT-X-MEDIA-SEQUENCE:</td>
            <td>0</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>#EXT-X-INDEPENEDNT-SEGMENTS</td>
            <td>toggle without parameters</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>#EXT-X-MEDIA</td>
            <td>NAME="English", TYPE=AUDIO, GROUP-ID="audio-stereo-64", LANGUAGE="en", DEFAULT=YES, AUTOSELECT=YES, URI="english.m3u8"</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>#EXT-X-STREAM-INF:</td>
            <td>BANDWIDTH=1123000, CODESC="avc1.64000f,mp4a.40.2"</td>
            <td>parameters have either one combined value or one per stream, separated by commas</td>
            <td></td>
        </tr>
        <tr>
            <td>#EXT-X-BYTERANGE:</td>
            <td>1024@256000</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>#EXT-X-DISCONTINUITY</td>
            <td>toggle without parameters</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>#EXT-X-DISCONTINUITY-SEQUENCE:</td>
            <td>2</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>#EXT-X-KEY</td>
            <td>METHOD=NONE</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>#EXT-X-MAP:</td>
            <td>URL=MediaInitializationSection</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>#EXT-X-PROGRAM-DATE-TIME:</td>
            <td>2010-02-19T14:54:23.031+08:00</td>
            <td>ISO 8601 format</td>
            <td></td>
        </tr>
        <tr>
            <td>#EXT-X-DATERANGE:</td>
            <td>ID=foo</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>#EXT-X-FRAMES-ONLY</td>
            <td>i-frame toggle without parameters</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>#EXT-X-SESSION-DATA:</td>
            <td>DATA-ID=com.exmaple.movie.title</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>#EXT-X-SESSION-KEY:</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>#EXT-X-ENDLIST</td>
            <td>end-of-list signal without parameters</td>
            <td></td>
            <td></td>
        </tr>
    </tbody>
</table>

## Getting Started

It is as simple as:

```python
from m3u import Parser

filepath="${filepath}/file.m3u8"
p = Parser()
print(p.version()) # 3.0.0
print(p.playlist()) # VOD
```

