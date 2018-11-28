#include<bits/stdc++.h>
//#include "A-small-practice.in"
#include <fstream>
#define ll long long
#define pf printf
#define sf scanf
using namespace std;

ll powe(ll a, int b)
{
    ll temp=1;
    for(int i=0;i<b;i++)
        temp*=a;

    return temp;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output2L.out","w",stdout);
    int T;
    cin>>T;
    for(int t=0;t<T;t++)
    {
        ll N;
        cin>>N;
        string s="";
        while(N!=0)
        {
            int k;
            k = N%10;
            N/=10;
            s+=('0'+k);
        }
        //cout << s << endl;
        for(int i=s.size()-1;i>=0;i--)
        {
            if(s[i]=='0')
            {
                for(int j=0;j<=i;j++)
                    s[j]='9';

                s[i+1] = ((s[i+1] - '0' - 1)+'0');
            }
        }
        //cout << s << endl;
        /*for(int i=0;i<s.size()-1;i++)
        {
            if(s[i]<s[i+1])
            {
                if(i==0)
                {
                    s[i]='9';
                    s[i+1] = ((s[i+1] - '0' - 1)+'0');
                }
                else
                {
                    s[i+1]=s[i];
                }
            }
        }*/
        for(int i=0;i<s.size()-1;i++)
        {
            if(s[i]<s[i+1])
            {
                for(int j=0;j<=i;j++)
                    s[j]='9';

                s[i+1] = ((s[i+1] - '0' - 1)+'0');
            }
        }
        ll ans=0;
        for(int i=0;i<s.size();i++)
            ans+=(s[i]-'0')*powe(10,i);

        cout << "Case #" << t+1 << ": " << ans << endl;
    }

    return 0;
}

