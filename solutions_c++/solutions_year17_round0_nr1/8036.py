//============================================================================
// Name        : GCJ.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;
int T;
int main() {
	cin>>T;
	for(int i=1;i<T+1;++i){
		string str;
		int K;
		int d[1000]={};
		int count=0;
		int l=0;
		int total=0;
		int flg=0;
		cin>>str>>K;
		for(int j=0;j<str.length()-K+1;++j){
			if(j>=K)count-=d[j-K];
			l=0;
			if(str[j]=='-')l=1;
			if((count+l)%2>0){
				d[j]=1;
				count+=1;
				total++;
			}
		}
		for(int j=str.length()-K+1;j<str.length();++j){
			if(j>=K)count-=d[j-K];
			l=0;
			if(str[j]=='-')l=1;
			if((count+l)%2>0)flg=1;
//			cout<<count<<endl;
		}
		if(flg==1){
			cout << "Case #" << i<<": IMPOSSIBLE"<<endl;
		}else{
			cout << "Case #" << i<<": "<<total<<endl;
		}
	}
	return 0;
}
