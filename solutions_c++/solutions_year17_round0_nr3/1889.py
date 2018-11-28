#include<bits/stdc++.h>
using namespace std;
#define REP(i,a,b)for(int i=(a),i##_end_=(b);i<i##_end_;++i)
#define PER(i,a,b)for(int i=(b)-1,i##_end_=(a);i>=i##_end_;--i)
#define pb push_back
#define fi first
#define se second
template<class T>inline bool umx(T& A,const T& B){return A<B?A=B,1:0;}
template<class T>inline bool umn(T& A,const T& B){return A>B?A=B,1:0;}
typedef long long LL;
typedef double db;
typedef pair<int,int> PII;
typedef pair<db,int> PDI;

LL n,k;
void solve(){
	scanf("%lld%lld",&n,&k);
	LL odd=0,even=0;
	(n&1) ? ++odd : ++even;
	for(;;){
		if(odd+even >= k){
			if(n&1){		// odd is bigger
				if(odd >= k){
					printf("%lld %lld\n",(n-1)/2,(n-1)/2);
				}else{
					printf("%lld %lld\n",(n-1-1+1)/2,(n-1-1)/2);
				}
			}else{
				if(even >= k){
					printf("%lld %lld\n",(n-1+1)/2,(n-1)/2);
				}else{
					printf("%lld %lld\n",(n-1-1)/2,(n-1-1)/2);
				}
			}
			return;
		}
		
		k-=(odd+even);
		
		LL ox,ex;
		if(n&1){
			ox=n;ex=n-1;
		}else{
			ox=n-1;ex=n;
		}
		
		LL no=0,ne=0;
		if(ox>1){
			if(((ox-1)/2)&1)no+=odd<<1;else ne+=odd<<1;
		}
		no+=even;
		if(ex>2)ne+=even;
		
//		printf("%lld %lld\n",no,ne);
		odd=no,even=ne;
//		printf("%lld %lld\n",odd,even);
		n=n/2;
	}
}
int main(){
//	freopen("in.txt","r",stdin);
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int _,__=0;scanf("%d",&_);
	while(_--){
		printf("Case #%d: ",++__);
		solve();
	}
	return 0;
}

