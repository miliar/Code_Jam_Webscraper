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

void proc(vector<int>& ns){
    bool changed = false;
    for(int i=ns.size()-1;i>=1;i--){
        if(ns[i] > ns[i - 1]){
            ns[i]--;
            for(int j=i-1;j>=0;j--){
                ns[j] = 9;
            }
            changed = true;
        }
    }
    if(changed){
        proc(ns);
    }
}

int main(){
    int t; cin >> t;
    for(int i=1;i<=t;i++){
        cout << "Case #" << i << ": ";
        ll n; cin >> n;
        vector<int> ns;
        while(n){
            ns.push_back(n % 10);
            n /= 10;
        }
        proc(ns);
        for(int i=ns.size()-1;i>=0;i--){
            if(ns[i]){
                cout << ns[i];
            }
        }
        cout << '\n';
    }
    return 0;
}
