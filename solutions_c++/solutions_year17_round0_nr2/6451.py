//Author:CookiC
//#include"stdafx.h"
#include<iostream>
#include<string>
//#pragma warning(disable : 4996)
using namespace std;

int N[20];

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	ios::sync_with_stdio(false);
	
	int T,M,i,len;
	string s;
	cin>>M;
	for(T=1;T<=M;++T){
		cin>>s;
		len=s.size();
		cout<<"Case #"<<T<<": ";
		for(i=0;i<len;++i)
			N[i]=s[i]-'0';
		for(i=0;i<len-1&&N[i]<=N[i+1];++i);
		if(i<len-1){
			while(i>0&&N[i]==N[i-1])
				--i;
			--N[i++];
			while(i<len)
				N[i++]=9;
			if(N[0])
				i=0;
			else
				i=1;
			while(i<len)
				cout<<N[i++];
			cout<<endl;
		}
		else
			cout<<s<<endl;
	}
	return 0;
}

