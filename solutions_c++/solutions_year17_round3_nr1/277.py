#include <bits/stdc++.h>
using namespace std;
typedef double LD;
struct hh{
    int r,h;
    LD val;
    inline void init(){
        cin>>r>>h;
        val=(LD)2.0*M_PI*r*h;
    }
    inline LD s(){
        return (LD)M_PI*r*r;
    }
    bool operator <(const hh &b){
        return val>b.val;
    }
}a[100000];
int T,n,k;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    cin>>T;
    for(int ti=1;ti<=T;ti++){
        cin>>n>>k;
        for(int i(1);i<=n;i++)
            a[i].init();
        sort(a+1,a+n+1);
        LD ans=0.0;
        for(int i(1);i<=n;i++){
            LD tmp=a[i].s()+a[i].val;
            int cnt(1);
            for(int j(1);j<=n;j++)
                if(j!=i&&a[j].r<=a[i].r&&cnt<k)
                    tmp+=a[j].val,cnt++;
            ans=max(ans,tmp);
        }
        printf("Case #%d: %lf\n",ti,ans);
        //cout<<ans<<endl;
    }   
    return 0;
}