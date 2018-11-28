
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;


int main() {
fstream infile, outfile;
    infile.open("input2.txt", ios::in);
    outfile.open("output2.txt", ios::out);
	int t;
	int a=-1;
	infile>>t;

for(int e=0;e<t;e++){
string s;
infile>>s;

while(a==-1){
for(int i=1;i<s.length();i++){
if(s[i-1]>s[i]){

s[i-1]=s[i-1]-1;
for(int o=i;o<s.length();o++){
    s[o]='9';
}
a++;
}
}
if(a==-1){
    break;
}
else{a=-1;}
}

if(s[0]=='0'){
    s=s.substr(1);
}
outfile<<"Case #"<<(e+1)<<": "<<s<<endl;
}
 return 0;
}
