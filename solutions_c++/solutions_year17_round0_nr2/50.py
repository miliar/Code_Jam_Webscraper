#include<cstdio>
#include<algorithm>
using namespace std;
long long n, po[19];
int main(){
    freopen("/Users/joseunghyeon/Downloads/B-large.in","r",stdin);
    freopen("/Users/joseunghyeon/Desktop/code2/output.txt","w",stdout);
    int TT, TC, i;
    po[0]=1;
    for(i=1;i<=18;i++)po[i]=po[i-1]*10;
    scanf("%d",&TC);
    for(TT=1;TT<=TC;TT++){
        printf("Case #%d: ",TT);
        scanf("%lld",&n);
        for(i=18;i>=0;i--){
            if(n/po[i]*po[i] + ((n/po[i])%10) * (po[i]/9) > n){
                n=n/po[i]*po[i] - 1;
                break;
            }
        }
        printf("%lld\n",n);
    }
}
