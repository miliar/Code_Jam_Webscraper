/*	In the name of God	*/
#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <cctype>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
#include <sstream>
#include <bitset>
#include <map>
#include <set>
#include <queue>
#include <stack>

#define rep(i,n) for((i)=0;(i)<(n);(i)++)
typedef long long ll;

using namespace std;

priority_queue<ll> q;
int main(){
	int tc;
	ll n,k;
	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("program.out", "w", stdout);
	cin>>tc;
	for (int ti = 0; ti < tc; ++ti) {
		while (!q.empty())
			q.pop();
		cin>>n>>k;
		q.push(n);
		for (int i = 0; i < k; ++i) {
			n=q.top();
			q.pop();
			q.push(n/2);
			q.push((n-1)/2);
		}
		printf("Case #%d: %lld %lld\n",ti+1,n/2,(n-1)/2);
		
	}
	
	
	return 0;
}