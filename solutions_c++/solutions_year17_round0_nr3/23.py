#include<cstdio>
#include<cstring>
using namespace std;

long long TEST,t,len,i,j,a,b,c,k,x,y,mx,mn;

int main(){
    scanf("%lld",&TEST);
    for(t=1;t<=TEST;t++){
        scanf("%lld %lld",&a,&k);
        b=1;
        c=0;
        while(1){
            x=0;
            y=0;
            if(a%2==0){
                if(k<=c){
                    mx=a/2;
                    mn=a/2;
                    break;
                }
                k-=c;
                y+=c*2;
                if(k<=b){
                    mx=a/2;
                    mn=a/2-1;
                    break;
                }
                k-=b;
                x+=b;
                y+=b;
                a=a/2-1;
            }
            else{
                if(k<=c){
                    mx=a/2+1;
                    mn=a/2;
                    break;
                }
                k-=c;
                x+=c;
                y+=c;
                if(k<=b){
                    mx=a/2;
                    mn=a/2;
                    break;
                }
                k-=b;
                x+=2*b;
                a=a/2;
            }
            b=x;
            c=y;
        }
        printf("Case #%lld: %lld %lld\n",t,mx,mn);
    }
    return 0;
}
