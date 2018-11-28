#pragma GCC optimize("O3")
#include <vector>
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define iter(i, a, b) for(void *i = a; i != b; i++)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
#define scanf nope
#define endl '\n'
#define INF 1 << 30
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;

pair<ll, ll> mindmaxd(vector<bool> &stalls, ll mid_i) {

        ll top_i = mid_i + 1; 
        while(!stalls[top_i]) //&& top_i != stalls.size() - 1)
                 top_i++;
        
        ll low_i = mid_i - 1;
        while(!stalls[low_i]) //&& low_i != 1)
                 low_i--;

        ll mind = min(top_i - mid_i, mid_i - low_i) - 1, maxd = max(top_i-mid_i, mid_i-low_i) - 1;
        
        return {mind, maxd};
}



int main() {
	cin.sync_with_stdio(0);
	
	ll tc, tcc;

	cin >> tc;
	tcc = tc;
	while (tc--) {
		ll N, K;

		cin >> N >> K;

		vector<bool> stalls(N+2);

		stalls[0] = true;
		stalls[N+1] = true;
		pair<ll, ll> positional_value;
		ll position;
		for (int i = 0; i < K; i++) {
			positional_value = {0ll, 0ll};
 	             	position = 0; 
		      	pair<ll, ll> pv = {0ll, 0ll};	
			for (int j = 1; j < N+1; j++) {
				if (!stalls[j]) {
					pv = mindmaxd(stalls, j);
				}

				if (pv > positional_value) {
					positional_value = pv;
					position = j;
				}
								
			}

			stalls[position] = true;
		}

		cout << "Case #" << tcc - tc << ": " << positional_value.second << " " << positional_value.first << endl;
	}
		
	return 0;
}
