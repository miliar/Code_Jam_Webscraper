#include <bits/stdc++.h>

using namespace std;

int t, k;
string s;

void Swap(char &c){
    if(c=='-') c = '+';
    else c = '-';
}

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0);
    //freopen("input.txt", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    cin>>t;
    for(int tt = 1; tt <= t; tt++){
        cin>>s>>k;
        int len = s.length();
        s = "#"+s;
        int res = 0;
        bool ok = false;
        for(int i = 1; i <= len; i++){
            if(s[i]=='-'){
                if(i+k-1>len){
                    ok = true;
                    break;
                }
                for(int j = i; j <= i+k-1; j++) Swap(s[j]);
                res++;
            }
        }
        if(ok) cout<<"Case #"<<tt<<": "<<"IMPOSSIBLE"<<endl;
        else cout<<"Case #"<<tt<<": "<<res<<endl;
    }
    return 0;
}
