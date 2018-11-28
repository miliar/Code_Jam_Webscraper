/*
deepansh_946
*/
#include <bits/stdc++.h>
#define gc getchar
#define pc putchar
#define lli unsigned long long int
#define MOD 1000000007
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
#define pd(x) printf("%d",x)
#define plld(x) printf("%lld",x)
#define ss(x) scanf("%s",&x)
#define ps(x) printf("%s",x)
#define code int t; cin>>t; while(t--)
#define gcd __gcd
using namespace std;

lli f(string s)
{
    lli ans = 0 , i = 0;
    while(s[i]!='\0')
    {
        ans = ans*10 + ((int)s[i]-48);
        i++;
    }
    return ans;
}

int main()
{
    freopen("in.in" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);
    int t;
    sd(t);
    for(int i=1;i<=t;i++)
    {
        string s;
        cin >> s;
        if(s.size() == 1)
        {
            cout << "Case #" << i << ": " << s << endl;
            continue;
        }
        bool flag = false;
        for(int i=1;i<s.size();i++)
        {
            if(s[i] < s[i-1])
            {
                flag = true;
                break;
            }
        }
        if(flag == false)
        {
            cout << "Case #" << i << ": " << f(s) << endl;
        }
        else
        {
            for(int i=0;i<s.size()-1;i++)
            {
                if(s[i]>=s[i+1])
                {
                    s[i]--;
                    for(int j=i+1;j<s.size();j++)
                        s[j] = '9';
                    break;
                }
            }
            cout << "Case #" << i << ": " << f(s) << endl;
        }
    }
    return 0;
}
