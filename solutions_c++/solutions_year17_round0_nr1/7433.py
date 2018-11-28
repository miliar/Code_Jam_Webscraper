#include<bits/stdc++.h>
using namespace std;

char b[1009];
int a[1009];

bool check(int n)
{
    for(int i=0;i<n;i++)
    {
        if(a[i]==1)
            return false;
    }
    return true;
}

int main()
{
    ios_base::sync_with_stdio(false);
    int t;
    cin>>t;
    for(int j=1;j<=t;j++)
    {
        cin>>b;
        int k;
        cin>>k;
        int n=strlen(b);
        int cnt=0;
        for(int i=0;i<n;i++)
        {
            if(b[i]=='+')
                a[i]=0;
            else if(b[i]=='-')
                a[i]=1;
        }
        for(int i=0;i<=n-k;i++)
        {
            if(a[i]==1)
            {
                for(int h=i;h<i+k;h++)
                {
                    if(a[h]==0)
                        a[h]=1;
                    else if(a[h]==1)
                        a[h]=0;
                }
                cnt++;
            }

        }
        cout<<"Case #"<<j<<": ";

        if(check(n)==false)
            cout<<"IMPOSSIBLE\n";
        else

            cout<<cnt<<"\n";



    }
    return 0;

}
