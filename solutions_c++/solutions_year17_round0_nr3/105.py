#include<stdio.h>
#include<map>
using namespace std;
#define int64 long long int
map<int64,int64> Map;
int64 sim(int64 n,int64 k){
	Map.clear();
	Map[n]++;
	while(!Map.empty()){
		int64 A = Map.rbegin() -> first;
		int64 B = Map.rbegin() -> second;
		if(B >= k)return A;
		Map.erase(A);
		k -= B;
		--A;
		if(A/2)Map[A/2] += B;
		if(A-A/2)Map[A-A/2] += B;
	}
	return -1;
}
int main(){
	int _,t;int64 n,k;
	scanf("%d",&_);
	for(t=1; t<=_; t++){
		scanf("%I64d%I64d",&n,&k);
		printf("Case #%d: ",t);
		int64 L = sim(n,k) - 1;
		printf("%I64d %I64d\n",L-L/2,L/2);
	}
	return 0;
}
