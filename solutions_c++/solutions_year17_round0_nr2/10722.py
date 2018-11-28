#include<bits/stdc++.h>

using namespace std;
typedef unsigned long long ull;

int main()
{
    ull t,n,u,m,i,x;
    cin>>t;
    u=t;
    while(t--)
    {
        cin>>n;
        if(n/10==0)
            cout<<"Case #"<<u-t<<": "<<n<<endl;
            else
            {
                for(i=n;i>10;i--)
                {
                    m=i; ull flag=0;
                    while(m>9)
                    {
                        x=m%10;
                        m=m/10;
                        if(m%10>x)
                        {
                            flag=1;
                            break;
                        }
                    }
                    if(flag==0)
                    {
                        break;
                    }

                }
                cout<<"Case #"<<u-t<<": "<<i<<endl;
            }
    }


    return 0;
}
