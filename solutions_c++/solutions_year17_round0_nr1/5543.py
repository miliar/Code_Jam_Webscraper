#include <bits/stdc++.h>
using namespace std;

string s;
int t,test,k,tt,ans,i,len,j;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    //freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    cin >> t;
    for(test=1;test<=t;++test){
        cin >> s >> k;
        len = s.size();
        tt = ans = 0;
        for(i=0;i<len;++i)
        if(s[i]=='-'){
            if(i+k-1>=len) {
                tt=1;
                break;
            } else{
            ++ans;
            for(j = i; j <=i+k-1;++j)
                if(s[j]=='-')s[j]='+'; else s[j]='-';
            }
        }
        cout<<"Case #"<<test<<": ";
        if(tt)cout<<"IMPOSSIBLE\n"; else cout<<ans<<'\n';
    }
}
