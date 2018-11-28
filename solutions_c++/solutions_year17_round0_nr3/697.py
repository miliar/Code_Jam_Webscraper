#include <stdio.h>
int main(){
    freopen("C-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    for(int t=1;t<=tc;t++){
        long long n,m;
        scanf("%lld %lld",&n,&m);
        long long a=0,b=0,aa=0,bb=0;
        long long l,r;
        if(n==1) l=-1;  else    l=(n-2)/2;
        r=n%2;
        a++;
        printf("Case #%d: ",t);
        while(m>0){
            aa=0;   bb=0;
            m-=a;
            if(m<=0){
                if(r==0)    printf("%lld %lld",l+1,l);
                else        printf("%lld %lld",l+1,l+1);
                break;
            }
            if(r==0){
                aa+=a;
                bb+=a;
            }
            else{
                aa+=2*a;
            }
            m-=b;
            if(m<=0){
                if(r==0)    printf("%lld %lld",l,l);
                else        printf("%lld %lld",l+1,l);
                break;
            }
            if(r==1){
                aa+=b;
                bb+=b;
            }
            else{
                bb+=2*b;
            }
            r=(l+1)%2;
            if(l==0)    l=-1;   else    l=(l-1)/2;
            a=aa;
            b=bb;
//            printf("%d %d %d %d\n",r,l,a,b);
        }
        printf("\n");
    }
}
