# Python: M3U Parser
<p>
<b>M3U</b> is a computer file format for a multimedia playlist.
One common use of the M3U file format is creating a single-entry playlist file pointing to stream on the internet.
The created file provides easy access to that stream and is often used in downloads from a website, for emailing,
and for listening to Internet radio.
</p>

## File Format

<p>
There is no specific formal specification for the M3U format; it is a de facto standard.
An M3U file is a plain text file that specifies the location of one or more media files.
The file saved with the "m3u" filename extension if the text is encoded in the local system's default non-Unicode endoding or with "m3u8" extension if the text is UTF-8 encoded.
</p>

## Exntended M3U
<table>
    <th>
        <tr>
            <td>Directives</td>
            <td>Description</td>
            <td>Exmaple</td>
            <td>Function</td>
        </tr>
    <th>
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

