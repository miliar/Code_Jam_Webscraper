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
	int t, n, r, o, y, g, b, v, k = 1, cont = 0;
	cin >> t;
	while(t--)
	{
		cont = 0;
		vector<pair<int, char > > a;
		cin >> n >> r >> o >> y >> g >> b >> v;
		printf("Case #%d: ", k++);
		int aux = max(r, max(y, b));
		if(aux > n-aux) puts("IMPOSSIBLE");
		else
		{
			//y
			if(y){ a.pb(mp(y, 'Y')); cont++;} 
			if(b){ a.pb(mp(b, 'B')); cont++;}
			if(r){ a.pb(mp(r, 'R')); cont++;}
			//cout << "r:" << r << "y:" << y << "b:" << b<< endl;
			char ant = ' ', p = 'f';	
			int conta = 0;
			for (int i = 0; i < n; i++)
			{
				sort(a.begin(), a.end(), greater<pair<int, char> > ());
				for (int j = 0; j < cont; j++)
				{
					
					if(p != 'f' && p != ant && conta > 0)
					{
						if(a[0].second == p) a[0].first--;
						else if(a[1].second == p) a[1].first--;
						else if(a[2].second == p) a[2].first--;
						conta--;
						ant = p;
						cout << p;
					}
					if(a[j].second != ant && a[j].first != 0)
					{
						if(p == 'f'){ p = a[j].second; conta = a[j].first - 1;}
						cout << a[j].second;
						a[j].first--;
						ant = a[j].second;
						break;
					}
					
					
				}
				
				
			}
			printf("\n");
			
		
		}
			
		
		
	}


return 0;
}
