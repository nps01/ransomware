# ransomware

This is a really basic piece of malware that I wrote in python that encrypts all of the text files in the directory that the malware executable is launched.  The script can be run without using the executable: <code> python worm.py </code>.  The executable is in the sandbox directory with some test files that will get encrypted if you launch the executable.  

XOR Encryption

XOR outputs 1 or True if both input bits are different (1 & 0) and it outputs 0 or False if both ouput bits are the same (1 & 1 or 0 & 0).

<table>
  <tbody>
    <tr>
      <td> variable name</td><td>base 10 (decimal)</td><td>base 2 (binary)</td>
     </tr>
    <tr>
      <td> A</td><td>4</td><td>0100</td>
     </tr>
    <tr>
      <td> B</td><td>11</td><td>1011</td>
     </tr>
    <tr>
      <td> A XOR B</td><td> 0100 XOR 1011 </td><td>1111</td>
     </tr>
  </tbody>
</table>


Creating the Executable

Spoofing the File Icon and Extension
