#include <iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int r=1;
    while(r<=t)
    {
        int n;
        cin>>n;
        int a,q,p,m;
        m=n;
        while(m>0)
        {
            a=m;
            p=a%10;
            int flag=1;
            while(a/10!=0)
            {
                a=a/10;
                q=a%10;
                if(q>p)
                {
                    flag=0;
                    break;
                }
                p=q;

            }
            if(flag==1)
            {
                cout<<"Case #"<<r<<": "<<m<<endl;
                break;
            }
            m--;
        }
    r++;

    }
}
