#include<bits/stdc++.h>

using namespace std;

#define ll long long
#define s(x) scanf("%lld" , &x)

int main()
{
    ll t , p = 0;
    freopen("in2.txt" , "r" , stdin);
    freopen("out2.txt" , "w" , stdout);
    s(t);
    while(t--){
        p ++;
        string s;
        ll k , i , j , cnt = 0 , f = 0;
        cin >> s;
        cin >> k;
        for(i = 0; i <= s.length()-k; i ++){
            if(s[i] == '-'){
                cnt ++;
                for(j = i; j < i+k; j ++){
                    if(s[j] == '-'){
                        s[j] = '+';
                    }
                    else{
                        s[j] = '-';
                    }
                }
            }
        }
        for(i = 0; i < s.length(); i ++){
            if(s[i] == '-'){
                f = 1;
                cout << "Case #" << p << ": IMPOSSIBLE" << endl;
                break;
            }
        }
        if(f == 0){
          cout << "Case #" << p << ": " << cnt << endl;
        }
    }
    return 0;
}
