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
	int d,n,k,s;
	freopen("A-large.in", "r", stdin);
	freopen("program.out", "w", stdout);
	cin>>tc;
	for (int ti = 0; ti < tc; ++ti) {
		double t=0;
		cin>>d>>n;
		for (int i = 0; i < n; ++i) {
			cin>>k>>s;
			t=max(t,(d-k)/(double)s);
		}
		printf("Case #%d: %lf\n",ti+1,d/t);
		
	}
	
	
	return 0;
}
