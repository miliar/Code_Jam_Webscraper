#include "bits/stdc++.h"
using namespace std;
const int N = 1005;
int n , k;
bool arr[N];
int ls[N];
int rs[N];

int getLs(int idx) {
    --idx;
    int cnt = 0;
    while(idx >= 1 && !arr[idx]) {
        ++cnt;
        --idx;
    }
    return cnt;
}

int getRs(int idx) {
    ++idx;
    int cnt = 0;
    while(idx <= n && !arr[idx]) {
        ++idx;
        ++cnt;
    }
    return cnt;
}

int main() {
    freopen("codejam3.txt" , "r" , stdin);
    freopen("codejamout3.txt" , "w" , stdout);
    int tt;
    cin >> tt;
    for(int qq = 1; qq <= tt; ++qq) {
        cout << "Case #" << qq << ": ";
        cin >> n >> k;
        memset(arr , 0 , sizeof arr);
        for(int i = 1; i <= n; ++i) {
            ls[i] = getLs(i);
            rs[i] = getRs(i);
        }
        for(int i = 1; i < k; ++i) {
            int pt = -1;
            int mn = -1;
            int mx = 0;
            for(int j = 1; j <= n; ++j) {
                if(arr[j]) {
                    continue;
                }
                if(min(ls[j] , rs[j]) > mn) {
                    pt = j;
                    mn = min(ls[j] , rs[j]);
                    mx = max(ls[j] , rs[j]);
                } else if(min(ls[j] , rs[j]) == mn) {
                    if(max(ls[j] , rs[j]) > mx) {
                        pt = j;
                        mx = max(ls[j] , rs[j]);
                    }
                }
            }
            assert(pt != -1);
            arr[pt] = 1;
            for(int i = 1; i <= n; ++i) {
                ls[i] = getLs(i);
                rs[i] = getRs(i);
            }
        }
        int pt = -1;
            int mn = -1;
            int mx = 0;
            for(int j = 1; j <= n; ++j) {
                if(arr[j]) {
                    continue;
                }
                if(min(ls[j] , rs[j]) > mn) {
                    pt = j;
                    mn = min(ls[j] , rs[j]);
                    mx = max(ls[j] , rs[j]);
                } else if(min(ls[j] , rs[j]) == mn) {
                    if(max(ls[j] , rs[j]) > mx) {
                        pt = j;
                        mx = max(ls[j] , rs[j]);
                    }
                }
            }
            cout << mx << " " << mn << endl;
    }
    return 0;
}

