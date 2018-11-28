#include <map>
#include <queue>
#include <string>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

#define DEBUGxy(x,y) cerr << #x << " = " << x << ", " << #y << " = " << y << endl;
#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define GI ({int _x; scanf("%d",&_x); _x;})

typedef long long LL; 
inline LL getLL() { LL x; scanf("%I64d",&x); return x; }
inline void OPEN(string name) {
	string in = name+".in"; freopen(in.c_str(),"r",stdin);
	string out = name+".out"; freopen(out.c_str(),"w",stdout);
}

// Powered By TimoAI 2.2

LL N;

int main() {
	OPEN("C");
	REP(nc,GI) {
		N=getLL();
		LL K=getLL();

		priority_queue< LL > pq;
		map<LL,LL> multi;

		pq.push(N);
		multi[N] = 1L;

		while(true) {

			LL length = pq.top(); pq.pop();
			LL person = multi[length];
			// DEBUGxy(length,person);

			LL SR = (length / 2);
			LL SL = (length - SR);

			K-=person; SL--;
			// printf("%I64d %I64d person = %I64d\n",max(SL,SR),min(SL,SR), person);

			if(K<=0) {
				printf("Case #%d: %I64d %I64d\n",nc+1,max(SL,SR),min(SL,SR));
				break;
			}
			if(multi[SL]==0) {
				pq.push(SL);
			}
			multi[SL] += person;

			if(multi[SR]==0) {
				pq.push(SR);
			}
			multi[SR] += person;
		}
	}
	return 0;
}

