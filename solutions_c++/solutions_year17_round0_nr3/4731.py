#include <bits/stdc++.h>
using namespace std;
#define ll long long
priority_queue<ll> pq;
map<ll,ll> freq;
int main(){
	int t,tt;
	ll n,k,l,r;
	cin >> t;
	for(tt=1;tt<=t;tt++){
		scanf(" %lld %lld",&n,&k);
		while(!pq.empty())
			pq.pop();
		freq.clear();
		pq.push(n);
		freq[n]=1;
		while(k>0){
			n=pq.top();
			pq.pop();
			l=n/2;
			r=(n-1)/2;
			k-=freq[n];
			if(!freq[l])
				pq.push(l);
			freq[l]+=freq[n];
			if(!freq[r])
				pq.push(r);
			freq[r]+=freq[n];
		}
		printf("Case #%d: %lld %lld\n",tt,l,r);
	}
}