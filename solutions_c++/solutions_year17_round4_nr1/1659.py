#include <string>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define GI ({int _x; scanf("%d",&_x); _x;})

inline int getint() { int x; scanf("%d",&x); return x; }
inline void OPEN(string name) {
	string in = name+".in"; freopen(in.c_str(),"r",stdin);
	string out = name+".out"; freopen(out.c_str(),"w",stdout);
}

// Powered By TimoAI 2.2

int f[8];

int main() {
	OPEN("A");
	REP(nc,getint()) {
		int N = GI;
		int P = GI;
		REP(i,P) f[i] = 0;
		REP(i,N) f[ getint() % P ]++;
		int ans = 0;
		if(P==2) {
			int c1 = f[1] / 2;
			ans = f[0] + c1;
			f[1] -= (c1 * 2);
			if(f[1]>0) ans++;
		}else if(P==3) {
			ans = f[0];
			int c1 = min(f[1],f[2]);
			ans += c1;
			f[1] -= c1;
			f[2] -= c1;

			int sum = 0;
			REP(i,f[2]) {
				sum += 2;
				sum %= P;
				if(sum==0) ans++;
			}
			REP(i,f[1]) {
				sum++;
				sum %= P;
				if(sum==0) ans++;
			}
			if(sum>0) ans++;

		}else {
			FOR(a,0,f[3]) FOR(b,0,N) FOR(c,0,N) {
				int p2 = b+b+c;
				if(p2 > f[2]) break;
				FOR(d,0,N) {

				int p3 = a;

				int p1 = a+c+c+d+d+d+d;
				if(p1 > f[1]) break;

				if(p1 <= f[1] && p2<=f[2] && p3 <=f[3]) {
					int temp = f[0];
					temp += a + b + c + d;
					int s1 = f[1] - p1;
					int s2 = f[2] - p2;
					int s3 = f[3] - p3;
					if(s1+s2+s3 > 0) temp++;
					ans = max(ans,temp);
				}
				}
			}
		}
		printf("Case #%d: %d\n",nc+1,ans);
	}
	return 0;
}
