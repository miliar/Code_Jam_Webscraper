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
int n,p;
int r[55];
int lo[3000],hi[3000],num[3000],del[3000];

int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","wb",stdout);
	cin >> tests;
	FOR (test,1,tests) {
		cerr << test << endl;
		cin >> n >> p;
		REP (i,n) cin >> r[i];
		vector<vector<int> > events;
		vector<int> starts;
		int id=0;
		REP (i,n) {
			REP (j,p) {
				int q;
				cin >> q;
				num[id]=i;
				lo[id]=ceil(q*10.0/(r[i]*11));
				starts.push_back(lo[id]);
				hi[id]=floor(q*10.0/(r[i]*9));
				del[id]=0;
				id++;
			}
		}
		sort(ALL(starts));
		int sol=0;
		for (int x : starts) {
			while (1) {
				vector<vector<PII> > f(n);
				REP (i,id) if (!del[i]) {
					if (lo[i]<=x && x<=hi[i]) {
						f[num[i]].push_back({hi[i],i});
					}
				}
				int ok=1;
				REP (i,n) {
					if (f[i].size()==0) ok=0;
					sort(ALL(f[i]));
				}
				if (!ok) break;
				sol++;
				REP (i,n) {
					del[f[i][0].second]=1;
				}
			}
		}
		printf("Case #%d: %d\n",test,sol);
	}
	return 0;
}
