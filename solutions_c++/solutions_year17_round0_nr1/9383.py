#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("in.in","r",stdin);
    freopen("in.out","w",stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);
    int t;
    cin>>t;
    for(int z=1;z<=t;z++){
        string s;
        int k;
        cin>>s>>k;
        int cnt=0;
        for(int i=0;i<(int)s.size();i++){
            if(s[i]=='-'){
                if((i+k)>(int)s.size()){
                    cnt=-1;
                    break;
                }
                for(int j=0;j<k;j++){
                    if(s[i+j]=='+')s[i+j]='-';
                    else s[i+j]='+';
                }
                cnt++;
            }
        }
        if(cnt==-1)cout<<"Case #"<<z<<": IMPOSSIBLE\n";
        else cout<<"Case #"<<z<<": "<<cnt<<"\n";
    }
    return 0;
}
