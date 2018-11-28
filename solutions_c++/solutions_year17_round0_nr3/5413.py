#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<cstring>
using namespace std;

int i,j,k[110],l,max1,f[1000010],n[110],p,index,e,r;

int compInc(const void *a, const void *b)  
{  
    return *(int *)a - *(int *)b;  
}  

int main(){
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    cin>>r;
    for(e=0;e<r;e++)
        cin>>n[e]>>k[e];
    for(e=0;e<r;e++){
    f[0]=0;
    f[1]=n[e]+1;

    for (i=1;i<=k[e];i++)f[i+1]=0;
    
    for(i=0;i<k[e];i++){
        qsort(f, i+2, sizeof(f[0]), compInc);  
        max1=0;
        for(j=0;j<i+1;j++){
            if(f[j+1]-f[j]-1>max1){max1=f[j+1]-f[j]-1;p=f[j];}
        }
        index=p+(max1+1)/2;
        if (i==k[e]-1)cout<<"Case #"<<e+1<<": "<<(max1)/2<<' '<<max1-1-(max1)/2<<endl;
        f[i+2]=index;
    }}
    
    
    return 0;
}
