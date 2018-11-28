#include<stdio.h>
#include<algorithm>
using namespace std;
void doit(){
    long long n,k;
    scanf("%I64d%I64d",&n,&k);//5 2
    long long temp = n;
    long long p = k - 1;
    long long r = 1;
    long long x = 0;
    while(p >= r){
        p -= r;
        temp /= 2;
        r *= 2;
    }
    p ++;
    //printf("p:%I64d r:%I64d ",p,r);
    if(p <= (n - k + p) % r){
        printf("%I64d %I64d\n",((n - k + p) / r + 1) / 2, ((n - k + p) / r ) / 2);
    }else{
        printf("%I64d %I64d\n",((n - k + p) / r ) / 2, ((n - k + p) / r - 1) / 2);
    }
}
int main(){
    int t;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        printf("Case #%d: ",i);
        doit();
    }
}
