#include <bits/stdc++.h>
using namespace std;
long T,K,l,ans,flag;
string S;
int main(){
	cin>>T;
	for (int t=1; t<=T; t++){
		cout<<"Case #"<<t<<": ";
		cin>>S;
		cin>>K;
		l=S.size();
		ans=0;
		int i;
		for(i=1; i<=l-K; i++){
			if(S[i-1]=='-'){
				ans++;
				for(int j=0; j<K; j++){
					if(S[i-1+j]=='-')	S[i-1+j]='+';
					else				S[i-1+j]='-';
				}
			}
		}
		flag=1;
		if(S[i-1]=='-'){
			ans++;
			for(int j=0; j<K; j++){
				if(S[i-1+j]=='+') flag=0;
			}
		}else{
			for(int j=0; j<K; j++){
				if(S[i-1+j]=='-') flag=0;
			}
		}
		if(flag)	cout<<ans<<endl;
		else		cout<<"IMPOSSIBLE"<<endl;
	}

}