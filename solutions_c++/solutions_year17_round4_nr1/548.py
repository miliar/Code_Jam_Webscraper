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
        int n, p;
        cin >> n >> p;
        vector<int> gs(n);
        for(int i = 0; i < n; i++){
            cin >> gs[i];
        }
        if(p == 2){
            vector<int> ms(2);
            for(int i : gs){
                ms[i % 2]++;
            }
            cout << ms[0] + (ms[1] + 1) / 2 << '\n';
        }else if(p == 3){
            vector<int> ms(3);
            for(int i : gs){
                ms[i % 3]++;
            }
            cout << ms[0] + min(ms[1], ms[2]) + (max(ms[1], ms[2]) - min(ms[1], ms[2]) + 2) / 3 << '\n';
        }else{
            vector<int> ms(4);
            for(int i : gs){
                ms[i % 4]++;
            }
            int ans = ms[0] + ms[2] / 2 + min(ms[1], ms[3]);
            int rem = max(ms[1], ms[3]) - min(ms[1], ms[3]) + (ms[2] % 2) * 2;
            ans += (rem + 3) / 4;
            cout << ans << '\n';
        }
    }
    return 0;
}
