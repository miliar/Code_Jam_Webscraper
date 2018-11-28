#include <bits/stdc++.h>
using namespace std;

long T,N,K,Top,Mid;
int main(){
	cin>>T;
	for(int t=1; t<=T; t++){
		cout<<"Case #"<<t<<": ";
		cin>>N;
		cin>>K;
		multiset <long> S;
		S.insert(N);
		for(int i=1; i<K; i++){
			Top=*(S.rbegin());
			S.erase(prev(S.end()));
			Mid=Top/2+Top%2;

			S.insert(Mid-1);
			S.insert(Top-Mid);
		}
		Top=*(S.rbegin());
		Mid=Top/2+Top%2;
		cout<<max(Mid-1, Top-Mid)<<' '<<min(Mid-1, Top-Mid)<<endl;
	}
}