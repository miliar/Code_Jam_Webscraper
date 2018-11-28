#include <bits/stdc++.h>
using namespace std;

#define LL long long
#define NL '\n'
#define xx first
#define yy second
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define si(x) scanf("%d",&x)
#define sl(x) scanf("%I64d",&x)
#define sd(x) scanf("%lf",&x)
#define ss(x) scanf("%s",x)
#define mem(a,b) memset(a,b,sizeof(a))
#define FOR(i,j,k) for(i=j;i<=k;i++)
#define REV(i,j,k) for(i=j;i>=k;i--)
#define READ(f) freopen(f,"r",stdin)
#define WRITE(f) freopen(f,"w",stdout)
#define cnd tree[idx]
#define lnd tree[idx*2]
#define rnd tree[(idx*2)+1]
#define lndp (idx*2),(b),((b+e)/2)
#define rndp (idx*2+1),((b+e)/2+1),(e)
#define pi 2.0*acos(0.0)
#define MOD 1000000007
#define MAX 100005

bool check(string s)
{
    char ch = '0';
    for(int i = 0; i < (int)s.size(); i++)
    {
        if(s[i] < ch) return 0;
        ch = s[i];
    }
    return 1;
}

int main()
{
    //READ("B-large.in");
    //WRITE("B-large.out");
    std::ios_base::sync_with_stdio(0);
    int cases, caseno=0, i, j, n;
    LL sum, k, d, p, cnt;
    string s;

    cin >> cases;

    while(cases--)
    {
        cin >> s;

        n = s.size();

        if(check(s))
        {
            cout << "Case #" << ++caseno << ": " << s << NL;
            continue;
        }

        sum = 0;
        p = 0;
        char ch = '0';

        FOR(i,0,n-1)
        {
            if(s[i] < ch) break;
            if(s[i] > ch)
            {
                cnt = p * 10LL + (s[i]-'1');
                FOR(j,i+1,n-1) cnt = (cnt * 10LL) + 9;
                sum = max(sum, cnt);
            }
            p = p * 10LL + (s[i]-'0');
            ch = max(ch, s[i]);
        }

        cout << "Case #" << ++caseno << ": " << sum << NL;
    }

    return 0;
}


