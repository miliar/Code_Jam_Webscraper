#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for (int tt=1;tt<=t;tt++)
    {
        int n,p;
        cin>>n>>p;
        int sum=0;
        int a[20];
        a[0]=a[1]=a[2]=a[3]=a[4]=0;
        for (int i=0;i<n;i++)
        {
            int x;
            cin>>x;
            a[x%p]++;
            sum+=x%p;
        }
        int ret;
        if (p==2)
        {
            ret=a[0];
            ret+=a[1]/2;
        }
        else if (p==3)
        {
            ret=a[0];
            int cur=min(a[1],a[2]);
            ret+=cur;
            a[1]-=cur,a[2]-=cur;
            ret+=a[1]/3+a[2]/3;
        }
        else if (p==4)
        {
            ret=a[0];
            int cur=a[2]/2;
            ret+=cur;
            a[2]=a[2]%2;
            cur=min(a[1],a[3]);
            ret+=cur,a[1]-=cur,a[3]-=cur;
            if (a[1])
            {
                if (a[2] && a[1]>1)
                    a[2]=0,a[1]-=2,ret++;
                ret+=a[1]/4;
            }
            else if (a[3])
            {
                if (a[2] && a[3]>1)
                    a[2]=0,a[3]-=2,ret++;
                ret+=a[3]/4;
            }
        }
        cout<<"Case #"<<tt<<": "<<ret+1-(sum%p==0)<<endl;
    }
}
