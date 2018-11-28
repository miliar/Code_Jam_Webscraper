#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <map>
#include <cstdlib>
#include <cmath>
#include <string>
#include <algorithm>
#include <set>
#include <stack>
#include <queue>
#include <utility>
#include <bitset>
#define fi first
#define se second
#define rep(i,a,b) for (int i=(a);i<(b);i++)
#define per(i,a,b) for (int i=(b)-1;i>=(a);i--)
#define REP(i,a,b) for (int i=(a);i<=(b);i++)
#define PER(i,a,b) for (int i=(b);i>=(a);i--)
using namespace std;
typedef long long LL;

const int INF = 0x3f3f3f3f;

const int MAXN = 1000005; // 1e6;
int n;
int N,T;
double D,s[MAXN],k[MAXN];
int main()
{
	freopen("A-large.in.txt","r",stdin);
	freopen("Large.out","w",stdout);
	cin>>T;
	rep(cas,1,T+1)
	{
		cin>>D>>N;
		rep(i,0,N) cin>>k[i]>>s[i];
		double t = 0;
		rep(i,0,N) t=max(t,(D-k[i])/s[i]);
		printf("Case #%d: %.8f\n",cas, D/t);
	}


}

