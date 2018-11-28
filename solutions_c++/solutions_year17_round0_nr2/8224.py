#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

ofstream fout("output.txt");
ifstream fin("input.txt");

char minus1(char c){

	switch(c){

		case '1':return '0';
		case '2':return '1';
		case '3':return '2';
		case '4':return '3';
		case '5':return '4';
		case '6':return '5';
		case '7':return '6';
		case '8':return '7';
		case '9':return '8';
	}

}

int main(){

	ll t,counter=0,i,j;

	fin>>t;

	while(t--){

		string s;

		fin>>s;

		for(i=s.size()-1;i>0;--i){

				if(s[i-1]>s[i]){

					s[i-1]=minus1(s[i-1]);

					for(j=i;j<s.size();++j) s[j]='9';

				}

			

		}

		fout<<"Case #"<<++counter<<": ";

		if(s[0]!='0') for(i=0;i<s.size();++i) fout<<s[i];

		else for(i=0;i<s.size()-1;++i) fout<<'9';

		fout<<"\n";
		

	}


}