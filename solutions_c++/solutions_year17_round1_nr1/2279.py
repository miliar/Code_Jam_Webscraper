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
		int r, c;
		string s[25];
		cin >> r >> c;
		inc(i, r) { cin >> s[i]; }
		
		bool used[256];
		inc(i, 256) { used[i] = false; }
		
		inc(i, r) {
		inc(j, c) {
			if(s[i][j] != '?' && ! used[ s[i][j] ]) {
				used[ s[i][j] ] = true;
				
				int is = i, ie = i;
				int js = j, je = j;
				while(0 <= js - 1 && s[i][js - 1] == '?') { js--; }
				while(0 <= is - 1 && s[is - 1][j] == '?') { is--; }
				
				bool flag;
				while(je + 1 < c) {
					flag = true;
					incII(ii, is, ie) { flag &= (s[ii][je + 1] == '?'); }
					if(flag) { je++; } else { break; }
				}
				while(ie + 1 < r) {
					flag = true;
					incII(jj, js, je) { flag &= (s[ie + 1][jj] == '?'); }
					if(flag) { ie++; } else { break; }
				}
				
				incII(ii, is, ie) {
				incII(jj, js, je) {
					assert((ii == i && jj == j) || s[ii][jj] == '?');
					s[ii][jj] = s[i][j];
				}
				}
				
				// inc(ii, r) { cout << "test  " << s[ii] << "\n"; } cout << endl;
			}
		}
		}
		
		inc(ii, r) {
		inc(jj, c) {
			assert(s[ii][jj] != '?');
		}
		}
		
		cout << "Case #" << q << ":\n";
		inc(i, r) { cout << s[i] << "\n"; }
	}
	
	return 0;
}
