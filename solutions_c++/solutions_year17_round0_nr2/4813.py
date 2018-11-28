#include <bits/stdc++.h>
using namespace std;

string S,s;
long T, l, Start, i;
int main(){
	cin>>T;
	for(int t=1; t<=T; t++){
		cout<<"Case #"<<t<<": ";
		cin>>S;
		s=S;
		l=S.size();
		Start=l;
		for(i=l-1; i>0; i--){
			if(S[i]<S[i-1]){
				S[i-1]--;
				Start=i;
			}
		}
		i=0;
		while(S[i]=='0' && i<Start)i++;
		for(; i<l; i++){
			if(i>=Start)cout<<9;
			else {
				cout<<S[i];
			}
		}
		cout<<endl;
	}
}