#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<queue>
#include<map>
#include<cmath>
#define ll long long
using namespace std;
int T;
map<ll,ll> m;
ll n,k,c,a;
int main(){
	scanf("%d",&T);
	for (int I=1;I<=T;I++){
		priority_queue<ll> q;
		m.clear();
		scanf("%lld%lld",&n,&k);
		q.push(n);
		m[n]=1;
		c=0;
		while (c<k){
			a=q.top();
			q.pop();
			c+=m[a];
			if (c>=k) break;
			if (m[a/2]==0) q.push(a/2);
			m[a/2]+=m[a];
			if (m[(a-1)/2]==0) q.push((a-1)/2);
			m[(a-1)/2]+=m[a];
		}
		printf("Case #%d: %lld %lld\n",I,a/2,(a-1)/2);
	}
    return 0;
}

