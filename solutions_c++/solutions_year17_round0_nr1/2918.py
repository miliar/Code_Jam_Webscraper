#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    cin>>t;
    string s;
    int k;
    int n;
    int nr = 0;
    bool flag;
    for(int i=1; i<=t; i++){
        cin>>s;
        cin>>k;
        n = s.size();
        nr = 0;
        for(int j=0; j+k <= n; j++){
            if(s[j] == '-'){
                for(int l = j; l < j+k; l++){
                    if(s[l] == '+')
                        s[l] = '-';
                    else
                        s[l] = '+';
                }
                nr++;
            }
        }
        flag = true;
        for(int j=0; j<n && flag == true; j++){
            if(s[j] == '-')
                flag = false;
        }

        if(flag){
            cout<<"Case #"<<i<<": "<<nr<<'\n';
        } else {
            cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<'\n';
        }
    }
    return 0;
}
