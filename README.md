## Hand-made Trimmomatic

***input:*** untrimmed fastq file, arguments  
***standart output:*** trimmed fastq file

### Usage and arguments
***usage***  trim_Skalon.py [-h] -i Str -o Str [-d Int] [-t Int]
 
***example***  
python trim_Skalon.py -i test.fastq -o trimmed.fastq -d 10 -t 5

***arguments***  
  -h, --help            show this help message and exit
  -i Str, --input Str   Input file
  -o Str, --output Str  Output file
  -d Int, --head Int    Score for headcrop
  -t Int, --tail Int    Score for tailcrop

 
