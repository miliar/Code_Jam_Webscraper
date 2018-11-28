#include <bits/stdc++.h>
using namespace std;

int main(){
    fstream fin,fout;
    fin.open("inputl.in");
    fout.open("output.txt");
	int t;
	fin>>t;
	for (int cs=1; cs<=t; cs++){
		fout<<"Case #"<<cs<<": ";

		string s;
		fin>>s;
		int i1=-1, i2;
		for (int i=0; i<s.length()-1; i++){
			if (s[i]>s[i+1]){
				i1 = i;
				i2 = i+1;
				break;
			}
		}
		if (i1 >= 0){
			if (s[i1] == '1'){
				for (int i=0; i<s.length()-1; i++) fout<<"9";
			} else {
				while (s[i1] == s[i1-1] && i1>0){
					i1--; i2--;
				}
				s[i1]--;
				for (int i=i2; i<s.length(); i++) s[i] = '9';
				fout<<s;
			}
		} else {
			fout<<s;
		}


		fout<<endl;
	}
}
