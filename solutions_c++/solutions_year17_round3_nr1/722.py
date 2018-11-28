#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
const  double  pi =3.1415926535897;
struct node{
    double r,h,sum;
}a[1005];
int cmp(node x,node y){
    return x.sum>y.sum;
}
int main()
{
    freopen("in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,n,k;
    cin>>T;
    for(int ca=1;ca<=T;ca++){
       // cerr<<ca<<endl;
        cin>>n>>k;
        for(int i=1;i<=n;i++){
            cin>>a[i].r>>a[i].h;
            a[i].sum=2*pi*a[i].r*a[i].h;
        }
        sort(a+1,a+1+n,cmp);
        double ans=0;
        for(int i=1;i<=n;i++){
            double tmp=pi*a[i].r*a[i].r+a[i].sum;int num=k-1;

            for(int j=1;j<=n;j++){
                if(j==i)continue;
                if(a[j].r>a[i].r)continue;
                if(num==0)break;

                tmp+=a[j].sum;num--;

            }
            ans=max(ans,tmp);
        }
        printf("Case #%d: %.10lf\n",ca,ans);
    }
    return 0;
}
