#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main(){
    int t,k;
    string st;
    cin>>t;
    for(int tc = 1;tc <= t;tc++){
        cin>>st>>k;
        int ans = 0;
        bool fl = 0;
        for(int i = 0;i < st.length();i++){
            if(st[i] == '-'){
                if(i + k > st.length()){
                    fl = 1;break;
                }
                for(int j = i;j < i+k;j++){
                    if(st[j] == '-')st[j] = '+';
                    else st[j] = '-';
                }
                ans++;
            }
        }
        if(fl)cout<<"Case #"<<tc<<": IMPOSSIBLE\n";
        else cout<<"Case #"<<tc<<": "<<ans<<"\n";
    }
    return 0;
}