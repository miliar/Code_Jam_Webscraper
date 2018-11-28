#include <bits/stdc++.h>
#define ll long long int
#define mod 1000000007
using namespace std;

ll t,tt,i,j,n,a[30];
string str;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    tt=t;
    while(t)
    {
        cin>>str;
        n=str.length();
        for(i=0;i<n;i++)
        {
            a[i]=str[i]-'0';
        }
        for(i=1;i<n;i++)
        {
            if(a[i]>=a[i-1])
                continue;

            for(j=0;j<i;j++)
            {
                if(a[j]==a[i-1])
                    break;
            }
            a[j]--;
            j++;
            for(;j<n;j++)
                a[j]=9;
            break;
        }

        cout<<"Case #"<<tt-t+1<<": ";
        i=0;
        while(!a[i])
        {
            i++;
        }
        for(;i<n;i++)
            cout<<a[i];
        cout<<endl;

        t--;
    }

    return 0;
}
