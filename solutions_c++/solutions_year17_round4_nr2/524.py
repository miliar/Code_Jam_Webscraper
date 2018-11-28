#include<algorithm>
#include<cmath>
#include<iomanip>
#include<iostream>
#include<map>
#include<numeric>
#include<queue>
#include<set>
#include<sstream>
#include<vector>
using namespace std;
using uint = unsigned int;
using ll = long long;
const int M = 1e9 + 7;
const ll MLL = 1e18L + 9;
#pragma unused(M)
#pragma unused(MLL)
#ifdef LOCAL
#include"rprint.hpp"
#else
template <class... T> void printl(T&&...){ }
template <class... T> void printc(T&&...){ }
template <class... T> void prints(T&&...){ }
template <class... T> void printd(T&&...){ }
template <class... T> void printArr(T&&...){ }
#endif

int main(){
    int t; cin >> t;
    for(int i = 1; i <= t; i++){
        cout << "Case #" << i << ": ";
        int n, c, m;
        cin >> n >> c >> m;
        vector<vector<int>> v(c, vector<int> (n));
        vector<int> cs(n);
        for(int i = 0; i < m; i++){
            int p, b;
            cin >> p >> b;
            p--; b--;
            v[b][p]++;
            cs[p]++;
        }
        // prints(v);
        int ans = 0, prom = 0;
        for(int i = 0; i < c; i++){
            int acc = accumulate(v[i].begin(), v[i].end(), 0);
            ans = max(ans, acc);
        }
        for(int i = ans; i <= 1000; i++){
            int cnt = 0;
            prom = 0;
            for(int j = n - 1; j >= 0; j--){
                if(cs[j] > i){
                    cnt += cs[j] - i;
                }else if(cs[j] < i){
                    int room = i - cs[j];
                    prom += min(cnt, room);
                    cnt -= min(cnt, room);
                }
            }
            if(!cnt){
                ans = i;
                break;
            }
        }
        cout << ans << ' ' << prom << '\n';
    }
    return 0;
}

