#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
    int t;
    scanf("%d",&t);
    int x=t;
    while(t--){
    ll n,k,i,f=2;
    int s;
     cin>>n>>k;
     int arr[61],j=0;
     for(i=1LL<<60;i>0;i=i/2){
        if(k&i){
            arr[j]=1;
            j++;
        }
        else{
            arr[j]=0;
            j++;
        }
     }
     for(s=0;s<61;s++){
        if(arr[s]==1)
            break;
     }
     //cout<<s<<endl;
     ll l=1,r=n,m=(l+r)/f,ls,rs;
     for(j=60;j>=s+1;j--){
        if(arr[j]==1){
            r=m-1LL;
        }
        else{
            l=m+1LL;
        }
        m=(l+r)/f;
     }
    // printf("%d %d %d\n",l,r,m);
     m=(l+r)/2LL;
     ls=m-l;
     rs=r-m;
     printf("Case #%d: %lld %lld\n",x-t,max(ls,rs),min(ls,rs));
    }
}
