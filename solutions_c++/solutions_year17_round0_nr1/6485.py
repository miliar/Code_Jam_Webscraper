//Author:CookiC
//#include"stdafx.h"
#include<iostream>
#include<string>
//#pragma warning(disable : 4996)
using namespace std;

int K;
string S;

void flip(int n){
	int i;
	for(i=n;i<n+K;++i)
		if(S[i]=='+')
			S[i]='-';
		else
			S[i]='+';
	
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	ios::sync_with_stdio(false);
	
	int cnt,i,T,N;
	cin>>N;
	for(T=1;T<=N;++T){
		cin>>S>>K;
		cnt=0;
		for(i=0;i<S.size()-K+1;++i)
			if(S[i]=='-'){
				flip(i);
//				cout<<S<<endl;
				++cnt;
			}
		
		while(i<S.size()&&S[i]=='+')
			++i;
		
		cout<<"Case #"<<T<<": ";
		if(i<S.size())
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<cnt<<endl;
	}
	return 0;
}

