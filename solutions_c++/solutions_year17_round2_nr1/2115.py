#include<bits/stdc++.h>
#define __SUBMIT__ ios_base::sync_with_stdio(0); \
                   cin.tie(0);
#define pb push_back
#define mp make_pair
#define fi first
#define se second

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

const int MOD = 1e9 + 7;
const int NMAX = 1e3;

int main()
{
    __SUBMIT__
    int TC; cin >> TC;
    for (int tc = 1; tc <= TC; tc++) {
    	int N;
    	double D;
    	cin >> D >> N;

    	double t = -1.0;
    	for (int i = 0; i < N; i++) {
    		double pos, speed;
    		cin >> pos >> speed;
    		t = max(t, (D-pos)/speed);
    	}
    	double ans = D/t;
    	cout << "Case #" << tc << ": ";
    	cout << fixed << setprecision(10) << ans << "\n";
    }
}