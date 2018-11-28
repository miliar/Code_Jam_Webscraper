#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main(){
	int T;
	ifstream input;
	input.open("q1l.in");
	input>>T;
	for(int t=1;t<=T;t++){
		string s;
		int k,i=0,j,l,count=0;
		input>>s>>k;
		l=s.length();
		while(i+k<=l){
			if(s[i]=='-'){
				for(j=i;j<i+k && j<l;j++){
					if(s[j]=='-')
						s[j]='+';
					else
						s[j]='-';
				}
				count++;
			}
			i++;
		}
		cout<<"Case #"<<t<<": ";
		for(j=l-k;j<l;j++){
			if(s[j]!='+'){
				cout<<"IMPOSSIBLE"<<endl;
				break;
			}
		}
		if(j==l){
			cout<<count<<endl;
		}
	}
}
