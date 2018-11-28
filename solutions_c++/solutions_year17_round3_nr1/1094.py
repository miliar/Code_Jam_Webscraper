#include <bits/stdc++.h>
//#include <iostream>
//#include <algorithm>

using namespace std;

typedef struct _pan{
	long long int ra;
	long long int res;
} pan;

bool sortpan(pan a, pan b){
	return (a.res>b.res);
}

int main(){
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		pan cake[1000];
		int N,K;
		long long int h;
		long long int ans=0;
		long long int sum=0;
		cin>>N>>K;
		for(int n=0;n<N;n++){
			cin>>cake[n].ra>>h;
			cake[n].res=2*cake[n].ra*h;
		}
		sort(&cake[0], &cake[N], sortpan);
		int k;
		for(k=0;k<K;k++){
			sum+=cake[k].res;
			if(ans<cake[k].ra) ans=cake[k].ra;
		}
		ans=ans*ans+sum;
		sum-=cake[K-1].res;
		for(;k<N;k++){
			if(ans<sum+cake[k].res+cake[k].ra*cake[k].ra){
				ans=sum+cake[k].res+cake[k].ra*cake[k].ra;
			}
		}
		cout.precision(9);
		cout<<"Case #"<<t<<": "<<fixed<<3.141592653589793L*(long double)ans<<endl;
	}
	return 0;
}
