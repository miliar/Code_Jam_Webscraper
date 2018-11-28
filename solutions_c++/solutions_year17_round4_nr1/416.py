#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N=1e1+1;
const ll p=1e9+7;
int a[N];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,T;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        printf("Case #%d: ",t);
        int i,n,p;memset(a,0,sizeof a);
        cin>>n>>p;
        for(i=0;i<n;i++)
        {
            int x;
            scanf("%d",&x);
            a[x%p]++;
        }
        if(p==2)printf("%d\n",a[0]+(a[1]+1)/2);
        if(p==3)printf("%d\n",a[0]+min(a[1],a[2])+(max(a[1],a[2])-min(a[1],a[2])+2)/3);
        if(p==4)
        {
            int ans=a[0];
            ans+=min(a[1],a[3]);
            a[2]+=(max(a[1],a[3])-min(a[1],a[3])+1)/2;
            ans+=(a[2]+1)/2;
            printf("%d\n",ans);
        }
    }
	return 0;
}
