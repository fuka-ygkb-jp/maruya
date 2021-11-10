#!/usr/local/bin/perl

require '../../lib/jcode.pl';

open(TXT, "$ARGV[0]");

while (<TXT>) {
&jcode'convert(*_, "euc");
chop($_);
s/([^\x21-\x24\x26-\x7E])/sprintf("%%%02X",unpack("C",$1))/ge;

#print "$_\n";
($txta, $txtb) = split(/%09/, $_);

print "s/$txta/$txtb/g;\n";
}
