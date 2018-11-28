#include<bits/stdc++.h>
using namespace std;
struct bing{
    int r,h;
}arr[1111];
bool cmp(bing a,bing b){
    if(a.r!=b.r){
        return a.r<b.r;
    }
    return a.h>b.h;
}
const double pi= acos(-1.0);
int n,k;
int main(){
    //freopen("A-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int a,b,c,d,e,f,g,h;
    scanf("%d",&b);
    for(int ii=1;ii<=b;ii++){
        scanf("%d%d",&n,&k);
        for(int i=0;i<n;i++){
            scanf("%d%d",&arr[i].r,&arr[i].h);
        }
        double ans=0.0;
        sort(arr,arr+n,cmp);
        set<double> se;
        double su=0.0;
        for(int i=0;i<k-1;i++){
            double t=arr[i].r;
            t*=2.0;t*=pi;
            t*=arr[i].h;
            se.insert(t);
            su+=t;
        }
        for(int i=k-1;i<n;i++){
            double tmp=arr[i].r;
            tmp*=tmp;
            tmp*=pi;
            //tmp*=2.0;
            double tt=(double)arr[i].h*pi*(double)arr[i].r*2.0;
            tmp+=tt;
            tmp+=su;
            ans=max(ans,tmp);
            su+=tt;
            se.insert(tt);
            tt=*se.begin();
            su-=tt;
            se.erase(se.begin());
            //printf("%f\n",su);
        }
        cout<<"Case #"<<ii<<": ";
        cout<<fixed<<setprecision(9)<<ans<<endl;
    }
    return 0;
}
