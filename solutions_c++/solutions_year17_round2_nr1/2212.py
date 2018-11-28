#include <bits/stdc++.h>

#define vmax 260000
#define INF 10e18
#define oi cout << "wtf" << endl
#define mp make_pair
#define sc(x) scanf("%lld", &x)
#define pb push_back 
#define ff first
#define ss second
#define clean(x, y) for(int i = 0; i < y; i++) x[i] = 0
#define buli(x) __builtin_popcountll(x)

using namespace std;

template<class T> T gcd(T a, T b) { return a ? gcd (b % a, a) : b; }

typedef long long int ll;
typedef double ld;

int dr1[] = {0,1,-1,0};
int dc1[] = {-1,0,0,1};

int dr2[] = {0,1,-1,0,1,-1,-1, 1};
int dc2[] = {-1,0,0,1,1, 1,-1,-1};

int main()
{
	int t, k = 1;
	ld d , n, x, maior = -INF, v;
	cin >> t;
	while(t--)
	{
		cin >> d >> n;
		maior = -INF;
		for (ll i = 0; i < n; i++)
		{
			cin >> x >> v;
			ld aux = d - x;
			aux /= v;
			maior = max(maior, aux);			
		}
		//cout << "maior:" << maior << endl;
		double ans = d / maior;
		printf("Case #%d: %.6lf\n",k++, ans);
		
		
	}


return 0;
}
