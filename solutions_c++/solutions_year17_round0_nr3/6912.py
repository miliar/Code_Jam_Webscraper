#include <iostream>
#include <stdio.h>
#include <queue>
#include <cmath>
using namespace std;
int main(){
	long long N=1000,K=1000,chunk,Ls,Rs;
	int T,casee=1;
	cin>>T;
	while(T--){
		cin>>N>>K;
		priority_queue<int> mypq;
		mypq.push(N);
		while(K--){
			chunk=mypq.top();
			chunk--;
			mypq.pop();
			Ls=chunk/2;
			Rs=chunk-Ls;
			//if(Ls!=0 || Rs!=0)
			//cout<<Ls<<' '<<Rs<<endl;
			if(Ls!=0)
			mypq.push(Ls);
			if(Rs!=0)
			mypq.push(Rs);
		}
		cout<<"Case #"<<casee<<": "<< max(Ls,Rs) <<' '<< min(Ls,Rs)<<'\n';
		casee++;
	}
	return 0;
}