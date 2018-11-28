#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main() {
	ifstream fin;
	ofstream fout;
	fin.open("sample.txt");
	fout.open("answers.txt");
	int t, i, j, T, k, f;
	string s;
	fin>>t;
	for(T=1;T<=t;T++) {
		fout<<"Case #"<<T<<": ";
		fin>>s;
		fin>>k;
		f=0;
		for(i=0;i<=s.length()-k;i++) {
			if(s[i]=='+')
				continue;
			for(j=i;j<i+k;j++) {
				if(s[j]=='-')
					s[j]='+';
				else
					s[j]='-';
			}
			f++;
		} 
		for(i;i<s.length();i++)
			if(s[i]=='-')
				break;
		if(i==s.length())
			fout<<f;
		else
			fout<<"IMPOSSIBLE";
		fout<<endl;
	}
	return 0;
}