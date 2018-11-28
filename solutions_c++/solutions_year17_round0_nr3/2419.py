#include <iostream>
#include <stdio.h>
#include <cstring>
using namespace std;
long long e[100];
void init(){
    e[0]=1;
    for(int i=1;e[i-1]<=1e18;i++){
        e[i]=e[i-1]+e[i-1];
    }
}
int main()
{
    freopen("E://project/code-jam/2017/Qualification/C-large.in","r",stdin);
    freopen("E://project/code-jam/2017/Qualification/C-large-out.txt","w",stdout);
    int t,kk=0;
    cin>>t;
    long long k,n;
    init();
    while(t--){
        scanf("%lld%lld",&n,&k);
        if(n==1){
            printf("Case #%d: 0 0\n",++kk);continue;
        }
        int level=0;
        while(e[level]+e[level]-1<k)level++;
        level--;
        long long loc=k-e[level]-e[level]+1;
        long long cur=n-e[level]-e[level]+1;
        long long x=cur/e[level+1],y,ans,a,b;
        y=cur-(x*e[level+1]);
        if(loc<=y)ans=x+1;
        else ans=x;
        if(k==1){
            ans=n;
        }
        ans--;
        a=ans/2;b=a;
        if(a+b<ans)b++;
        printf("Case #%d: %lld %lld\n",++kk,b,a);
    }
    return 0;
}
