#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
#define sll(x) scanf("%lld",&x)
#define pll(x) printf("%lld\n",x)
#define mp make_pair
#define pb push_back
#define fr first
#define se second

int main()
    {
    ll t,i,j;
    sll(t);
    for(j=1;j<=t;j++)
        {
        bool one=false,ok=false;
        char x;
        string s,a;
        cin >> s;
        for(i=0;i<s.length()-1;i++)
            {
            if(s[i]>s[i+1])
                {
                if(s[i]=='1')
                    {
                    one=true;
                }
                x=s[i]-1;
                ok=true;
                break;
            }
            a.pb(s[i]);
        }
        if(one)
            {
            a.clear();
            for(i=0;i<s.length()-1;i++)
                {
                a.pb('9');
            }
        }
        else if(ok)
            {
            while(a.length() && a.back()>x)
                {
                a.pop_back();
            }
            a.pb(x);
            while(a.length()<s.length())
                {
                a.pb('9');
            }
        }
        else
            {
            a.clear();
            a.append(s);
        }
        cout << "Case #" << j << ": " << a << endl;
    }
    return 0;
}
