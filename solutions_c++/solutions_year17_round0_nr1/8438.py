#include <iostream>
#include <stdio.h>
#include <cmath>
#include <stdlib.h>
#include <algorithm>
#include <bitset>
using namespace std;

int main(){
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	string cake;
	bitset<1000> cak;
	int l,K;
	int cnt;
	bool flag;
	int j,h;
	for(int i = 1;i<=T;i++){
		cin>>cake;
		l = cake.length();
		cin>>K;
		cnt = 0;
		flag = true;
		for(j = 0;j < l;j++){
			if(cake[j]=='+')cak[j] = 1;
			else cak[j] = 0;
		}
		for(j = K;j <= l;j++){
			if(cak[j-K]==0){
				cnt++;
				for(h = j-K;h<j;h++){
					cak.flip(h);
				};
			}
		}
		for(j = l-K+1;j<l;j++){
			if(cak[j]==0){flag = false;break;};
		}
		if(flag)cout<<"Case #"<<i<<": "<<cnt<<endl;
		else{ cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
		}
	}


}