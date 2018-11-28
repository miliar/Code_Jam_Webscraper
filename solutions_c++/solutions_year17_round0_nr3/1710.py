#include <vector>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <list>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cassert>
#include <ctime>
#include <cctype>
#include <cstring>
#include <bitset>
#include <algorithm>
#include <iomanip>

#define ld long double
#define ll long long
#define ull unsigned long long
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define y0 _y0
#define y1 _y1

using namespace std;

template < typename T > T abs(T x)
{
    return x > 0 ? x : -x;
}

template < typename T > T sqr(T x)
{
    return x * x;
}

void inst(vector < pair <ll, ll> > &v, pair <ll, ll> item) {
	for (int i = 0; i < v.size(); i++) {
		if (v[i].fst == item.fst) {
			v[i].snd += item.snd;
			return;
		}
	}
	
	v.pb(item);
	return;
}

int main()
{
	freopen("input3.txt", "r", stdin);
	freopen("output3.txt", "w", stdout);
	
	int t;
	
	cin >> t;
	
	int initt = t;
	
	while (t--) {
		ll n, k;
		
		cin >> n >> k;
		
		vector < pair <ll, ll> > cur;
		
		cur.pb(mp(n, 1));
		
		ll ans = 0;
		
		vector < pair <ll, ll> > nxt;
		
		while (true) {
			
			nxt.clear();
			
			for (int i = cur.size() - 1; i >= 0; i--) {
				if (k <= cur[i].snd) {
					ans = cur[i].fst;
					break;
				} 
				else {
					k -= cur[i].snd;
				}
				if (cur[i].fst % 2 == 0) {
					inst(nxt, mp(cur[i].fst / 2, cur[i].snd));
					inst(nxt, mp(cur[i].fst / 2 - 1, cur[i].snd));
				}
				else {
					inst(nxt, mp(cur[i].fst / 2, 2LL * cur[i].snd));
				}
			}
			if (ans > 0) break;
			
			sort(nxt.begin(), nxt.end());
			
			cur.clear();
			for (int i = 0; i < nxt.size(); i++)
				cur.pb(nxt[i]);
		}
		
		cout << "Case #" << initt - t << ": ";
		if (ans & 1) {
			cout << ans / 2LL << " " << ans / 2LL;
		}
		else {
			cout << ans / 2LL << " " << ans / 2LL - 1LL;
		}
		cout << "\n"; 
	}	
    return 0;   
}

