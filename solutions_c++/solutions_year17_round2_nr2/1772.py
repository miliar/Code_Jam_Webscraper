#include<bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int (i)=(a);(i)<=(b);++i)
#define repd(i,a,b) for(int (i)=(a); (i)>=(b);--i)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define ll long long int

int main()
{
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        int n,i,j,a[8],flag=0,b[1004];
        cin>>n;
        rep(i,1,6)
            cin>>a[i];
        if(n==1)
        {
            rep(i,1,6)
            {
                if(a[i]==1)
                    b[1]=i;
            }
            goto z;
        }
        if(a[2]==0&&a[4]==0&&a[6]==0)
        {
            if(a[1]==0)
            {
                if(a[3]!=a[5])
                {
                    flag=1;
                    goto z;
                }
                else
                {
                    rep(i,1,n)
                    {
                        b[i++]=3;
                        b[i]=5;
                    }
                    goto z;
                }
            }
            if(a[3]==0)
            {
                if(a[1]!=a[5])
                {
                    flag=1;
                    goto z;
                }
                else
                {
                    rep(i,1,n)
                    {
                        b[i++]=1;
                        b[i]=5;
                    }
                    goto z;
                }
            }
            if(a[5]==0)
            {
                if(a[3]!=a[1])
                {
                    flag=1;
                    goto z;
                }
                else
                {
                    rep(i,1,n)
                    {
                        b[i++]=1;
                        b[i]=3;
                    }
                    goto z;
                }
            }
            if(a[1]+a[3]<a[5]||a[1]+a[5]<a[3]||a[3]+a[5]<a[1])
            {
                flag =1;
                goto z;
            }
            else
            {
                if(a[1]>=a[3]&&a[1]>=a[5])
                {
                    int x=a[3]+a[5]-a[1],j=1;
                    rep(i,1,x)
                    {
                        b[j++]=1;
                        b[j++]=3;
                        b[j++]=5;
                    }
                    rep(i,x+1,a[3])
                    {
                        b[j++]=1;
                        b[j++]=3;
                    }
                    rep(i,x+1,a[5])
                    {
                        b[j++]=1;
                        b[j++]=5;
                    }
                    goto z;
                }
                if(a[3]>=a[1]&&a[3]>=a[5])
                {
                    int x=a[1]+a[5]-a[3],j=1;
                    rep(i,1,x)
                    {
                        b[j++]=3;
                        b[j++]=5;
                        b[j++]=1;
                    }
                    rep(i,x+1,a[5])
                    {
                        b[j++]=3;
                        b[j++]=5;
                    }
                    rep(i,x+1,a[1])
                    {
                        b[j++]=3;
                        b[j++]=1;
                    }
                    goto z;
                }
                if(a[5]>=a[1]&&a[5]>=a[5])
                {
                    int x=a[1]+a[3]-a[5],j=1;
                    rep(i,1,x)
                    {
                        b[j++]=5;
                        b[j++]=1;
                        b[j++]=3;
                    }
                    rep(i,x+1,a[1])
                    {
                        b[j++]=5;
                        b[j++]=1;
                    }
                    rep(i,x+1,a[3])
                    {
                        b[j++]=5;
                        b[j++]=3;
                    }
                    goto z;
                }

            }
        }
        else
        {
            if(a[1]==0&&a[3]==0&&a[4]==0&&a[6]==0)
            {
                if(a[2]==a[5])
                {
                    rep(i,1,a[2])
                    {
                        b[2*i-1]=2;
                        b[2*i]=5;
                    }
                    goto z;
                }
                else
                {
                    flag=1;
                    goto z;
                }
            }
            if(a[2]==0&&a[3]==0&&a[5]==0&&a[6]==0)
            {
                if(a[1]==a[4])
                {
                    rep(i,1,a[1])
                    {
                        b[2*i-1]=1;
                        b[2*i]=4;
                    }
                    goto z;
                }
                else
                {
                    flag=1;
                    goto z;
                }
            }

            if(a[1]==0&&a[2]==0&&a[4]==0&&a[5]==0)
            {
                if(a[3]==a[6])
                {
                    rep(i,1,a[3])
                    {
                        b[2*i-1]=3;
                        b[2*i]=6;
                    }
                    goto z;
                }
                else
                {
                    flag=1;
                    goto z;
                }
            }
            if(a[2]>a[5]||a[4]>a[1]||a[6]>a[3])
            {
                flag =1;
                goto z;
            }
            else{
                a[1]=a[1]-a[4];
                a[3]=a[3]-a[6];
                a[5]=a[5]-a[2];
               /*int i1=1,i3=1,i5=1;
               rep(i,1,a[4])
               {
                   c[i1++]=1;
               }*/

                if(a[1]==0)
            {
                if(a[3]!=a[5])
                {
                    flag=1;
                    goto z;
                }
                else
                {
                    j=1;
                    for(i=1;j<=n;i++)
                    {
                        if(i<=a[6])
                        {
                            b[j++]=3;
                            b[j++]=6;
                            b[j++]=3;
                        }
                        else
                            b[j++]=3;
                        if(i<=a[2])
                        {
                            b[j++]=5;
                            b[j++]=2;
                            b[j++]=5;
                        }
                        else b[j++]=5;
                    }
                    goto z;
                }
            }
            if(a[3]==0)
            {
                if(a[1]!=a[5])
                {
                    flag=1;
                    goto z;
                }
                else
                {
                    j=1;
                    for(i=1;j<=n;i++)
                    {
                        if(i<=a[4])
                        {
                            b[j++]=1;
                            b[j++]=4;
                            b[j++]=1;
                        }
                        else
                            b[j++]=1;
                        if(i<=a[2])
                        {
                            b[j++]=5;
                            b[j++]=2;
                            b[j++]=5;
                        }
                        else b[j++]=5;
                    }
                    goto z;
                }
            }
            if(a[5]==0)
            {
                if(a[3]!=a[1])
                {
                    flag=1;
                    goto z;
                }
                else
                {
                    j=1;
                    for(i=1;j<=n;i++)
                    {
                        if(i<=a[6])
                        {
                            b[j++]=3;
                            b[j++]=6;
                            b[j++]=3;
                        }
                        else
                            b[j++]=3;
                        if(i<=a[4])
                        {
                            b[j++]=1;
                            b[j++]=4;
                            b[j++]=1;
                        }
                        else b[j++]=1;
                    }
                    goto z;
                }
            }
            if(a[1]+a[3]<a[5]||a[1]+a[5]<a[3]||a[3]+a[5]<a[1])
            {
                flag =1;
                goto z;
            }
            else
            {
                if(a[1]>=a[3]&&a[1]>=a[5])
                {
                    int x=a[3]+a[5]-a[1],j=1;
                    rep(i,1,x)
                    {
                        if(i<=a[4])
                        {
                            b[j++]=1;
                            b[j++]=4;
                            b[j++]=1;
                        }
                        else b[j++]=1;
                        if(i<=a[6])
                        {
                            b[j++]=3;
                            b[j++]=6;
                            b[j++]=3;
                        }
                        else
                        b[j++]=3;
                        if(i<=a[2])
                        {
                            b[j++]=5;
                            b[j++]=2;
                            b[j++]=5;
                        }
                        else
                        b[j++]=5;
                    }
                    rep(i,x+1,a[3])
                    {
                        if(i<=a[4])
                        {
                            b[j++]=1;
                            b[j++]=4;
                            b[j++]=1;
                        }
                        else
                        b[j++]=1;
                        if(i<=a[6])
                        {
                            b[j++]=3;
                            b[j++]=6;
                            b[j++]=3;
                        }
                        else
                        b[j++]=3;
                    }
                    rep(i,x+1,a[5])
                    {
                        if(i+a[3]-x<=a[4])
                        {
                            b[j++]=1;
                            b[j++]=4;
                            b[j++]=1;
                        }
                        else
                        b[j++]=1;
                        if(i<=a[2])
                        {
                            b[j++]=5;
                            b[j++]=2;
                            b[j++]=5;
                        }
                        else
                        b[j++]=5;
                    }
                    goto z;
                }
                if(a[3]>=a[1]&&a[3]>=a[5])
                {
                    int x=a[1]+a[5]-a[3],j=1;
                    rep(i,1,x)
                    {
                        if(i<=a[6])
                        {
                            b[j++]=3;
                            b[j++]=6;
                            b[j++]=3;
                        }
                        else
                        b[j++]=3;
                        if(i<=a[2])
                        {
                            b[j++]=5;
                            b[j++]=2;
                            b[j++]=5;
                        }
                        else
                        b[j++]=5;
                        if(i<=a[4])
                        {
                            b[j++]=1;
                            b[j++]=4;
                            b[j++]=1;
                        }
                        else
                        b[j++]=1;
                    }
                    rep(i,x+1,a[5])
                    {
                        if(i<=a[6])
                        {
                            b[j++]=3;
                            b[j++]=6;
                            b[j++]=3;
                        }
                        else
                        b[j++]=3;
                        if(i<=a[2])
                        {
                            b[j++]=5;
                            b[j++]=2;
                            b[j++]=5;
                        }
                        else
                        b[j++]=5;
                    }
                    rep(i,x+1,a[1])
                    {
                        if(i+a[5]-x<=a[6])
                        {
                            b[j++]=3;
                            b[j++]=6;
                            b[j++]=3;
                        }
                        else
                        b[j++]=3;
                        if(i<=a[4])
                        {
                            b[j++]=1;
                            b[j++]=4;
                            b[j++]=1;
                        }
                        else
                        b[j++]=1;
                    }
                    goto z;
                }
                if(a[5]>=a[1]&&a[5]>=a[5])
                {
                    int x=a[1]+a[3]-a[5],j=1;
                    rep(i,1,x)
                    {
                        if(i<=a[5])
                        {
                            b[j++]=5;
                            b[j++]=2;
                            b[j++]=5;
                        }
                        else
                        b[j++]=5;
                        if(i<=a[4])
                        {
                            b[j++]=1;
                            b[j++]=4;
                            b[j++]=1;
                        }
                        else
                        b[j++]=1;
                        if(i<=a[6])
                        {
                            b[j++]=3;
                            b[j++]=6;
                            b[j++]=3;
                        }
                        else
                        b[j++]=3;
                    }
                    rep(i,x+1,a[1])
                    {
                        if(i<=a[2])
                        {
                            b[j++]=5;
                            b[j++]=2;
                            b[j++]=5;
                        }
                        else
                        b[j++]=5;
                        if(i<=a[4])
                        {
                            b[j++]=1;
                            b[j++]=4;
                            b[j++]=1;
                        }
                        else
                        b[j++]=1;
                    }
                    rep(i,x+1,a[3])
                    {
                        if(i+a[1]-x<=a[2])
                        {
                            b[j++]=5;
                            b[j++]=2;
                            b[j++]=5;
                        }
                        else
                        b[j++]=5;
                        if(i<=a[6])
                        {
                            b[j++]=3;
                            b[j++]=6;
                            b[j++]=3;
                        }
                        else
                        b[j++]=3;
                    }
                    goto z;
                }

            }
            }
        }
        z:
            if(flag==1)
        cout<<"Case #"<<tt<<": IMPOSSIBLE\n";
        else
        {
            cout<<"Case #"<<tt<<": ";
            char c[6]={'R','O','Y','G','B','V'};
            rep(i,1,n)
            {
                cout<<c[b[i]-1];
            }
            cout<<endl;
        }
    }
        return 0;
}
