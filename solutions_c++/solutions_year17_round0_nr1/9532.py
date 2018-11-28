#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int T;
string s;
int k;
int n;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin.sync_with_stdio(false);
	cin>>T;
	for(int tt=1;tt<=T;tt++){
		cin>>s>>k;
		int nm=0;
		n=s.length();
		for(int i=0;i<n-k+1;i++){
			if(s[i]=='-'){
				nm++;
				for(int j=i;j<i+k;j++){
					if(s[j]=='-'){
						s[j]='+';
					} else {
						s[j]='-';
					}
				}
			}
		}
		bool ok=true;
		for(int i=0;i<n;i++){
			if(s[i]=='-'){
				ok=false;
			}
		}
		cout<<"Case #"<<tt<<": ";
		if(ok){
			cout<<nm<<endl;
		} else {
			cout<<"IMPOSSIBLE"<<endl;
		}
	}
}