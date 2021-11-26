This scripts changes all files names with a convention:
BRAND_COUNTRY_LANGUAGE_fileName

NOTE: COUNTRY is actually the parent folder's name so it could not be the real country name.

This script tries to find out the language of the file from it's title as most of the files have ISO_CODE2 (e.g. "FR") in the name. If it can't find any reference than it puts "UNKNOWN" as the language. It's recommended to check manually wether the language has been selected properly or not!  

It also generates a .html FILE that has the list of all the file names that has been changed with reference to what it was before and after the change. (this files extension is just for having a bit of colors in it to identify better one file from another. You can change it into .xml, it doesn't matter)
