#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <utility>
#include <map>
#include <vector>
#include <set>
#include <cmath>
#include <utility>
#include <queue>
#include <deque>

#define rep(i,a,n) for(int i=a;i<=n;i++)
#define REP(i,a,n) for(int i=a;i<n;i++)
#define mp make_pair
#define pb push_back
#define SZ(x) ((int) (x).size())


using namespace std;

typedef  long long  LL;
typedef  vector<int> VI;
typedef  pair<int,int> PII;


int main(){
	ios::sync_with_stdio(false);
	int T;
	cin>>T;
	rep(pp, 1, T) {
		printf("Case #%d: ", pp);
		int n,k;
		cin>>n>>k;
		priority_queue<int> Q;
		Q.push(n);
		int larger, smaller;
		while(k) {
			int x = Q.top();
			Q.pop();
			if(x&1) {
				larger = (x-1)/2;
				smaller = (x-1)/2;
			} else {
				larger = x / 2;
				smaller = x / 2 - 1;
			}
			Q.push(larger);
			Q.push(smaller);
			k--;
		}
		printf("%d %d\n", larger, smaller);
	}
	return 0;
}