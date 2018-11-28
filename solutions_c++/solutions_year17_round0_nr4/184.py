#include <bits/stdc++.h>
using namespace std;
const int MAX = 1e3 + 10;
typedef long long i64;


// Kuhn matching algorithm O(N*M) much better in practice
int matchL[ MAX ] , matchR[ MAX ];
bool seen[ MAX ];
vector< int > ady[ MAX ];
bool bpm( int left ){
    if( seen[ left ] ) return 0;
    seen[ left ] = 1;
    int right;
    for(int i = 0 ; i < (int)ady[ left ].size() ; ++i ){
        right = ady[ left ][ i ];
        if( matchR[ right ] == -1 || bpm( matchR[ right ] ) ){
            matchR[ right ] = left;
            matchL[ left ] = right;
            return 1;
        }
    }
    return 0;
}
int kuhn(int L){// from 0 to L-1 are the nodes in the left component
    bool change = true;
    memset( matchR , -1 , sizeof( matchR ) );
    memset( matchL , -1 , sizeof( matchL ) );
    while( change ){
        change = false;
        memset( seen , 0 , sizeof( seen ) );
        for(int i = 0; i < L ; ++i ){
            if( matchL[ i ] == -1) change |= bpm( i );
        }
    }
    int ret = 0;
    for( int i = 0 ; i < L ; ++i )
        if( matchL[ i ] != -1 ) ret++;
    return ret;
}




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
    	int n, m; cin >> n >> m;
    	vector<vector<int>> mat(n, vector<int>(n));
    	for(int i = 0; i < m; i++){
    		char ar[3]; int r, c;
    		cin >> ar >> r >> c;r--; c--;
    		if(ar[0] == 'o')mat[r][c] = 3;
    		else if(ar[0] == '+')mat[r][c] = 1;
    		else mat[r][c] = 2;
    	}
    	vector<vector<int>> sol = mat;
    	// solving for rows, cols
    	for(int i = 0; i < 2 * n; i++)ady[i].clear();
    	vector<bool> markedl(2 * n, false), markedr(2 * n, false);
    	for(int i = 0; i  < n; i++)
    		for(int j = 0; j < n; j++){
    			if(mat[i][j] & 1){
    				markedl[i + j] = true;
    				markedr[i - j + n - 1] = true;
    			}
    		}
    	for(int i = 0; i  < n; i++)
			for(int j = 0; j < n; j++){
				if((mat[i][j] & 1) == 0 && !markedl[i + j] && !markedr[i - j + n - 1]){
					ady[i + j].push_back(i - j + n - 1);
				}
			}

    	kuhn(2 * n);
    	for(int t = 0; t < 2 * n; t++){
    		if(matchL[t] != -1){
    			assert((t + matchL[t] - (n - 1)) % 2 == 0);
    			int i = (t + matchL[t] - (n - 1)) / 2;
    			int j = (t - matchL[t] + (n - 1)) / 2;
    			sol[i][j] |= 1;
    		}
    	}

    	for(int i = 0; i < n; i++)ady[i].clear();
		vector<bool> mrl(n, false), mrr(n, false);
		for(int i = 0; i  < n; i++)
			for(int j = 0; j < n; j++){
				if(mat[i][j] & 2){
					mrl[i] = true;
					mrr[j] = true;
				}
			}
		for(int i = 0; i  < n; i++)
			for(int j = 0; j < n; j++){
				if((mat[i][j] & 2) == 0 && !mrl[i] && !mrr[j]){
					ady[i].push_back(j);
				}
			}
		kuhn(n);
		for(int t = 0; t < n; t++){
			if(matchL[t] != -1){

				int i = t;
				int j = matchL[t];
				sol[i][j] |= 2;
			}
		}

		vector<pair<char, pair<int, int>>> ans;
		int price = 0;
		int prices[4] = {0, 1, 1, 2};
		char chars[5] = ".+xo";
		for(int i= 0; i < n ;i++)
			for(int j = 0; j< n; j++){
				price += prices[sol[i][j]];
				if(sol[i][j] == mat[i][j])
					continue;
				ans.push_back({chars[sol[i][j] ], {i + 1, j + 1}});
			}

		cout << price << " " << ans.size() << endl;
		for(auto pp: ans){
			cout << pp.first << " " << pp.second.first << " " << pp.second.second << endl;
		}



    }


}

