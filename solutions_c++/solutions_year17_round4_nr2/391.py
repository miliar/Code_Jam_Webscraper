#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N=1e3+1;
const ll p=1e9+7;
int a[N],s[N];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t,T;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        printf("Case #%d: ",t);
        int i,n,c,m;
        cin>>n>>c>>m;
        memset(a,0,sizeof a);memset(s,0,sizeof s);
        for(i=0;i<m;i++)
        {
            int x,y;
            scanf("%d%d",&x,&y);
            s[y]++;
            a[x]++;
        }
        int ans=0,ans1=0,sum=0;
        for(i=1;i<=c;i++)ans=max(ans,s[i]);
        for(i=1;i<=n;i++)
        {
            sum+=a[i];
            ans=max(ans,sum/i+(sum%i>0));
        }
        for(i=1;i<=n;i++)
            if(a[i]>ans)ans1+=a[i]-ans;
        printf("%d %d\n",ans,ans1);
    }
	return 0;
}
