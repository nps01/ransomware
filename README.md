# ransomware

This is a really basic piece of malware that I wrote in python that encrypts all of the text files in the directory that the malware executable is launched.  The script can be run without using the executable: <code> python worm.py </code>.  The executable is in the sandbox directory with some test files that will get encrypted if you launch the executable.  

XOR Encryption
given to integers: 
<table>
  <tbody>
    <tr>
      <td> variable name</td><td>base 10 (decimal)</td><td>base 2 (binary)</td>
     </tr>
    <tr>
      <td> A</td><td>4</td><td>100</td>
     </tr>
    <tr>
      <td> B</td><td>0010</td><td>1011</td>
     </tr>
  </tbody>
</table>
A = 4, B = 11


Creating the Executable

Spoofing the File Icon and Extension
