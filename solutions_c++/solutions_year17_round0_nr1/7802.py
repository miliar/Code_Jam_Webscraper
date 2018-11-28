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
typedef long double ld;
 
int dr1[] = {0,1,-1,0};
int dc1[] = {-1,0,0,1};
 
int dr2[] = {0,1,-1,0,1,-1,-1, 1};
int dc2[] = {-1,0,0,1,1, 1,-1,-1};

int main()
{
	//freopen("a.in", "r", stdin); 
	//freopen("a.out", "w", stdout);
	
	int t, k, i = 0, m = 1;
	cin >> t;
	getchar();
	string s1;
	while(t--)
	{
		i = 0;
		cin >> s1 >> k;
		getchar();
		int flag = 0, cont = 0;
		printf("Case #%d: ", m++);
		while(i < (int)s1.size())
		{
			//cout << s1 << endl;
			if(s1[i] == '+') i++;
			else
			{
				if(i + k > (int)s1.size())
				{
					flag = 1;
					break;
				}
				for (int j = i; j < k+i; j++)
				{
					if(s1[j] == '-') s1[j] = '+';
					else s1[j] = '-';
					
				}
				i = 0;
				cont++;
			}
			
		}
		if(flag) puts("IMPOSSIBLE");
		else cout << cont << endl;
		
		
		
	}
	
	return 0;
 
}
