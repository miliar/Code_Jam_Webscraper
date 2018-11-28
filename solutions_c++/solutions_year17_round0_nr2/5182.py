#include <bits/stdc++.h>
#define X first
#define Y second
#define ll long long
#define INF 1000000007ll
#define rep(i, x, n) for (int i = x; i < n; i++)
#define rev(A) reverse((A).begin(), (A).end())
#define sorv(A) sort((A).begin(), (A).end())
#define pb push_back
#define db(...) ZZ(#__VA_ARGS__, __VA_ARGS__)
#define dbv(v) cout << "Printing "#v << " --> \n"; for(int i=0;i<v.size();i++) cout << v[i] << " "; cout << "\n";
#define dbst(st) cout << "Printing "#st << " --> \n"; for(auto i=st.begin();i!=st.end();i++) cout << *i << " "; cout << "\n";
#define dbmp(mp) cout << "Printing "#mp << " --> \n"; for(auto i=mp.begin();i!=mp.end();i++) cout << #mp"[" << i->first << "]"<< " = " << i->second << "\n";
template <typename Arg1>void ZZ(const char* name, Arg1&& arg1){std::cout << name << " = " << arg1 << std::endl;}
template <typename Arg1, typename... Args>void ZZ(const char* names, Arg1&& arg1, Args&&... args)
{
    const char* comma = strchr(names + 1, ',');
    std::cout.write(names, comma - names) << " = " << arg1;
    ZZ(comma, args...);
}
using namespace std;

ll t;
string s;


int main()
{
	ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
	cin >> t;
	for (ll i = 0; i < t; i++)
	{
		cin >> s;
		for (ll k = 0; k < s.length(); k++)
		{
			for (ll j = 1; j < s.length(); j++)
			{
				if (s[j] < s[j - 1])
				{
					ll m = j - 1 ;
					while (m >= 0 && s[m] == '0')
					{
						s[m] = s[m] - 1;
						m--;
					}
					if (m >= 0)
					{
						s[m]--;
						// remember leading 0's
					}
					for (ll m = j; m < s.length(); m++)
					{
						s[m] = '9';
					}
				}
			}
		}
		string ans;
		for (ll j = 0; j < s.length(); j++)
		{
			if (s[j] != '0')
			{
				ans += s[j];
			}
		}
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
	return 0;
}
