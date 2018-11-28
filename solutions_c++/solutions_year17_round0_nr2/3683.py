#include <vector>
#include <string>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

#define DEBUGx(x) cerr << #x << " = " << x << endl;
#define ALL(x) x.begin(),x.end()
#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FOREACH(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define PB push_back
#define MP make_pair
#define GI ({int _x; scanf("%d",&_x); _x;})
#define ND second

typedef long long LL;
template<class T> inline int size(const T&c) { return c.size(); }
inline LL getLL() { LL x; scanf("%I64d",&x); return x; }
inline void OPEN(string name) {
	string in = name+".in"; freopen(in.c_str(),"r",stdin);
	string out = name+".out"; freopen(out.c_str(),"w",stdout);
}

// Powered By TimoAI 2.2

char S[32];
vector< pair<int,string> > ans;

bool tidy(LL N) {
	char temp[32];
	sprintf(temp,"%I64d",N);
	REP(i,strlen(temp)) {
		if(i==0) continue;
		if(temp[i] >= temp[i-1]) continue;
		return false;
	}
	return true;
}

LL brutal(LL N) {
	if(N<10) return N;
	while(N>0) {
		if(tidy(N)) return N;
		N--;
	}
	return 0;
}

int main() {

	OPEN("B");

	REP(nc,GI) {

		ans.clear();

		LL N = getLL();
		printf("Case #%d: ",nc+1);
		if(N < 10 || tidy(N)) printf("%I64d\n",N);
		else {
			sprintf(S,"%I64d",N);



			int len = strlen(S);


			REP(i,len) {
				if(i==0 && S[i]>'1') {
					string z="";
					z.PB(S[i]-1);
					FOR(j,i+1,len-1) z.PB('9');
					ans.PB( MP(size(z),z) );
				}else if(i > 0) {
					if(S[i] > S[i-1]) {
						string z = "";
						REP(j,len) {
							if(j<i) z.PB(S[j]);
							else if(j==i) z.PB(S[j]-1);
							else z.PB('9');
						}
						ans.PB( MP(size(z),z) );
					}else {
						break;
					}
				}
			}

			string z="";
			REP(i,len-1) z.PB('9');
			ans.PB( MP(size(z),z) );

			sort(ALL(ans));
			//FOREACH(it,ans) DEBUGx(it->ND);
			//printf("%I64d ",brutal(N));
			puts(ans.back().ND.c_str());
		}
	}
	return 0;
}
