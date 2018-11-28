#include<iostream>
#include<string.h>
#include<stdio.h>
#include<set>
#include<map>
using namespace std;

int k[1005],s[1005];
float t[1005];

int main(){
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int T,ca=0;
    int i,j,n,D;
    cin>>T;
    while(T--){
        ca++;
        //scanf("%d%d",&D,&n);
        cin>>D>>n;
        memset(k,0,sizeof(k));
        memset(s,0,sizeof(s));
        memset(t,0,sizeof(t));
        for(i=1;i<=n;i++){
            //scanf("%d%d",&k[i],&s[i]);
            cin>>k[i]>>s[i];
            t[i]=1.0*(D-k[i])/s[i];
        }
        for(i=n-1;i>=1;i--){
            if(t[i+1]>t[i]){
                t[i]=t[i+1];
            }
        }
        printf("Case #%d: %.6f\n",ca,1.0*D/t[1]);
    }
    return 0;
}
