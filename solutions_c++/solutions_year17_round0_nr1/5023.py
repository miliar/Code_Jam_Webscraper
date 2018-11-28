#include <bits/stdc++.h>

using namespace std;

vector<bool> ve;
int cs(0),k,n;

void calc(){
    int ret(0);
    int flip(0);
    int sub[1010];
    memset(sub,0,sizeof sub);
    for(int i=0;i<=n-k;++i){
        flip -= sub[i];
        if(flip&1)ve[i] = !ve[i];
        if(!ve[i]){
            ++flip;
            ++ret;
            ++sub[i+k];
        }
    }
    for(int i=n-k+1;i<n;++i){
        flip -= sub[i];
        if(flip&1)ve[i] = !ve[i];
        if(!ve[i]){
            cout<<"IMPOSSIBLE";
            return ;
        }
    }
    cout<<ret;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    string s;
    while(t--){
        ++cs;
        cin>>s>>k;
        n = s.size();
        ve.resize(s.size());
        for(int i=0;i<n;++i){
            if(s[i]=='+')ve[i] = 1;
            else ve[i] = 0;
        }
        cout<<"Case #"<<cs<<": ";
        calc();
        cout<<"\n";
    }
    return 0;
}
