#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

long long digit[20];

long long rep(int d, int sz){
    long long ret = 0ll;
    for (int i = 1; i <= sz; i++){
        ret = ret * 10ll + d;
    }
    return ret;
}

long long ll(int sz){
    long long ret = 0ll;
    for (int i = 1; i <= sz; i++){
        ret = ret * 10ll + digit[i];
    }
    return ret;
}

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    long long N;
    cin >> T;
    for (int t = 1; t <= T; t++){
        cin >> N;
        int sz = (int)log10(N) + 1;
        if(N < rep(1, sz)) cout << "Case #" << t << ": " << rep(9, sz - 1) << endl;
        else {
            for (int i = 1; i <= sz; i++){
                for (int j = 9; j >= 1; j--){
                    for (int k = i; k <= sz; k++){
                        digit[k] = j;
                    }
                    if (ll(sz) <= N) break;
                }
            }
            cout << "Case #" << t << ": " << ll(sz) << endl;
        }
    }
    return 0;
}
