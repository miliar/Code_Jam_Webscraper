#include<bits/stdc++.h>
using namespace std;
main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T,c;
    scanf("%d",&T);
    for(c=1;c<=T;c++){
        long long n;
        int i,j,ary[100],ans[100],len=0,mark=0,Max=-1;
        scanf("%lld",&n);
        while(n)ary[len++]=n%10,n/=10;
        for(i=0;i<len-1;i++){
            if(ary[i]<ary[i+1]||(mark&&(ary[i]<=ary[i+1])))mark=1,Max=i+1;
            else mark=0;
        }
        for(i=0;i<Max;i++)ans[i]=9;
        if(Max!=-1)ans[Max]=ary[Max]-1;
        for(i=Max+1;i<len;i++)ans[i]=ary[i];
        while(ans[len-1]==0)len--;
        printf("Case #%d: ",c);
        for(i=len-1;i>=0;i--)printf("%d",ans[i]);
        puts("");
    }
}
