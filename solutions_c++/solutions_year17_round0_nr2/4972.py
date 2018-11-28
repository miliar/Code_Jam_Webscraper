#include<bits/stdc++.h>
#define ll long long
using namespace std;

vector<ll>v;
ll n;
ll mem[20][20][10][2];
string s;

ll dp(ll pos, ll len, ll prev, ll flag)
{
    if(pos==len)
        return 1;

    if(mem[pos][len][prev][flag]!=-1)
        return mem[pos][len][prev][flag];

    mem[pos][len][prev][flag]= 0;

    if(pos==0)
    {
        if(len==n)
        {
            for(int i= s[pos]-48; i>=1; i--)
            {
                int x;

                if(i==s[pos]-48)
                    x= dp(pos+1, len, i, 0);
                else
                    x= dp(pos+1, len, i, 1);

                if(x)
                {
                    v.push_back(i);
                    return 1;
                }
            }
        }
        else
        {
            for(int i= 9; i>=1; i--)
            {
                if(dp(pos+1, len, i, 1))
                {
                    v.push_back(i);
                    return 1;
                }
            }
        }
    }
    else
    {
        if(!flag)
        {
            for(int i=s[pos]-48; i>=0; i--)
            {
                if(i>=prev)
                {
                    int x;

                    if(i==s[pos]-48)
                        x= dp(pos+1, len, i, 0);
                    else
                        x= dp(pos+1, len, i, 1);

                    if(x)
                    {
                        v.push_back(i);
                        return 1;
                    }
                }
            }
        }
        else
        {
            for(int i=9; i>=0; i--)
            {
                if(i>=prev)
                {
                    if(dp(pos+1, len, i, flag))
                    {
                        v.push_back(i);
                        return 1;
                    }
                }
            }
        }
    }

    return mem[pos][len][prev][flag];
}

int main()
{
    ll t, cs= 0, res;

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    scanf("%lld", &t);

    while(t--)
    {
        memset(mem, -1, sizeof mem);

        cin>>s;

        n= s.size();

        if(!dp(0, n, 0, 0))
            dp(0, n-1, 0, 0);

        reverse(v.begin(), v.end());

        res= 0;
        for(int i=0; i<v.size(); i++)
        {
            res*= 10;
            res+= (v[i]);
        }

        printf("Case #%lld: %lld\n", ++cs, res);

        v.clear();
    }

    return 0;
}
