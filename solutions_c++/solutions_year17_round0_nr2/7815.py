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
	int t, k = 1;
	cin >> t;
	string s1;
	while(t--)
	{
		cin >> s1;
		int i = 0;
		printf("Case #%d: ", k++);
		while(i < (int)s1.size() - 1)
		{
			if(s1[i] > s1[i+1])
			{
				s1[i]--;
				for (int j = i+1; j < (int)s1.size(); j++)
					s1[j] = '9';
				i = 0;
			}else i++;
		}
		int j = 0;
		for (int i = 0; i < (int)s1.size(); i++)
		{
			if(s1[i] != '0')break;
			else j++;
		}
		for (int i = j; i < (int)s1.size() ; i++)
			cout << s1[i];
		cout << endl;
		
		
	}
	return 0;
 
}
