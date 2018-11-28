#include<bits/stdc++.h>
using namespace std;
#define N 1005
int t,c,a[N],n,i,fg,p,q,x;
int main()
{
    freopen("in.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d",&t);
    for(i=1;i<=1000;i++){
        x=i;
        p=10;
        fg=1;
        while(x){
            q=x%10,x/=10;
            if(q>p) { fg=0;break; }
            p=q;
        }
        a[i]=fg?i:a[i-1];
    }
    for(c=1;c<=t;c++) scanf("%d",&n),printf("Case #%d: %d\n",c,a[n]);
}
