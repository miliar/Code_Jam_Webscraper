#include<bits/stdc++.h>
using namespace std;
struct P{
    double r,h;
}p[10010];
bool cmp(P &a,P &b){
    return 2*acos(-1)*a.r*a.h>2*acos(-1)*b.r*b.h;
}
int main(){
    int a,n,k,b=1,f;
    double ans,res;
    cin>>a;
    while(a--){
        cin>>n>>k;
        res=0;
        for(int q=0;q<n;++q)cin>>p[q].r>>p[q].h;
        sort(p,p+n,cmp);
        for(int q=0;q<n;++q){
            f=1;
            ans=p[q].r*p[q].r*acos(-1);
            ans+=2*p[q].r*acos(-1)*p[q].h;
            for(int w=0;w<n;++w){
                if(f==k)break;
                if(w!=q&&p[w].r<=p[q].r){
                    f++;
                    ans+=2*p[w].r*acos(-1)*p[w].h;
                    if(f==k)break;
                }
            }
            if(f==k)
                res=max(res,ans);
        }
        cout<<"Case #"<<b++<<": ";
        cout<<fixed<<setprecision(8)<<res<<endl;
    }
}
