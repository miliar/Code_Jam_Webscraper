#include <iostream>
#include <bits/stdc++.h>

using namespace std;

bool notTidy(long long n){
    while(n > 9){
        int x = n%10;
        n /= 10;
        if(x < (n%10) || x == 0)
            return 1;
    }
    return 0;
}
int main()
{
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t, c = 0; cin >> t;
    long long x;
    while(t--){
        cout << "Case #" << ++c << ": ";
        cin >> x;
        string ans = "";
        if(notTidy(x)){
            ans += "9";
            x /= 10;
            x--;

            while(x > 9){
                long long cur = x%10;
                x /= 10;

                if(cur < (x%10) || cur == 0){
                    ans = "9" + ans;
                    x--;
                }

                else{
                    stringstream ss;
                    ss << cur;
                    ans = ss.str() + ans;
                }
            }
            if(x > 0){
                stringstream ss;
                ss << x;
                ans = ss.str() + ans;
            }
            cout << ans << "\n";
        }
        else{
            cout << x << "\n";
        }
//        while(x > 9){
//            int cur = x%10;
//            x /= 10;
//
//            if(cur < (x%10) || cur == 0){
//                int digit = 9;
//                if(ans.size() > 0){
//                    string s = "";
//                    s += ans[0];
//
//                    int tmp = atoi(s.c_str());
//                    while(digit > tmp)
//                        digit--;
//                }
//                stringstream ss;
//                ss << digit;
//                ans = ss.str() + ans;
//
//                x--;
//            }
//            else{
//                stringstream ss;
//                ss << cur;
//
//                ans = ss.str() + ans;
//            }
//        }
//        if(x > 0)
//            cout << x << ans << "\n";
//        else
//            cout << ans << "\n";
    }
    return 0;
}
