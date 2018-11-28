#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define loop(x, n) for(int x = 0; x < n; ++ x)
long long GCD(long long  n1, long long n2)
{
    if (n2 != 0)
        return GCD(n2, n1 % n2);
    else
        return n1;
}
long long LCM(long long  n1, long long n2)
{
    long long m;
    m=n1*n2/GCD(n1,n2);
    return m;
}
unsigned long long choose(unsigned long long n, unsigned long long k)
{
    if (k > n)
    {
        return 0;
    }
    unsigned long long r = 1;
    for (unsigned long long d = 1; d <= k; ++d)
    {
        r *= n--;
        r /= d;
    }
    return r;
}
bool isprime(int x)
{
    if(x==1)
        return 0;
    for(int i=2; i*i<x; i++)
    {
        if(x%i==0)
            return 0;
    }
    return 1;
}

int main()
{
    freopen("A-large.in", "r", stdin);
freopen("o.out", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    /*********************/
    int t,k,num=1;string s;
    cin>>t;
    while(t--)
    {
        cin>>s;
        cin>>k;
        long long c=0;
        for(int i=0;i<s.size()-k+1;i++)
        {
            if(s[i]=='-')
            {
                c++;
                for(int j=i;j<i+k;j++)
                {
                    if(s[j]=='+')
                        s[j]='-';
                    else
                        s[j]='+';
                }
            }
        }
        bool da=0;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='-')
            {
                da=1;
                break;
            }
        }
        cout<<"Case #"<<num<<": ";
        if(da)
        {
           cout<<"IMPOSSIBLE"<<endl;
        }
        else
            cout<<c<<endl;
        num++;
    }
    return 0;
}
/*
3
---+-++- 3
+++++ 4
-+-+- 4
*/
