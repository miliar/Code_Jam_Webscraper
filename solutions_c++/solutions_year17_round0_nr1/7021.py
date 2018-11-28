#include<bits/stdc++.h>
#define ll long long
#define fin(x) scanf("%lld",&x)
#define fout(x) printf("%lld\n",x)
#define pll pair<ll,ll>
#define mp(x,y) make_pair(x,y)
#define cases int t;  scanf("%d",&t);   while(t--)
#define MOD 1000000007
#define MAXN 1234567
#define read() freopen("input.txt","r",stdin)
#define write() freopen("dede.txt","w",stdout)

using namespace std;

int main()
{
    read();
    write();
    ll T = 0;
    cases
    {
        T++;
        string str;
        ll k, len, kount = 0, ptr, j;
        cin >> str >> k;
        len = str.length();
        for(ll i = 0; i < len; i++)
        {
            if(str[i] == '-')
            {
                ptr = i;
                j = (ptr + k) - 1;
                if(j < len)
                {
                    kount++;
                    while(ptr <= j)
                    {
                        if(str[ptr] == '-')   str[ptr] = '+';
                        else if(str[ptr] == '+')  str[ptr] = '-';
                        ptr++;
                    }
                }
            }
        }
        bool ok = true;
        for(auto it : str)
        {
            if(it == '-')
            {
                ok = false;
                break;
            }
        }
        if(ok)
            printf("Case #%lld: %lld\n", T, kount);
        else
            printf("Case #%lld: IMPOSSIBLE\n", T);
    }
    return 0;
}
