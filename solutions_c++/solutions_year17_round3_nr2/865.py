#include <bits/stdc++.h>

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

#define SLL(n) scanf("%lld",&n);
#define SLL2(n,m) scanf("%lld %lld",&n,&m);
#define SLL3(n,m,o) scanf("%lld %lld %lld",&n,&m,&o);


#define PINT(n) printf("%d",(int)(n));
#define PINT2(n,m) printf("%d %d",(int)(n),(int)(m));
#define PINT3(n,m,l) printf("%d %d %d",(int)(n),(int)(m),(int)(l));
#define PLL(n) printf("%lld",(long long)(n));

#define PINTN(n) printf("%d\n",(int)(n));
#define PINT2N(n,m) printf("%d %d\n",(int)(n),(int)(m));
#define PINT3N(n,m,l) printf("%d %d %d\n",(int)(n),(int)(m),(int)(l));
#define PLLN(n) printf("%lld\n",(long long)(n));


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

#define FILL(a,v) fill(begin(a),end(a), v)
#define FILL0(a) memset(a,0,sizeof(a))
#define FILL1(a) memset(a,-1,sizeof(a))

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> Pi;
typedef pair<ll, ll>   Pll;


const int INF = 0x1f1f1f1f; //522,133,279
const ll INFLL = 0x1f1f1f1f1f1f1f1fLL; //2,242,545,357,980,376,863

#include <stdio.h>
#include <stdlib.h>







int main() {
	int TT;
	cin >> TT;
	rep(T, TT) {
		vector<Pi> ts;
		int Ac, Aj;

		cin >> Ac >> Aj;

		rep(i, Ac) {
			int a, b;
			cin >> a >> b;
			ts.push_back({ a, b });
		}

		rep(i, Aj) {
			int a, b;
			cin >> a >> b;
			ts.push_back({ a, b });
		}


		sort(ts.begin(), ts.end());

		ts.push_back(ts[0]);

		if (Ac <= 1 && Aj <= 1) {
			printf("Case #%d: %d\n", T + 1, 2);


		} else {
			if (ts[1].second - ts[0].first <= 12 * 60) {
				printf("Case #%d: %d\n", T + 1, 2);

			} else if (ts[2].second - ts[1].first + 24 * 60 <= 12 * 60) {
				printf("Case #%d: %d\n", T + 1, 2);
			} else {
				printf("Case #%d: %d\n", T + 1, 4);
			}


			//printf("Case #%d: %d\n", T + 1, ret);
		}


	}
}