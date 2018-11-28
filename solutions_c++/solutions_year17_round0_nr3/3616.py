#include <bits/stdc++.h>
#define rep(i, a, n) for(int i = a; i < n; i++)
#define repb(i, a, b) for(int i = a; i >= b; i--)
#define all(a) a.begin(), a.end()
#define o(a) cout << a << endl
#define int long long
#define fi first
#define se second
using namespace std;
typedef pair<int, int> P;

signed main(){
    int tnum;
	cin >> tnum;
	for(int ti = 1; ti <= tnum; ti++){
        int n, k;
        cin >> n >> k;
        int m, c = 1;
        for(int i = 0;; i++){
            if(c * 2 > k && k >= c){
                m = i; break;
            }
            c *= 2;
        }
        k -= c;
        int bl = (n - (c - 1)) / c;
        int br = n / c;
        int cnt = (n - (c - 1)) % c;
        int a, b;
        if(k < cnt){
            a = br / 2;
            b = (br - 1) / 2;
        }else{
            a = bl / 2;
            b = (bl - 1) / 2;
        }
		cout << "Case #" << ti << ": " << a << " " << b << endl;            
	}
}