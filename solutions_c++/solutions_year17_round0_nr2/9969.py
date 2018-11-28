#include<bits/stdc++.h>
using namespace std;
#include<algorithm>
int main()
{
    freopen("B-small-attempt4.in","r",stdin);
    freopen("output.in","w",stdout);
    std::ios_base::sync_with_stdio(false);
    int t,n,a[1001],count,m,i,j,k,flag=1,l,count1=0;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        i=0;
        flag=1;
        count=0;
        cin>>n;
        m=n;
        while(m>0)
        {
            a[i++]=m%10;
            m=m/10;
        }
        i--;
        count=i;
       if(i==0)
        {
            flag=2;
            cout<<"Case #"<<k<<": ";
            cout<<n<<endl;

        }
        else
        {
            for(j=0;j<count;j++)
            {
                if(a[j]<a[j+1])
                    {
                        for(l=j;l>=0;l--)
                            a[l]=9;
                        a[j+1]-=1;
                    }
                    /*break;
                     }
                i--;
            }
            if(flag==0)
            while(i>=0)
                a[i--]=9;
        }*/
            }
        }
    if(flag!=2)
        {
        if(a[count]==0)
        count-=1;
        cout<<"Case #"<<k<<": ";
        for(j=count;j>=0;j--)
        {
        cout<<a[j];
        }
        cout<<endl;
        }
    }


 return 0;
}
