#include<cstdio>

using namespace std;
int test,T,n,m,c,a,b,num[1010],k[3],mx,mx2,i;

int main(){
    scanf("%d",&test);
    for(T=1;T<=test;T++){
        scanf("%d %d %d",&n,&c,&m);
        for(i=1;i<=n;i++)num[i]=0;
        k[1]=0;
        k[2]=0;
        for(i=0;i<m;i++){
            scanf("%d %d",&a,&b);
            num[a]++;
            k[b]++;
        }
        mx=k[1];
        if(k[2]>k[1])mx=k[2];
        if(num[1]>mx)mx=num[1];
        mx2=0;
        for(i=1;i<=n;i++){
            if(num[i]>mx){
                mx2=num[i]-mx;
            }
        }
        printf("Case #%d: %d %d\n",T,mx,mx2);
    }
}
