#include <bits/stdc++.h>
const int MAX = 2e5 + 10;
typedef long long i64;
using namespace std;

int person[MAX];
int position[MAX];
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
    	int n, c, m; cin >> n >> c>> m;
    	for(int i = 0; i < n; i++)position[i] = 0;
    	for(int i = 0; i < c; i++)person[i] = 0;
    	for(int i = 0; i < m; i++){
    		int b, p; cin >> p >> b; b--, p--;
    		person[b]++;
    		position[p]++;
    	}
    	//cout << person[0] << endl;
    	int y = -1e9;
    	for(int i = 0; i < c; i++)
    		y = max(y, person[i]);
    	int tot = 0;
    	for(int i = 0; i < n; i++){
    		tot += position[i];
    		int ty = (tot + i ) / (i + 1);
    		y = max(y, ty);
    	}
    	y = max((m + n - 1) / n , y);
    	int z = 0;
    	for(int i = 0; i < n; i++){
    		if(position[i] > y){
    			z += position[i] - y;
    		}
    	}
    	cout << y << " " << z << endl;



    }
}

