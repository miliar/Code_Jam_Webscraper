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
        cout << "Case #" << i << ": ";
        ll n, k;
        cin >> n >> k;
        priority_queue<ll> q;
        q.push(n);
        ll maxi = 0, mini = 0;
        for(int j=0;j<k;j++){
            ll num = q.top(); q.pop();
            num--;
            q.push(num / 2);
            q.push(num - num / 2);
            maxi = max(num / 2, num - num / 2);
            mini = min(num / 2, num - num / 2);
        }
        cout << maxi << ' ' << mini << '\n';
    }
    return 0;
}

