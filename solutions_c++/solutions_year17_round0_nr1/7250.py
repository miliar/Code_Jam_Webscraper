#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;
typedef long double ld;

#define MAX1 100005
#define mod1 1000000009
#define mod 1000000007
#define rep0(i,n) for(int(i)=0; (i)<(n);++(i))
#define rep1(i,n) for(int(i)=1; (i)<(n);++(i))
#define rep2(i,n) for(int(i)=1; (i)<=(n);++(i))
#define MAX(x, y) (((x) > (y)) ? (x) : (y))
#define MIN(x, y) (((x) < (y)) ? (x) : (y))

int main()
{
    ll t;
    cin>>t;
    int co=1;
    while(t--)
    {
        char a[2000];
        cin>>a;
        int k;
        cin>>k;
        int len =strlen(a);
        //cout<<len<<"\n";
        int ans=0,i;
        for(i=0;i<=len-k;i++)
        {
            if(a[i]=='-')
            {
                ans++;
                for(int j=i;j<i+k;j++)
                {
                    if(a[j]=='+')
                        a[j]='-';
                    else
                        a[j]='+';
                }
            }
        }
        int flag=1;
        for(i=0;i<len;i++)
        {
            if(a[i]=='-')
            {
                flag=0;
                break;
            }
        }
        cout<<"Case #"<<co<<": ";
        co++;
        if(flag)
        {
            cout<<ans<<"\n";
        }
        else
        {
            cout<<"IMPOSSIBLE\n";
        }
    }
    return 0;
}

