#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cmath>
using namespace std;

typedef vector<int> vi;
typedef pair<int,int> pii;
typedef vector<pii> vii;

#define ri(x) scanf("%d", &x)
#define rii(x,y) scanf("%d%d", &x, &y)
#define FOR(i,S,E) for(int i=S; i<E; i++)
#define fst first
#define snd second
#define mp make_pair
#define pb push_back

int noventa(int t) {
	return (ceil(90.0*t/100.0));
}
int ciento10(int t) {
	return (ceil(110.0*t/100.0));
}
int porc(int t, int m) {
	return (ceil(m*100.0/t));
}

int main() {
	int T; ri(T);
	FOR(t,1,T+1) {
		vi oc;
		int N,P; rii(N,P);
		vi R;
		FOR(i,0,N) {
			int inp; ri(inp);
			R.pb(inp);
		}
		vector < multiset<int> > Q;
		Q.resize(N);
		FOR(i,0,N) {
			FOR(j,0,P) {
				int inp; ri(inp);
				Q[i].insert(inp);
			}
		}
		int ans=0, idx=1;
		multiset<int>::iterator it = Q[0].begin();
		while(it != Q[0].end()) {

			int l=noventa(idx*R[0]), r=ciento10(idx*R[0]);
			if (l > *it) {
				it++;
				continue;
			}
			bool bad=0;
			while(!(*it >= l && *it <= r) && l <= *it) {
				idx++;
				l = noventa(idx*R[0]);
				r=ciento10(idx*R[0]);
			}
			if (l > *it) {
				it++;
				continue;
			}
			//printf("%d\n", idx);
			//printf("\t%d <= %d <= %d\n", l, *it, r);
			int count=1;
			vii aux;
			FOR(i,1,N) {
				int l1 = noventa(idx*R[i]), r1 = ciento10(idx*R[i]);
				multiset<int>::iterator itt = Q[i].begin();
				while(itt != Q[i].end() && !(*itt >= l1 && *itt <= r1)) {
					//printf("\t\t%d <= %d <= %d\n", l1, *itt, r1);
					itt++;
				}
				if (itt == Q[i].end()) break;
				//printf("\t%d\n", *itt);
				aux.pb({*itt, i});
				Q[i].erase(itt);
				count++;
			}
			//printf("\tcount: %d\n", count);
			if (count == N) {
				ans++;
				it++;
				idx=1;
			}
			else {
				FOR(i,0,aux.size()) {
					int id = aux[i].snd;
					Q[id].insert(aux[i].fst);
				}
				idx++;
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
}
