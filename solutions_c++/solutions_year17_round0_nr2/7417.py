#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main() {
	ifstream fin;
	ofstream fout;
	fin.open("sample.txt");
	fout.open("answers.txt");
	long long int t, i, j, T, p, k;
	fin>>t;
	string s;
	for(T=1;T<=t;T++) {
		fout<<"Case #"<<T<<": ";
		fin>>s;
		p=0;
		for(k=0;k<18;k++) {
			for(i=1;i<s.length();i++) {
				if(s[i-1]>s[i]) {
					s[i-1]--;
					for(j=i;j<s.length();j++) {
						s[j]='9';
					}
					break;
				}
			}
		}
		for(i=0;i<s.length();i++) {
			if(s[i]!='0')
				fout<<s[i];
		}
		fout<<endl;
	}
	return 0;
}