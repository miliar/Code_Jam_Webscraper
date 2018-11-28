#include <cstdio>
#include <iostream>
#include <cstring>
#define db(x) cout<<#x<<"="<<(x)<<" "
#define el cout<<endl
using namespace std;

const int MXN = 1010;
typedef long long ll;

int cas, tcas;

ll N, K;

int A[MXN];

void init()
{
	cin>>N>>K;
}

namespace solve
{	
	void solve()
	{
		ll a, ta, tb;
		a = N; ta = 1;tb = 0;
		for(ll k = 0, t = 0; ; ++k)
		{
			if (t + (1 << k) < K)
			{
				ll lta = ta, ltb = tb;
				if (a & 1)
				{
					ta = lta * 2 + ltb;
					tb = ltb;
				}
				else
				{
					tb = ltb * 2 + lta;
					ta = lta;
				}
				a = (a - 1) / 2;
				t += 1 << k;
			}
			else
			{
				ll res = K - t;
				if (res <= tb)
				{
					cout << (a + 1) / 2 <<" " << (a) / 2 <<endl;
				}
				else
				{
					cout << a / 2 <<" " << (a - 1) / 2 <<endl;
				}
				return;
			}
			//db(a),db(ta),db(tb),el;
		}
	}
}

int main()
{
	//freopen("C-small-2-attempt0.in", "r", stdin);
	//freopen("C-small-2-attempt0.out", "w", stdout);
	scanf("%d", &cas);
	for(tcas = 0; tcas < cas; ++tcas)
	{
		init();
		printf("Case #%d: ", tcas + 1);
		solve::solve();
	}
	return 0;
}
