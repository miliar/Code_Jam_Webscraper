#pragma comment(linker, "/STACK:36777216")

#include <bits/stdc++.h>
#include <pthread.h>
#include <ext/rope>

#define L(a) (int)((a).size())
#define sqr(x) ((x) * 1ll * (x))
#define vi vector<int>
#define mp make_pair
#define pub push_back
#define pob pop_back
#define ii pair<int, int>
#define vii vector <ii>
#define all(s) (s).begin(),(s).end()
#define fore(i, l ,r) for(int i = (int)l; i < (int)r; i++)
#define TRACE(x) cerr << #x << " : " << x << endl
#define _ << " - " << 

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;


const ld EPS = 1e-9;
const ld PI = acos((ld)-1);
const int MOD = (int)1e9 + 7;
const int INF32 = (int)1e9;
const int INF64 = (ll)1e19;

using namespace std;
using namespace __gnu_cxx;

int main()
{
	int t;
	cin >> t;
	fore(tc, 1, t + 1)
	{
		string s;
		cin >> s;
		for (int i = L(s) - 1; i >= 1; i--)
		{
			if(s[i - 1] > s[i])
			{
				s[i - 1]--;
				fore(j, i, L(s))
					s[j] = '9';
			}
		}
		if(s[0] == '0')
			s = s.substr(1);
		cout << "Case #" << tc << ": " << s << endl;
	}
}