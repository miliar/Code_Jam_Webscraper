#include<bits/stdc++.h>
using namespace std;
char s[10000000];
int main()
{
    long long n,t,i,j,k,l,a1,ans,f;
    double x,y,d,m;
    cin>>t;m=0;j=0;
    while(t--)
    {j++;m=0.0;
        cin>>d>>n;
        for(i=0;i<n;++i)
        {
            cin>>x>>y;
           // cout<<x<<" "<<y<<"\n";
            x=d-x;
            y=x/y;
            //cout<<x<<" "<<y<<"\n";
            if(y>m)
            {
                m=y;
            }

        }cout<<"Case #"<<j<<": ";
        printf("%.12f\n",d/m);

    }




    return 0;
}
