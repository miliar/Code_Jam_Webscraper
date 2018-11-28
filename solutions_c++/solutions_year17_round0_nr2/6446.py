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
bool sort_(string s)
{
    for(int i=0; i<s.size(); i++)
    {
        for(int j=i+1; j<s.size(); j++)
        {
            if(s[i]>s[j])
                return 0;
        }
    }
    return 1;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.out","w",stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    /*********************/
    int t,num=1;
    cin>>t;string s;
    unsigned long long x;long long sum;stringstream ss;
    while(t--)
    {
        sum=0;
        cin>>s;
        while(!sort_(s))
        {
            unsigned long long a;
            ss.clear();
            sum++;
            s.erase(s.size()-1,1);
            ss<<s;
            ss>>a;
            a--;
            s.clear();
            ss.clear();
            ss<<a;
            ss>>s;
        }
        if(s=="0")
            s.clear();
        cout<<"Case #"<<num<<": "<<s;
        for(int i=0;i<sum;i++)
            cout<<9;
        cout<<endl;
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
