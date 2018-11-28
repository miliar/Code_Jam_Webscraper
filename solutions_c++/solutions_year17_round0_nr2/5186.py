#include<bits/stdc++.h>

using namespace std;

#define ll long long
#define s(x) scanf("%lld" , &x)

int main()
{
    freopen("bl.txt" , "r" , stdin);
    freopen("obl.txt" , "w" , stdout);
    ll t , p = 0;
    s(t);
    while(t--){
        p ++;
        ll i , j , flag;
        string s;
        cin >> s;
        while(1){
            flag = 0;
            for(i = 1; i < s.length(); i ++){
                if(s[i] < s[i-1]){
                    s[i-1] = (char)(s[i-1]-1);
                    for(j = i; j < s.length(); j ++){
                        s[j] = '9';
                    }
                    flag = 1;
                }
            }
            if(flag == 0){
                break;
            }
        }
    cout << "Case #" << p << ": ";
        flag = 1;
        for(i = 0; i < s.length(); i ++){
            if(s[i] != '0'){
                flag = 0;
                cout << s[i];
            }
            else if(s[i] == '0' && flag == 1){

            }
        }
        cout << endl;
    }
    return 0;
}
