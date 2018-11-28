#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        int num, k;
        cin >> num >> k;
        int n = num;
        int bitS = 1;
        int tmp = k;
        while(tmp>>=1) bitS++;
        bitS--;
        int nnn = 1<<bitS;
        while(bitS) {
            n = (n-1)>>1;
            bitS--;
        }
        //cout << n << " | ";
        //cout << k << ' ' << num << ' ' << n << ' ' << nnn << " " << (k-num+(n*nnn)) << " | ";
        int use = (k-num+(n*nnn))<=0?n+1:n;
        //cout << use << " | ";
        if(use&1) cout << ((use-1)>>1) << " " << ((use-1)>>1) << endl;
        else cout << (use>>1) << " " << ((use-1)>>1) << endl;
    }
    return 0;
}
