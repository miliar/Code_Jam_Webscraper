#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <math.h>
#include <queue>
#include <list>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <ctime>
#include <unordered_map>
using namespace std;

#define ALL(c) (c).begin(),(c).end()
#define IN(x,c) (find(c.begin(),c.end(),x) != (c).end())
#define REP(i,n) for (int i=0;i<(int)(n);i++)
#define FOR(i,a,b) for (int i=(a);i<=(b);i++)
#define INIT(a,v) memset(a,v,sizeof(a))
#define SORT_UNIQUE(c) (sort(c.begin(),c.end()), c.resize(distance(c.begin(),unique(c.begin(),c.end()))))
template<class A, class B> A cvt(B x) { stringstream ss; ss<<x; A y; ss>>y; return y; }

typedef pair<int,int> PII;
typedef long long int64;

int tests;
int64 n,k;

int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","wb",stdout);
	cin >> tests;
	FOR (test,1,tests) {
		cerr << test << endl;
		printf("Case #%d: ",test);
		cin >> n >> k;
		map<int64, int64, greater<int64> > f;
		f[n]=1;
		int64 m=-1,M=-1;
		while (k>0) {
			int64 l=f.begin()->first, c=f.begin()->second;
			f.erase(f.begin());
			k-=c;
			if (l%2==1) {
				m=(l-1)/2; M=l-1-m;
			} else {
				m=l/2-1; M=l-1-m;
			}
			f[m]+=c;
			f[M]+=c;
		}
		printf("%I64d %I64d\n",M,m);
	}
	return 0;
}
