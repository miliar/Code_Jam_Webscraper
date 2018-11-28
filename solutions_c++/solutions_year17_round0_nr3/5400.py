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

ll t, n, m, last_guy;

vector<ll> ar;

void solve(ll l, ll r)
{
	if (m <= 0 || l < 1 || r > n)
	{
		return;
	}
	ll mid = (l + r) / 2;
	ar[mid] = 1;
	last_guy = mid;
	ll ls = mid - l;
	ll rs = r - mid;
	m--;
	priority_queue<pair<ll, pair<ll, ll> > > pq;
	pq.push({ls, {l, mid - 1}});
	pq.push({rs, {mid + 1, r}});
	while (!pq.empty() && m > 0)
	{
		pair<ll, pair<ll, ll> > tp = pq.top();
		pq.pop();
		ll len = tp.X;
		l = tp.Y.X;
		r = tp.Y.Y;
		mid = (l + r) / 2;
		ar[mid] = 1;
		last_guy = mid;
		ls = mid - l;
		rs = r - mid;
		m--;
		pq.push({mid - 1 - l, {l, mid - 1}});
		pq.push({r - mid - 1, {mid + 1, r}});
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
	cin >> t;
	for (ll i = 0; i < t; i++)
	{
		cin >> n >> m;
		ar.assign(n + 2, 0);
		ar[0] = ar[n + 1] = 1;
		solve(1, n);
		ll ls = 0;
		ll rs = 0;
		for (ll j = last_guy + 1; j < n + 2; j++)
		{
			if (ar[j] != 1)
			{
				rs++;
			}
			else
			{
				break;
			}
		}
		for (ll j = last_guy - 1; j >= 0; j--)
		{
			if (ar[j] != 1)
			{
				ls++;
			}
			else
			{
				break;
			}
		}
		ll ans1 = max(ls, rs);
		ll ans2 = min(ls, rs);
		printf("Case #%lld: %lld %lld\n", i + 1, ans1, ans2);
	}
	return 0;
}
