#include<bits/stdc++.h>
#define ll long long
#define ld long double
#define fi first
#define se second
using namespace std;
#define sd(x) scanf("%d",&x)
#define pd(x) printf("%d",x)
#define sl(x) scanf("%lld",&x)
#define pl(x) printf("%lld",x)
#define mem(x,a) memset(x,a,sizeof(x))
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define all(v) v.begin(),v.end()
#define N (int)(2e5+50)
vector<int> v;
void solve(){
    string s;
    int k,ans=0;
    cin>>s;
    sd(k);
    v.clear();
    for(int i=0;i<s.size();i++){
        if(s[i]=='+')v.pb(1);
        else v.pb(0);
    }
    for(int i=0;i<v.size();i++){
        if(v[i]==1)continue;
        if(i+k-1>=v.size()){
            printf("IMPOSSIBLE\n");
            return;
        }
        ans++;
        for(int j=i;j<i+k;j++){
            v[j]^=1;
        }
    }
    pd(ans);
    printf("\n");
}
int main(){
    freopen("input.IN","r",stdin);
    freopen("out.txt","w",stdout);
    //ios_base::sync_with_stdio(0);
    int t=1;
    sd(t);
    for(int i=1;i<=t;i++){
       printf("Case #%d: ",i);
       solve();
   }
   return 0;
}
