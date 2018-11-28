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

char buf[22];
int len;
bool isTidy(ll x){
    mem(buf,0);
    sprintf(buf,"%lld",x);
    len=strlen(buf);
    for(int i=0;i<len-1;i++){
        if(buf[i]>buf[i+1]) {
            return false;
        }
    }
    return true;
}

ll bl(ll x){
    while(!isTidy(x)) x--;
    return x;
}

ll solve(ll x){
    int base=0;
    while(!isTidy(x)){
        int pos=len-1-base;
        buf[pos]='9';
        if(buf[pos-1]>'0') buf[pos-1]--;
        else {
            while(buf[pos-1]=='0'){
                buf[pos-1]='9';
                pos--;
            }
            buf[pos-1]--;
        }
        string str=buf;
        stringstream ss(str);
        ss>>x;
        base++;
        //cout<<base<<" "<<x<<endl;
    }
    return x;
}
int main()
{
#ifndef ONLINE_JUDGE
    freopen("d:\\B-large.in","r",stdin);
    freopen("d:\\out2.txt","w",stdout);
#endif
//    for(int i=1;i<=1000;i++){
//        if(bl(i)!=solve(i)){
//            cout<<i<<" "<<bl(i)<<" "<<solve(i)<<endl;
//        }
//    }
    int T; cin>>T;
    for(int cs=1;cs<=T;cs++){
        ll n;
        cin>>n;
        ll ans=solve(n);
        printf("Case #%d: ",cs);
        printf("%lld\n",ans);
        //cout<<bl(n)<<endl;
    }
    return 0;
}