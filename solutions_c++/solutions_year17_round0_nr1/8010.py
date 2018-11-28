#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;


int main() {
    fstream infile, outfile;
    infile.open("input.txt", ios::in);
    outfile.open("output.txt", ios::out);
	int t;
	infile>>t;
    string s;
	int k;
	int count=0;
for(int e=0;e<t;e++){
        count=0;
        infile>>s;
        infile>>k;

        for(int i=0;i<s.length()-k+1;i++){
        if(s[i]=='-'){
            for(int o=0;o<k;o++){
                if(s[i+o]=='+'){
                    s[i+o]='-';
                }
                else if(s[i+o]=='-'){
                    s[i+o]='+';
                }
            }
            count++;
        }

    }

    for(int o=0;o<k-1;o++){
                if(s[s.length()-o-1]=='-'){
                    count=-1;
                    break;
                }
            }

if(count==-1){
    outfile<<"Case #"<<(e+1)<<": "<<"IMPOSSIBLE"<<endl;
}
else{
    outfile<<"Case #"<<(e+1)<<": "<<count<<endl;
}
	}
    return 0;
}
