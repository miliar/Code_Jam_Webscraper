#include <bits/stdc++.h>
using namespace std;
const int MAX = 1e3 + 10;
typedef long long i64;




int S[MAX];
int K[MAX];

int main() {
    #ifdef LOCAL_DEBUG
        freopen("data.in", "r", stdin);
        freopen("data.out", "w", stdout);
    #endif

    cin.tie();
    ios_base::sync_with_stdio(0);
	#define endl '\n'

    int T; cin >> T;
    for(int tt = 0; tt < T; tt++){
    	cout << "Case #" << tt + 1 << ": ";
    	int N, D ; cin >> D >> N;
    	double ans = 1e18;
    	for(int i = 0; i < N ;i++){
    		cin >> K[i] >> S[i];
    		double cur = (double)D * S[i] / (D - K[i]);
    		ans = min(ans, cur);
    	}
    	cout << fixed << setprecision(8) << ans << endl;


    }

}

