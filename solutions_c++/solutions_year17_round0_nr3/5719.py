#include <iostream>

using namespace std;
void calclr(int *l,int *r,int *v,int i,int n)
{
    int j;
    for (j=i-1;j>=0;j--)
    {
        if (v[j]==1)
        {
            l[i]=i-j-1;
            break;
        }
    }
    for (j=i+1;j<=n+1;j++)
    {
        if (v[j]==1)
        {
            r[i]=j-i-1;
            break;
        }
    }
}
int main()
{
    int t,tc=1;
    cin>>t;
    while (t--)
    {
       int n,k,i,j;
       cin>>n>>k;
       int l[n+2],r[n+2],v[n+2];
       for (i=1;i<=n;i++)
       {
           v[i]=0;
       }
       v[0]=1;
       v[n+1]=1;
       for (j=0;j<k;j++)
       {
            for (i=1;i<=n;i++)
            {
                if (v[i]==0)
                {
                    calclr(l,r,v,i,n);
                }
            }
            int maxmin=-1,maxmax=-1,maxmin_i,maxmax_i;
            for (i=1;i<=n;i++)
            {
                int p=min(l[i],r[i]);
                if (maxmin<p&&v[i]==0)
                {
                    maxmin=p;
                    maxmin_i=i;
                }
            }
            for (i=1;i<=n;i++)
            {
                int p=min(l[i],r[i]);
                int q=max(l[i],r[i]);
                if (maxmax<q&&p==maxmin&&v[i]==0)
                {
                    maxmax=q;
                    maxmax_i=i;
                }
            }
           // cout<<l[maxmax_i]<<" "<<r[maxmax_i]<<endl;
            v[maxmax_i]=1;
           if (j==(k-1))
            {
                cout<<"Case #"<<tc<<": ";
                cout<<max(l[maxmax_i],r[maxmax_i])<<" "<<min(l[maxmax_i],r[maxmax_i])<<endl;
            }

       }
       tc++;
    }
    return 0;
}
