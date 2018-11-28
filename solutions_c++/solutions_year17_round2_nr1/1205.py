#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std;

#define pb push_back
#define ri(x) scanf("%lf",&x)
#define rii(x,y) ri(x),ri(y)
#define ms(obj,val) memset(obj,val,sizeof(obj))
#define ms2(obj,val,sz) memset(obj,val,sizeof(obj[0])*sz)
#define FOR(i,f,t) for(int i=f;i<(int)t;i++)
#define FORR(i,f,t) for(int i=f;i>(int)t;i--)

typedef long long ll;
typedef vector<int> vi;

const int MAXN=1010;

double T,D,N,pos,speed,tm;

int main() {
	ri(T);
	FOR(t,1,T+1) {
		tm=0;
		rii(D,N);
		FOR(i,0,N) {
			rii(pos,speed);
			tm=max(tm,(D-pos)/speed);
		}
		printf("Case #%d: %.6lf\n",t,D/tm);
	}
}