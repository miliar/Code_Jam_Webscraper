#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <list>
#include <stack>
#include <queue>
#include <complex>
#include <ctime>
#include<cstdlib>
#define _USE_MATH_DEFINES
#include <math.h>
#include<cmath>
#include <cstdarg> 
#include <iomanip>

#include<unordered_map>
#include<unordered_set>
//#include <arra.y>

//#define  NDEBUG
#include <assert.h>

using namespace std;

#define dprint(Exp,...) if(Exp){fprintf(stderr, __VA_ARGS__);}
#define printe(...) fprintf(stderr, __VA_ARGS__);
#define PrtExp(_Exp)  cerr<< #_Exp <<" = "<< (_Exp)
#define PrtExpN(_Exp)  cerr<< #_Exp <<" = "<< (_Exp) <<"\n"

#define SINT(n) scanf("%d",&n);
#define SINT2(n,m) scanf("%d %d",&n,&m);
#define SINT3(n,m,o) scanf("%d %d %d",&n,&m,&o);
#define SINT4(n,m,o,p) scanf("%d %d %d %d",&n,&m,&o,&p);
#define SINT5(n,m,o,p,q) scanf("%d %d %d %d %d",&n,&m,&o,&p,&q);
//#define SLL(n) scanf("%I64d",&n);
#define SLL(n) scanf("%lld",&n);
#define SLL2(n,m) scanf("%lld %lld",&n,&m);
#define SLL3(n,m,o) scanf("%lld %lld %lld",&n,&m,&o);
#define SST(s) scanf("%s",s);
#define SCH(c) scanf("%c",&c);

#define GC() getchar();

#define PINT(n) printf("%d",(int)(n));
#define PINT2(n,m) printf("%d %d",(int)(n),(int)(m));
#define PINT3(n,m,l) printf("%d %d %d",(int)(n),(int)(m),(int)(l));
//#define PLL(n) printf("%I64d",(long long)(n));
#define PLL(n) printf("%lld",(long long)(n));
#define PST(s) printf("%s",(s));
#define PCH(s) printf("%c",(s));

#define PINTN(n) printf("%d\n",(int)(n));
#define PINT2N(n,m) printf("%d %d\n",(int)(n),(int)(m));
#define PINT3N(n,m,l) printf("%d %d %d\n",(int)(n),(int)(m),(int)(l));
//#define PLLN(n) printf("%I64d\n",(long long)(n));
#define PLLN(n) printf("%lld\n",(long long)(n));
#define PSTN(s) printf("%s\n",(s));
#define PCHN(s) printf("%c\n",(s));

#define PSP() printf(" ");
#define PN() printf("\n");

#define PC(c) putchar(c);
#define CSP (' ')
#define SN ("\n")

#define rep(i,a) for(int i=0;i<a;i++)
#define reP(i,a) for(int i=0;i<=a;i++)
#define Rep(i,a) for(int i=a-1;i>=0;i--)
#define ReP(i,a) for(int i=a;i>=0;i--)

#define rEp(i,a) for(i=0;i<a;i++)
#define rEP(i,a) for(i=0;i<=a;i++)
#define REp(i,a) for(i=a-1;i>=0;i--)
#define REP(i,a) for(i=a;i>=0;i--)

#define repft(i,a,b) for(int i=a;i<b;i++)
#define repfT(i,a,b) for(int i=a;i<=b;i++)
#define Repft(i,a,b) for(int i=a-1;i>=b;i--)
#define RepfT(i,a,b) for(int i=a;i>=b;i--)

#define foreach(a,it) for(auto it = a.begin(); it != a.end(); ++it)

#define FILL(a,v) fill(begin(a),end(a), v)
#define FILL0(a) memset(a,0,sizeof(a))
#define FILL1(a) memset(a,-1,sizeof(a))

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> Pi;
typedef pair<ll, ll>   Pll;


const int INF = 0x1f1f1f1f;//522,133,279
const ll INFLL = 0x1f1f1f1f1f1f1f1fLL;//2,242,545,357,980,376,863

template <class A, class B> inline ostream& operator<<(ostream& st, const pair<A, B>& P) { return st << "(" << P.first << "," << P.second << ")"; };
template <class A, class B> inline pair<A, B> operator+(const pair<A, B>& P, const pair<A, B>& Q) { return pair<A, B>(P.first + Q.first, P.second + Q.second); };
template <class A, class B> inline pair<A, B> operator-(const pair<A, B>& P, const pair<A, B>& Q) { return pair<A, B>(P.first - Q.first, P.second - Q.second); };

ll bitcount(ll bits) {
	bits = (bits & 0x5555555555555555) + (bits >> 1 & 0x5555555555555555);
	bits = (bits & 0x3333333333333333) + (bits >> 2 & 0x3333333333333333);
	bits = (bits & 0x0f0f0f0f0f0f0f0f) + (bits >> 4 & 0x0f0f0f0f0f0f0f0f);
	bits = (bits & 0x00ff00ff00ff00ff) + (bits >> 8 & 0x00ff00ff00ff00ff);
	bits = (bits & 0x0000ffff0000ffff) + (bits >> 16 & 0x0000ffff0000ffff);
	return (bits & 0x00000000ffffffff) + (bits >> 32 & 0x00000000ffffffff);
}



map<ull, ull> m;
typedef pair<ull, ull>   Pull;


int main() {
	
	int T;

	cin >> T;


	repfT(t, 1, T) {
		ull N;
		ll K;
		cin >> N >> K;

		m.clear();
		m.insert({N,1});

		bool f = true;

		while (!m.empty()) {

			//cerr << m.size();for (auto &x : m) cerr << x;cerr <<K<< endl;

			Pull p = *(--m.end());
			m.erase(p.first);

			K -= p.second;

			//cerr << "K = " << K << endl;
			if (K <= 0) {
				f = false;
				//cerr << "!\n";
				if (p.first % 2 == 0) {
					printf("Case #%d: %lld %lld\n", t, p.first / 2, p.first / 2 - 1);
				} else {
					printf("Case #%d: %lld %lld\n", t, p.first / 2, p.first / 2);
				}
				break;
			}

			if (p.first > 4) {
				if (p.first%2 == 0) {
					m[p.first / 2] += (p.second);
					m[p.first/2-1] += (p.second);

				} else {
					m[p.first / 2] += (p.second*2);
				}
			} else if (p.first == 4) {
				m[2] += (p.second);
			}
		}
		if (f) {
			printf("Case #%d: 0 0\n", t);
		}


	}
}
