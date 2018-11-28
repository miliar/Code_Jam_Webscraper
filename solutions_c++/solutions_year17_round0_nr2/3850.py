/*************************************************************************
	> File Name: main.cpp
	> Author: cxlove
	> Mail: cxlove321@gmail.com
	> Created Time: 六  4/ 8 20:01:09 2017
 ************************************************************************/

#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
LL n;
int bit[30], a[30], k;
int main () {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, cas = 0;
    cin >> t;
    while (t --) {
        cin >> n;
        k = 0;
        LL ans = 1;
        while(n) {
            bit[k ++] = n % 10;
            n /= 10;
        }
        for(int i = -1 ; i < k ; i ++) {
            for(int j = 0 ; j < k ; j ++) {
                a[j] = bit[j];
            }
            if(i != -1) {
                a[i] --;
                for(int j = 0 ; j < i ; j ++) {
                    a[j] = 9;
                }
            }
            int flag = 1;
            for(int j = 1 ; j < k ; j ++) {
                if(a[j] > a[j - 1]) {
                    flag = 0;
                } 
            }
            if(flag) {
                LL ret = 0;
                for(int j = k - 1 ; j >= 0 ; j --) {
                    ret = ret * 10 + a[j];
                }
                ans = max(ans , ret);
            }
        }
        cout << "Case #" << ++ cas << ": " << ans << endl;
    }

    return 0;
}

