#include <stdio.h>

using namespace std;

int main()
{

    int i,k,T,x,a,b,temp[25],count=1;
    long long int N,j;
    scanf("%d",&T);
    while(count<=T){
        scanf("%lld",&N);
        b=0;
        for(j=N;j>0;j/=10){
            a=j%10;
            temp[b++]=a;
        }
        for(i=1;i<b;i++){
            if(temp[i-1]<temp[i]){
                temp[i]--;
                k=i-1;
                for(x=k;x>=0;x--){
                    temp[x]=9;
                }
            }
        }
        j=0;
        i=b-1;
        while(i>=0){
            j=j*10+temp[i];
            i--;
        }
        printf("Case #%d:\t%lld\n",count,j);
        count++;
    }
    return 0;
}
