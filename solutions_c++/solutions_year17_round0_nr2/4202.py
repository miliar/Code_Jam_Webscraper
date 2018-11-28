#include<bits/stdc++.h>
using namespace std;
string s = "";
int l;

void calculate_answer(){
	
	for(int i=1;i<l;i++){
		if(s[i-1]>s[i]){
			s[i-1]--;
			for(int j=i; j<l;j++){
				s[j] = '9';
			}
			calculate_answer();
		}
	}
}
int main(){
	ofstream out("output.out");
	ifstream in("input.in");
	int t;
	in>>t;
	for(int i=1; i<=t;i++){
		in>>s;
		l = s.length();
		calculate_answer();
		string ans="";
		for(int j=0;j<l;j++){
			if(s[j]!='0')
				ans += s[j];
		}
		out<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}