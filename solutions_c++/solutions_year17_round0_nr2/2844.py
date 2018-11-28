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
void solve(){
    string s;
    cin>>s;
    int cur=-1;
    for(int i=0;i<s.size()-1;i++){
        if(s[i]>s[i+1]){
            s[i]=s[i]-1;
            for(int j=i+1;j<s.size();j++){
                s[j]='9';
            }
            cur=i;
            break;
        }
    }
    if(cur!=-1){
        for(int i=cur;i>=1;i--){
            if(s[i]<s[i-1]){
                s[i-1]=s[i-1]-1;
                s[i]='9';
            }
        }
    }
    while(s[0]=='0'){
        s.erase(s.begin());
    }
    cout<<s<<endl;
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
