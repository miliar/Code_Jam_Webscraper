#include <vector>
#include <string>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

#define DEBUGxy(x,y) cerr << #x << " = " << x << ", " << #y << " = " << y << endl;
#define ALL(x) x.begin(),x.end()
#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define PB push_back
#define GI ({int _x; scanf("%d",&_x); _x;})

typedef vector<int> VI;
template<class T> inline int size(const T&c) { return c.size(); }
inline void OPEN(string name) {
	string in = name+".in"; freopen(in.c_str(),"r",stdin);
	string out = name+".out"; freopen(out.c_str(),"w",stdout);
}

// Powered By TimoAI 2.2

VI satu;
VI dua;

int A[1024];
int B[1024];
int visit[1024];
int nomor = 1;

bool dfs(int s) {
	if(visit[s]==nomor) return false;
	visit[s] = nomor;
	REP(i,size(dua)) {
		if(satu[s] == dua[i]) continue;
		if(B[i]==-1 || dfs(B[i])) {
			B[i] = s;
			A[s] = i;
			return true;
		}
	}
	REP(i,size(dua)) {
		if(B[i]==-1 || dfs(B[i])) {
			B[i] = s;
			A[s] = i;
			return true;
		}
	}
	return false;
}

int main() {
	OPEN("B");
	REP(nc,GI) {
		int N = GI;
		int C = GI;
		int M = GI;
		satu.clear();
		dua.clear();
		REP(i,M) {
			int pos = GI;
			int own = GI;
			if(own==1) satu.PB(pos);
			else dua.PB(pos);
		}
		sort(ALL(satu));
		sort(ALL(dua));
		REP(i,1024) A[i]=B[i]=-1;
		bool update = true;
		while(update) {
			update = false;
			REP(i,size(satu)) {
				if(A[i]==-1) {
					nomor++;
					if(dfs(i)) update = true;
				}
			}
		}

		int ride = 0;
		int promo = 0;

		int ta = size(satu);
		int tb = size(dua);

		REP(i,max(ta,tb)) {
			if(A[i]==-1 || B[i]==-1) ride++;
			else {
				int a = i;
				int b = A[i];
				ride++;
				if(satu[a]==dua[b]) {
					if(satu[a]==1) {
						if(ta==tb) {
							ride++;
						}
						else {
							if(ta<tb) ta++;
							else tb++;
						}
					}
					else {
						promo++;
					}
				}
			}
		}

		printf("Case #%d: %d %d\n",nc+1,ride,promo);
	}
	return 0;
}

