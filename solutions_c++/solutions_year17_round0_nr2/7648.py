#include <bits/stdc++.h>
using namespace std;
int main(){
    int t, prev, curr;
    unsigned long long n, i, j, ans;
    cin >> t;
    for (int k=1; k<=t; ++k){
        cin >> n;
        for (i=n; i>=0; --i){
            j = i;
            bool flag = true;
            curr = j%10;
            j /= 10;
            while (j > 0){
                prev = curr;
                curr = j % 10;
                j /= 10;
                if (prev < curr){
                    flag = false;
                    break;
                }
            }
            if (flag){
                ans = i;
                break;
            }
        }
        cout << "Case #" << k << ": " << ans << "\n";
    }
    return 0;
}
