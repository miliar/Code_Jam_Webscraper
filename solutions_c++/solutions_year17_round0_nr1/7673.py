#include <bits/stdc++.h>
typedef long long ll;

using namespace std;

int main()
{
    ios::sync_with_stdio(false);

    int T , k , ans;
    bool flag;
    string s;
    cin>>T;
    for(int t = 1 ; t <= T ; t++){
        flag = 0;
        cin>>s>>k;
        ans = 0;
        for(int i = 0 ; i<(int)s.length() ; i++){
            if (s[i] == '-'){
                ans ++;
                int j;
                for(j = i ; j<(int)s.length() && j-i < k; j++){
                    if (s[j] == '-')
                        s[j] = '+';
                    else
                        s[j] = '-';
                }
                if (j-i < k){
                    flag = 1;
                    break;
                }
            }
        }
        cout<<"Case #"<<t<<": ";
        if (flag)
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<ans<<endl;
    }


    return 0;
}
