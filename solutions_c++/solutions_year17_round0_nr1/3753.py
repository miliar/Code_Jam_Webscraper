#include <bits/stdc++.h>

#define mem(a,b) memset(a,b,sizeof(a))
#define rep(i,a,b) for(int i=a;i<b;i++)
const int INF=0x3f3f3f3f;
const int maxn=1e3+5;
const int mod=9901;
#define pii pair<int,int>
#define mp(a,b) make_pair(a,b)
typedef long long ll;
typedef unsigned int ui;
using namespace std;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("d:\\A-large.in","r",stdin);
    freopen("d:\\out2.txt","w",stdout);
#endif
    int T; cin>>T;
    for(int cs=1;cs<=T;cs++){
        string str; int k;
        cin>>str>>k;
        int ans=0;
        for(int i=0;i<str.length()-k+1;i++){
            if(str[i]=='-'){
                for(int j=i;j<i+k;j++)
                    str[j]=str[j]=='-'? '+':'-';
                ans++;
                //cout<<ans<<" "<<str<<endl;
            }
        }
        printf("Case #%d: ",cs);
        if(str.find('-')!=string::npos){
            puts("IMPOSSIBLE");
        }else printf("%d\n",ans);
    }
    return 0;
}