#include<bits/stdc++.h>
using namespace std;

#define ff first
#define ss second
#define m_p make_pair
#define pb push_back
#define ppb pop_back
#define pf push_front
#define ppf pop_front
#define ll long long
#define l_b lower_bound
#define u_b upper_bound

char rev(char c)
{
	if (c == '+') return '-';
	return '+';
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("myout.out","w",stdout);
	int ks, kase;
	cin >> kase;
	for (ks = 1; ks <= kase; ks++)
	{
		string s;
		int ans = 0, imp = 0, k;
		cin >> s >> k;

		for (int i = 0; i < s.size(); i++)
		{
			if (s[i] == '-')
			{
				if (s.size() - i <  k )
				{
					imp = 1;
					break;
				}
				ans++;
				for (int j = 0; j < k; j++) s[i + j] = rev(s[i + j]);
			}
		}
		if (!imp) printf("Case #%d: %d\n", ks, ans);
		else printf("Case #%d: IMPOSSIBLE\n", ks);
	}
}