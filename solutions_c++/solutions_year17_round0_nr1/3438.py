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
#endif

int main(){
    int t; cin >> t;
    for(int i=1;i<=t;i++){
        string s;
        int k;
        cin >> s >> k;
        int idx = 0, cnt = 0;
        cout << "Case #" << i << ": ";
        while(1){
            // prints(s);
            while(idx < s.size() && s[idx] == '+'){ idx++; }
            if(idx == s.size()){
                cout << cnt << '\n';
                break;
            }else if(idx + k - 1 >= s.size()){
                cout << "IMPOSSIBLE" << '\n';
                break;
            }
            for(int j=0;j<k;j++){
                s[idx + j] = s[idx + j] == '+' ? '-' : '+';
            }
            cnt++;
        }
    }
    return 0;
}
