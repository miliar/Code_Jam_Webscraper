#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <cmath>
#include <string>
#include <queue>
#include <algorithm>


#define MOD 1000000007
#define ll long long
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define pll pair<long long,long long>
#define PI 3.14159

using namespace std;

int main() {
	// your code goes here
	ll t;
	scanf("%lld",&t);
	for(ll j=1;j<=t;j++){
	
	 ll n,k;
	 cin>>n>>k;
	 priority_queue<ll>pq;
	 pq.push(n);
	 for(ll i=1;i<=k-1;i++){
	     ll x=pq.top();
	     pq.pop();
	     pq.push(x/2);
	     pq.push(x-x/2-1);
	 }
	 ll ans1=pq.top()/2;
	 ll ans2=(pq.top()-1)/2;
	 printf("Case #%lld: %lld %lld\n",j,ans1,ans2);
	}
	return 0;
}
