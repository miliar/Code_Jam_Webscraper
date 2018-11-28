#include <iostream>
#include <iomanip>
#include <climits>
#include <stack>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <cassert>

#define FOR(i,n) for(int i=0,_n=n;i<_n;i++)
#define FORR(i,s,n) for(int i=s,_n=n;i<_n;i++)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define pli pair<ll,int>
#define vi vector<int>
#define fs first
#define sec second

#define maxn 100000

using namespace std;
typedef long long ll;

const ll MOD = 1000000007LL;

void solve(int prim){
	ll n,k;
	cin >> n >> k;
	k--;
	map<ll,ll> rng;
	rng[n]=1;
	while(k){
		ll size = rng.rbegin()->fs;
		ll num = rng.rbegin()->sec;
		if(num>k){
			rng.rbegin()->sec -= k;
			break;
		}
		rng.erase(size);
		k-=num;
		if(size==1)break;
		ll a,b;
		if(size&1)a=b=size/2;
		else{
			a=size/2;
			b=size/2-1;
		}
		if(b>0){
			if(rng.find(b)!=rng.end())rng[b]+=num;
			else rng[b]=num;
		}
		if(rng.find(a)!=rng.end())rng[a]+=num;
		else rng[a]=num;
	}
	ll last = rng.rbegin()->fs;
	ll a,b;
	if(last&1)a=b=last/2;
	else {a=last/2;b=last/2-1;}
	printf("Case #%d: %lld %lld\n",prim,a, b);
}

int main(){
	int n;
	scanf("%d",&n);
	FORR(i,1,n+1)solve(i);
	return 0;
}
