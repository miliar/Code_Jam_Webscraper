#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <functional>
#include <iostream>
#define MOD 1000000007LL
using namespace std;
typedef long long ll;
typedef pair<int,int> P;

int t;
ll n,k;
int len[100];

int main(void){
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		scanf("%lld%lld",&n,&k);
		ll res1,res2;
		int cnt=0;
		ll all=1;
		memset(len,0,sizeof(len));
		while(all<=k){
			all*=2LL;
			cnt++;
		}
		all/=2LL;
		cnt--;
		ll rest=n-(all-1LL);
		ll val=rest/all;
		ll rem=rest%all;
		ll k2=k-all;
		if(k2<rem){
			res1=(val+1)/2LL;
			res2=val/2LL;
		}else{
			res1=val/2LL;
			res2=(val-1LL)/2LL;
		}
		printf("Case #%d: %lld %lld\n",i+1,res1,res2);
	}
	return 0;
}
