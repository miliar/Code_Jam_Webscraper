#include<iostream>
#include<fstream>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
	int t,T,i,j,l,count,flag;
	string s;
	ifstream in;
	ofstream out;

	in.open("q2l.in");
	out.open("a2.out");

	in>>T;
	for(t=1;t<=T;t++){
		in>>s;
		l=s.length();
		
		for(i=l-1;i>0;i--){
			if(s[i]=='0' || s[i]<s[i-1]){
				for(j=i;j<l;j++){
					s[j]='9';
				}
				s[i-1]--;
			}
		}
		out<<"Case #"<<t<<": ";
		if(s[0]!='0')
			out<<s;
		else{
			for(i=1;i<l;i++){
				out<<s[i];
			}
		}
		out<<endl;
	}


	return 0;
}

