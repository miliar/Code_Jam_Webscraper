#include<iostream>
#include<string.h>
#include<stdio.h>
#include<set>
#include<map>
using namespace std;

int c[10];
int ans[1005];

int main(){
    //freopen("B-small-attempt4.in","r",stdin);
    //freopen("B-small-attempt4.out","w",stdout);
    //freopen("in.txt","r",stdin);
    int T,ca=0;
    int n,i,j,k;
    scanf("%d",&T);
    while(T--){
        ca++;
        scanf("%d",&n);
        for(i=1;i<=6;i++){
            scanf("%d",&c[i]);
        }
        c[2]=c[3];
        c[3]=c[5];
        int m1,m2,m3;
        int mm = 0;
        /*for(i=1;i<=3;i++){
            printf("%d ",c[i]);
        }
        printf("\n");*/
        for(i=1;i<=3;i++){
            if(mm<c[i]){
                mm=c[i];
                m1=i;
            }
        }
        if(m1==1){
            if(c[2]>c[3]){
                m2=2;
                m3=3;
            }
            else{
                m2=3;
                m3=2;
            }
        }
        if(m1==2){
            if(c[1]>c[3]){
                m2=1;
                m3=3;
            }
            else{
                m2=3;
                m3=1;
            }
        }
        if(m1==3){
            if(c[1]>c[2]){
                m2=1;
                m3=2;
            }
            else{
                m2=2;
                m3=1;
            }
        }
        //printf("%d %d %d\n",m1,m2,m3);
        if(n/2<c[m1]){
            printf("Case #%d: IMPOSSIBLE\n",ca);
            //printf("%d %d %d %d\n",n,c[m1],c[m2],c[m3]);
            continue;
        }

        int pos=0;
        memset(ans,0,sizeof(ans));
        //printf("CA%d   %d %d %d %d\n",ca,n,c[m1],c[m2],c[m3]);
        for(i=1;i<=c[m1];i++){
            ans[pos]=m1;
            //printf("%d ",pos);
            if(i<c[m1]) pos+=2;
        }
        //printf("\n\n");
        for(i=1;i<=c[m2];i++){
            while(ans[pos]){
                pos++;
                if(pos>=n) pos-=n;
            }
            ans[pos]=m2;
            //printf("%d ",pos);
            pos+=2;
            if(pos>=n) pos-=n;
        }
        //printf("\n\n");
        int cnt = 0;
        for(i=0;i<n;i++){
            if(!ans[i]) {
                ans[i]=m3;
                cnt++;
            }
        }
        if(cnt!=c[m3]){
            printf("error!\n");
            printf("%d %d %d %d\n",n,c[m1],c[m2],c[m3]);
        }
        //printf("\n\n");
        printf("Case #%d: ",ca);
        for(i=0;i<n;i++){
            if(ans[i]==1) printf("R");
            if(ans[i]==2) printf("Y");
            if(ans[i]==3) printf("B");
        }
        printf("\n");
        for(i=0;i<n-1;i++){
            if(ans[i]==ans[i+1]){
                printf("error!\n");
                printf("%d %d %d %d\n",n,c[m1],c[m2],c[m3]);
            }
        }
        if(ans[n-1]==ans[0]){
            printf("error!\n");
            printf("%d %d %d %d %d\n",n,n/2,c[m1],c[m2],c[m3]);
        }
        /*for(i=0;i<n;i++){
            printf("%d",ans[i]);
        }
        printf("\n");*/
    }
    return 0;
}
