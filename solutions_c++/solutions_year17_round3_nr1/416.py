#include <bits/stdc++.h>
using namespace std;

typedef long long   signed int LL;
typedef long long unsigned int LU;

#define incID(i, l, r) for(int i = (l)    ; i <  (r); i++)
#define incII(i, l, r) for(int i = (l)    ; i <= (r); i++)
#define decID(i, l, r) for(int i = (r) - 1; i >= (l); i--)
#define decII(i, l, r) for(int i = (r)    ; i >= (l); i--)
#define  inc(i, n) incID(i, 0, n)
#define inc1(i, n) incII(i, 1, n)
#define  dec(i, n) decID(i, 0, n)
#define dec1(i, n) decII(i, 1, n)

#define inII(v, l, r) ((l) <= (v) && (v) <= (r))
#define inID(v, l, r) ((l) <= (v) && (v) <  (r))

#define PB push_back
#define EB emplace_back
#define MP make_pair
#define FI first
#define SE second
#define UB upper_bound
#define LB lower_bound
#define PQ priority_queue

#define  ALL(v)  v.begin(),  v.end()
#define RALL(v) v.rbegin(), v.rend()
#define  FOR(it, v) for(auto it =  v.begin(); it !=  v.end(); ++it)
#define RFOR(it, v) for(auto it = v.rbegin(); it != v.rend(); ++it)

template<typename T> bool   setmin(T & a, T b) { if(b <  a) { a = b; return true; } else { return false; } }
template<typename T> bool   setmax(T & a, T b) { if(b >  a) { a = b; return true; } else { return false; } }
template<typename T> bool setmineq(T & a, T b) { if(b <= a) { a = b; return true; } else { return false; } }
template<typename T> bool setmaxeq(T & a, T b) { if(b >= a) { a = b; return true; } else { return false; } }
template<typename T> T gcd(T a, T b) { return (b == 0 ? a : gcd(b, a % b)); }
template<typename T> T lcm(T a, T b) { return a / gcd(a, b) * b; }

// ---- ----

int main() {
	int t;
	cin >> t;
	inc1(q, t) {
		LL n, k, r[1000], h[1000];
		cin >> n >> k;
		inc(i, n) { cin >> r[i] >> h[i]; }
		
		k--;
		LL ans = 0;
		inc(i, n) {
			vector<pair<LL, LL>> vec;
			inc(j, n) {
				if(j == i) { continue; }
				vec.EB(r[j] * h[j], r[j]);
			}
			sort(ALL(vec));
			
			LL c = 0, s = r[i] * r[i] + 2 * r[i] * h[i];
			dec(j, vec.size()) {
				if(c == k) { break; }
				if(vec[j].SE <= r[i]) {
					s += vec[j].FI * 2;
					c++;
				}
			}
			
			if(c == k) { setmax(ans, s); }
		}
		
		cout << "Case #" << q << ": ";
		printf("%.8f\n", ans * 3.141592653589);
		//cout << ans << endl;
	}
	
	return 0;
}
