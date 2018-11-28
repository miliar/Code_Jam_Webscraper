#include<bits/stdc++.h>


int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-out.txt","w",stdout);
    long long x,y;
    int T,t=0,a[30]={0},s;
    scanf("%d",&T);
    while(T--){
        t++;
        scanf("%lld",&y);
        x=y;
        s=0;
        while(x){
            a[s++]=x%10;
            x/=10;
        }
        printf("Case #%d: ",t);
        bool flag=true;
        int pp;
        for(int k=s-1;k>=1;k--){
            if(a[k]>a[k-1]){
                pp=k;
                flag=false;
                break;
            }
        }
        if(flag){
            printf("%lld\n",y);
            continue;
        }
        int no=s-1;
        for(int k=pp;k<s-1;k++){
            if(a[k]-1>=a[k+1]){
                no=k;
                break;
            }
        }
        for(int k=s-1;k>no;k--) printf("%d",a[k]);
        if(a[no]>1||no!=s-1) printf("%d",a[no]-1);
        for(int k=no-1;k>=0;k--) printf("9");
        puts(""); 
    }
}
        
