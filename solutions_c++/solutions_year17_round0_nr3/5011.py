#include<bits/stdc++.h>
using namespace std;
//#define i64 long long;

map<long long,long long> myMap;
map<long long,long long>::iterator it;

long long getResult(long long N,long long K)
{
	myMap[N] = 1;
	queue<long long>Q;
	Q.push(N);
	while(!Q.empty()) {
		long long u = Q.front();
		//cout<<u<<endl;
		Q.pop();
		if(!u)continue;
		if(u & 1){
			long long x = u/2;
			if(myMap.count(x)){
				myMap[x] += 2 * myMap[u];
			} else {
				myMap[x] = 2*myMap[u];
				Q.push(x);
			}
			//cout<<"Adding "<<x<<" 2*"<<myMap[u]<<endl;
		} else {
			long long x = u/2;
			if(myMap.count(x)){
				myMap[x] +=  myMap[u];
			} else {
				myMap[x] = myMap[u];
				Q.push(x);
			}
			//cout<<"Adding "<<x<<" 1*"<<myMap[u]<<endl;
			long long y = u/2 - 1;
			if(myMap.count(y)){
				myMap[y] +=  myMap[u];
			} else {
				myMap[y] = myMap[u];
				Q.push(y);
			}
			//cout<<"Adding "<<y<<" 1*"<<myMap[u]<<endl;
		}
	}
	long long z=0;
	for(auto it = myMap.rbegin(); ; it++) {
		if(it==myMap.rend())break;
		long long x=it->first; 
		z+=myMap[x];
		if(z>=K)return x;
	}
	return 1;
}


int main()
{
		freopen("C-large.in","r",stdin);
		freopen("C_large.out","w",stdout);
		int T,cas=0;
		scanf("%d",&T);
		while(T--){
			myMap.clear();
			long long N,K;
			cin>>N>>K;
			long long x=getResult(N,K),res1,res2;
			if(x & 1){
				res1 = (x/2);
				res2 = (x/2);
			} else {
				res1 = (x/2);
				res2 = (x/2) - 1;
			}
			printf("Case #%d: %lld %lld\n", ++cas, res1, res2);
		}
		return 0;
}

