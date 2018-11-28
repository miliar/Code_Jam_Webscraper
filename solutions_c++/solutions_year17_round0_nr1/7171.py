#include <bits/stdc++.h>
using namespace std;

int t,n,k,ans;
string s;
bool u;

int main(){
    ifstream cin ("pancake.in");
    ofstream cout ("pancake.out");
    cin>>t;
    for (int w=1; w<=t; w++){
        cin>>s; u=true; cin>>k;
        ans=0;
        s='0'+s;
        n=s.length()-1;
        for (int i=1; i<=n-k+1; i++){
            if (s[i]=='-'){
                ans++;
                for (int j=i; j<i+k; j++){
                    if (s[j]=='-') s[j]='+';
                    else s[j]='-';
                }
            }
        }
        for (int i=n-k+2; i<=n; i++){
            if (s[i]=='-') u=false;
        }
        if (!u) cout<<"Case #"<<w<<": IMPOSSIBLE\n";
        else cout<<"Case #"<<w<<": "<<ans<<"\n";
    }
    return 0;
}
