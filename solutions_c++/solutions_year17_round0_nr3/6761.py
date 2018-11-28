#include <bits/stdc++.h>
 
#define gc getchar
#define ii(x) scanf(" %d", &x)
#define ill(x) scanf(" %lld", &x)
#define ll long long
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define all(x) x.begin(),x.end()
#define fill(a,b) memset(a, b, sizeof(a))
#define rep(i,a,b) for(i=a;i<b;i++)
#define per(i,a,b) for(i=a;i>=b;i--)
#define pii pair<int, int>
 
using namespace std;
 
void in(int &x){
    register int c=gc();
    x=0;
    for(;(c<48||c>57);c=gc());
    for(;c>47&&c<58;c=gc()){x=(x<<1)+(x<<3)+c-48;}
}

int main()
{
	ll t, n, k, i, j, tt;
	cin >> t; rep(tt, 1, t + 1){
		cin >> n >> k;
		std::set<ll> ss;
		ss.insert(0); ss.insert(n + 1);
		ll best = 0, pos = -1, cur;
		rep(i, 1, k + 1){
			best = -1, pos = -1, cur = -1;
			rep(j, 1, n + 1) if(ss.find(j) == ss.end()){
				auto it1 = ss.upper_bound(j), it2 = it1;
				it1--;
				if(min(j - (*it1), (*it2) - j) > best){
					best = cur = min(j - (*it1), (*it2) - j);
					pos = j;
				}else if(min(j - (*it1), (*it2) - j) == best){
					if(max(j - (*it1), (*it2) - j) > cur){
						cur = max(j - (*it1), (*it2) - j);
						pos = j;
					}
				}
			}
			ss.insert(pos);
		}
		auto it1 = ss.lower_bound(pos), it2 = it1;
		it1--, it2++;
		ll val1 = *it1, val2 = *it2;
		cout << "Case #" << tt <<  ": " << max(pos - val1, val2 - pos) - 1 << " " << min(pos - val1, val2 - pos) - 1 << endl;
	}

	return 0;
}