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

int a[10];

int main()
{
    //READ("A-large.in");
    //WRITE("A-large.out");
    std::ios_base::sync_with_stdio(0);
    int cases, caseno=0, n, i, j, k, cnt, sum, p;

    cin >> cases;

    while(cases--)
    {
        cin >> n >> p;

        mem(a,0);

        FOR(i,1,n)
        {
            cin >> k;
            k = k % p;
            a[k]++;
        }

        cnt = a[0];

        if(p == 2)
            cnt += ((a[1]+1)/2);
        else if(p == 3)
        {
            k = min(a[1], a[2]);
            cnt += k;
            a[1] -= k;
            a[2] -= k;
            cnt += ((a[1]+2)/3);
            cnt += ((a[2]+2)/3);
        }
        else if(p == 4)
        {
            if((a[1]+a[2]*2+a[3]*3) % 4 != 0) cnt++;
            cnt += (a[2]/2);
            a[2] %= 2;
            k = min(a[1], a[3]);
            cnt += k;
            a[1] -= k;
            a[3] -= k;
            if(a[1])
            {
                if(a[2] && a[1] > 1)
                {
                    cnt++;
                    a[1] -= 2;
                }
                cnt += (a[1]/4);
            }
            else
            {
                if(a[2] && a[3] > 1)
                {
                    cnt++;
                    a[3] -= 2;
                }
                cnt += (a[3]/4);
            }
        }

        cout << "Case #" << ++caseno << ": " << cnt << NL;
    }

    return 0;
}


