#include <bits/stdc++.h>
using namespace std;
const int MAX = 1e3 + 10;
typedef long long i64;
int main() {
    #ifdef LOCAL_DEBUG
        freopen("data.in", "r", stdin);
        freopen("data.out", "w", stdout);
    #endif

    cin.tie();
    ios_base::sync_with_stdio(0);
	#define endl '\n'
    int T; cin >> T;
    for(int tt = 1; tt <= T; tt++){
    	cout << "Case #" << tt << ": ";
    	i64 N, K; cin >> N >> K;
    	set<i64> S;
    	map<i64, i64> M;
    	S.insert(N);
    	M[N] = 1;
    	i64 mx = -1, mn;
    	while(K > 0){
    		auto ff = *S.rbegin();
    		S.erase(ff);
    		auto cur = M[ff];
    		//M[ff] = 0;
    		if(cur >= K){
    			mx = ff/ 2, mn = (ff-1)/ 2;
    			K = 0;
    		}else{
    			K -= cur;
    			if((ff - 1) / 2 > 0){
    				S.insert((ff-1)/ 2);
    				M[(ff-1)/ 2] += cur;
    			}
    			if(ff /2 > 0){
    				S.insert(ff/ 2);
    				M[ff/ 2] += cur;
    			}
    		}
    	}
    	assert(mx != -1);
    	cout << mx << " " << mn << endl;
    }


}

