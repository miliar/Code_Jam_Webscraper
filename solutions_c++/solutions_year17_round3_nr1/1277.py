#include <iostream>
#include <stdio.h>
#include <cstring>
#include <math.h>
#include <algorithm>
using namespace std;
const double pi=acos(-1);
struct node{
    double r;
    double h;
    double cemianji;
}no[1005],no2[1005];
bool cmp(node a,node b){
    if(a.r>b.r)return true;
    if(a.r<b.r)return false;
    if(a.cemianji>b.cemianji)return true;
    else return false;
}
bool cmp2(node a,node b){
    return a.cemianji>b.cemianji;
}
int main()
{
    freopen("E://project/code-jam/2017/round1c/A-large.in","r",stdin);
    freopen("E://project/code-jam/2017/round1c/a-large.txt","w",stdout);
    int t,n,k,K=0;
    cin>>t;
    double ans,temp;
    while(t--){
        scanf("%d%d",&n,&k);
        for(int i=0;i<n;i++){
            scanf("%lf%lf",&no[i].r,&no[i].h);
            no[i].cemianji=2.0*pi*no[i].r*no[i].h;
        }
        sort(no,no+n,cmp);
        for(int i=0;i<n;i++){
         //   cout<<no[i].r<<"  "<<no[i].cemianji<<endl;
        }
        ans=0;temp=0;
        for(int i=0;i<n-k+1;i++){
            temp=pi*no[i].r*no[i].r+no[i].cemianji;
            for(int j=i+1;j<n;j++)no2[j]=no[j];
            sort(no2+i+1,no2+n,cmp2);
            for(int j=i+1;j<i+k;j++)temp+=no2[j].cemianji;
            ans=max(ans,temp);
        }
        printf("Case #%d: %.9f\n",++K,ans);
    }
    return 0;
}
