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
		int n, k;
		double u, p[50];
		cin >> n >> k >> u;
		inc(i, n) { cin >> p[i]; }
		
		sort(p, p + n);
		
		double ans;
		if(k == n) {
			int lim = 0;
			double s = 0.0;
			inc(i, n) {
				s += p[i];
				if(i + 1 == n || s + u <= p[i + 1] * (i + 1)) { lim = i; break; }
			}
			
			ans = 1.0;
			inc(i, n) {
				if(i <= lim) {
					ans *= (s + u) / (lim + 1);
				} else {
					ans *= p[i];
				}
			}
			
			cout << "Case #" << q << ": ";
			printf("%.8f\n", ans);
		} else {
			cout << "Case #" << q << ": ";
			printf("I don't know.\n", ans);
		}
	}
	
	return 0;
}
