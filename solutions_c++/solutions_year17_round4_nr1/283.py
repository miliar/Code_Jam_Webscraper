#include <bits/stdc++.h>
const int MAX = 1e2 + 10;
typedef long long i64;
using namespace std;

int dp2[MAX][MAX];
int dp3[MAX][MAX][MAX];
int main() {

    #ifdef LOCAL_DEBUG
    freopen ("data.in", "r", stdin );
    freopen ("data.out", "w", stdout );
    #endif
    ios_base::sync_with_stdio(0); cin.tie(0);
    #define endl '\n'

    int T; cin >> T;
    for(int test = 1; test <= T; test++){
    	cout << "Case #" << test << ": ";

    	int n, p; cin >> n >> p;
    	vector<int> g(p);
    	for(int i = 0; i < n; i++){
    		int a; cin >> a;
    		a = a % p;
    		g[a]++;
    	}
    	int ans = g[0];
    	if(p == 2){
    		cout << ans + (g[1] + 1) / 2 << endl;
    	}
    	else if(p == 3){
    		memset(dp2, -1, sizeof(dp2));
    		dp2[0][0] = 0;
    		for(int i1 = 0; i1 <= g[1]; i1++)
    			for(int i2 = 0; i2 <= g[2]; i2++){
    				if(i1 == 0 && i2 == 0){
    					continue;
    				}
    				if(i1 > 0 && dp2[i1 -1][i2] >= 0)dp2[i1][i2] = max(dp2[i1][i2], dp2[i1 -1][i2] + ((i1 - 1 + i2 * 2) % 3 == 0 ));
    				if(i2 > 0 && dp2[i1][i2- 1] >= 0)dp2[i1][i2] = max(dp2[i1][i2], dp2[i1][i2 - 1] + ((i1 + (i2 - 1) * 2) % 3 == 0 ));
    			}
    		cout << ans + dp2[g[1]][g[2]] << endl;
    	}
    	else{
    		memset(dp3, -1, sizeof(dp3));
			dp3[0][0][0] = 0;
			for(int i1 = 0; i1 <= g[1]; i1++)
				for(int i2 = 0; i2 <= g[2]; i2++){
					for(int i3 = 0; i3 <= g[3]; i3++){
						if(i1 == 0 && i2 == 0 && i3 == 0){
												continue;
											}
						if(i1 > 0 && dp3[i1 -1][i2][i3] >= 0)dp3[i1][i2][i3] = max(dp3[i1][i2][i3], dp3[i1 -1][i2][i3] + ((i1 - 1 + (i2) * 2 + (i3) * 3) % 4 == 0 ));
						if(i2 > 0 && dp3[i1][i2 - 1][i3] >= 0)dp3[i1][i2][i3] = max(dp3[i1][i2][i3], dp3[i1][i2 - 1][i3] + ((i1 + (i2 - 1) * 2 + (i3) * 3) % 4 == 0 ));
						if(i3 > 0 && dp3[i1][i2][i3 -1 ] >= 0)dp3[i1][i2][i3] = max(dp3[i1][i2][i3], dp3[i1][i2][i3 - 1] + ((i1 + (i2) * 2 + (i3 - 1) * 3) % 4 == 0 ));

					}
				}
			cout << ans + dp3[g[1]][g[2]][g[3]] << endl;
    	}


    }
}

