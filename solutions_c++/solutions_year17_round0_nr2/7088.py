#include <bits/stdc++.h>
#include <string>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define flp(i, l, n) for(i = (l); i < (n); ++i)
#define rflp(i, n, l) for(i = (n-1);i>= (l);--i)
#define wlp(t) while(t--)
#define nl cout << "\n"
#define out(a) cout << a << "\n"
#define gout(t, a) cout << "Case #" << t << ": " << a << "\n"
#define vi vector<int>
#define vll vector<ll>
#define vvi vector < vector<int> >
#define vvll vector < vector<ll> >
#define vd vector<double>
#define vdd vector< vector<double> > 
#define vs vector<string> 
#define pi pair <int, int>
#define pll pair <ll, ll>
#define pb push_back
#define mp make_pair
#define FF first
#define SS second
#define boost ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)

const ll mod = 1e9+7;

int main(int argc, char const *argv[])
{
	boost;
	int t, temp = 1;
	cin >> t;
	wlp(t)
	{
		string s;
		cin >> s;
		int n = s.length();
		int i = n - 1;
		while(i > 0)
		{
			if(s[i] < s[i-1])
			{
				// if(s[i] == '0')
				// {	
					s[i-1] -= 1;
					int j;
					flp(j, i, n) s[j] = '9';
				// }
				// else
					// s[i-1] = s[i];
			}
			--i;
		}
		i = 0;
		while(s[i] == '0') ++i;
		s = s.substr(i);
		gout(temp++, s);
	}
	return 0;
}