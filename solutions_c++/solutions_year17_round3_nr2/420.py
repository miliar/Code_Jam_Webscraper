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
		int ac, aj, l[200], r[200];
		cin >> ac >> aj;
		inc(i, ac + aj) { cin >> l[i] >> r[i]; }
		
		int a[1440];
		inc(i, 1440) { a[i] = 0; }
		inc(i, ac + aj) {
			incID(j, l[i], r[i]) { a[j] = (i < ac ? 1 : 2); }
		}
		
		int sc = 0, sj = 0, sg = 0, ans = 0;
		vector<int> vc, vj;
		int svc = 0, svj = 0;
		
		int base;
		dec(i, 1440) {
			if(a[i] !=0) { base = i; break; }
		}
		int pre = a[base], gap = 0;
		inc1(i, 1440) {
			int p = (base + i) % 1440;
			
			if(a[p] == 0) { gap++; }
			else {
				(a[p] == 1 ? sc : sj) += 1;
				
				if(pre != a[p]) {
					sg += gap;
					ans++;
				} else {
					if(gap != 0) {
						(a[p] == 1 ? vc : vj).PB(gap);
						(a[p] == 1 ? svc : svj) += gap;
					}
				}
				
				gap = 0;
				pre = a[p];
			}
		}
		
		sort(ALL(vc));
		sort(ALL(vj));
		
		dec(i, vc.size()) {
			if(sc + svc <= 720) { break; }
			svc -= vc[i];
			ans += 2;
		}
		dec(i, vj.size()) {
			if(sj + svj <= 720) { break; }
			svj -= vj[i];
			ans += 2;
		}
		
		
		cout << "Case #" << q << ": ";
		cout << ans << endl;
	}
	
	return 0;
}
