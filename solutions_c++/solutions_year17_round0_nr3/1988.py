#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll n,k;
map <ll,ll> m;
int main()
{
	int t;
	scanf("%d",&t);
	for (int asd=1;asd<=t;asd++){
		scanf("%lld%lld",&n,&k);
		m.clear();
		priority_queue <ll> pq;
		pq.push(n);
		m[n]=1;
		while (k){
			ll top=pq.top();
			pq.pop();
			ll jum=m[top];
			ll mini=top/2 - (top&1?0:1),maxi=top/2;
			if (k<=jum){
				printf("Case #%d: %lld %lld\n",asd,maxi,mini);
				break;
			}
			k-=jum;
			if (!m[mini]) pq.push(mini);
			m[mini]+=jum;
			if (!m[maxi]) pq.push(maxi);
			m[maxi]+=jum;
		}
	}
}