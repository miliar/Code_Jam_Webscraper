#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
typedef pair <int, int> pii;
typedef vector<int> vi;

#define mp make_pair
#define pb push_back

#define FOR(i, a, b) for (int i=a; i<b; i++)
#define F0R(i, a) for (int i=0; i<a; i++)
 
#define f first
#define s second
#define lb lower_bound
#define ub upper_bound
#define endl "\n"
 
const int MOD = 1000000007;
double PI = 4*atan(1);

int N,P;
multiset<pii> in[50];
vi need;

int solve() {
    int ans = 0;
    while (1) {
        F0R(i,N) if (in[i].size() == 0) return ans;
        int x = 0;
        F0R(i,N) x = max(x,(*in[i].begin()).f);
        
        bool f = 1;
        F0R(i,N) while (in[i].size() && (*in[i].begin()).s < x) {
            f = 0;
            in[i].erase(in[i].begin());
        }
        if (f) {
            ans++;
            F0R(i,N) in[i].erase(in[i].begin());
        }
    }
}

int main() {
	int T; cin >> T;
	F0R(i,T) {
		cout << "Case #" << (i+1) << ": ";
		cin >> N >> P; need.resize(N);
		F0R(j,N) cin >> need[j];
		F0R(j,N) {
		    in[j].clear();
		    F0R(k,P) {
		        int x; cin >> x;
		        int lo = ceil(double(x)/need[j]/1.1), hi = floor(double(x)/need[j]/0.9);
		        lo = max(lo,1);
		        if (lo <= hi) in[j].insert({lo,hi});
		    }
		}
		cout << solve() << "\n";
	}
}