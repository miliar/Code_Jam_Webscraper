#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define pb push_back
#define mp make_pair

int n, r, o, y, g, b, v;

void solve()
{
    cin >> n >> r >> o >> y >> g >> b >> v;
    string res;
    if(r > y + b || y > r + b || b > r + y){
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    for(int i = 0; i < n; i++){
        if(i == 0){
            if(r >= y && r >= b && r > 0) res.pb('R'), r--;
            else if(y >= r && y >= b && y > 0) res.pb('Y'), y--;
            else if(b >= r && b >= y && b > 0) res.pb('B'), b--;
        }
        else{
            if(res.back() == 'Y'){
                if(r >= b && r > 0){
                    res.pb('R');
                    r--;
                }
                else if(b > 0){
                    res.pb('B');
                    b--;
                }
            }
            else if(res.back() == 'B'){
                if(r >= y && r > 0){
                    res.pb('R');
                    r--;
                }
                else if(y > 0){
                    res.pb('Y');
                    y--;
                }
            }
            else{
                if(y >= b && y > 0){
                    res.pb('Y');
                    y--;
                }
                else if(b > 0){
                    res.pb('B');
                    b--;
                }
            }
        }
    }
    if(res[n - 1] == res[0]){
        swap(res[n - 1], res[n - 2]);
    }
    cout << res << endl;
}

int main()
{
    freopen("B.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test;
    cin >> test;
    for(int i = 1; i <= test; i++){
        cout << "Case #" << i << ": ";
        solve();
    }
}
