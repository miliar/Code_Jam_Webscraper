#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<cstring>
using namespace std;

int i,j,k[110],l,max1,f[1000010],n[110],p,index,e,r;

int compInc(const void *a, const void *b)  
{  
    return *(int *)b - *(int *)a;  
}  

int main(){
    freopen("C-small-1-attempt0.in","r",stdin);
    freopen("C-small-1-attempt0.out","w",stdout);
    cin>>r;
    for(e=0;e<r;e++)
        cin>>n[e]>>k[e];
    for(e=0;e<r;e++){
    f[0]=n[e];
   

    for (i=1;i<=k[e];i++)f[i+1]=0;
    
    for(i=0;i<k[e];i++){
        qsort(f, i+1, sizeof(f[0]), compInc);  
        max1=f[0];
        f[0]=max1/2;
        f[i+1]=max1-max1/2-1;
        if (i==k[e]-1)cout<<"Case #"<<e+1<<": "<<(max1)/2<<' '<<max1-1-(max1)/2<<endl;
    
    }}
    
    
    return 0;
}
