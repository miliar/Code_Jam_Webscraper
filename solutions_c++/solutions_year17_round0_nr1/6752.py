#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

char flip(char c){
	if(c=='+')
		return '-';
	else
		return '+';
	}

int main(){
int T;
cin>>T;
for(int t=1;t<=T;t++){
	string s;
	int k,c=0,f=0;
	cin>>s;
	cin>>k;
	for(int i=0;i<(s.length()-k+1);i++){
		if(s[i]=='-'){
			c++;
			for(int j=0;j<k;j++)
				s[i+j]=flip(s[i+j]);
			
			}
		}
	for(int j=0;j<k;j++){
		if(s[s.length()-j-1]=='-')
			f=1;
		}
	if(f==0)
		cout<<"Case #"<<t<<": "<<c<<endl;
	else
		cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;
	}
	
}
