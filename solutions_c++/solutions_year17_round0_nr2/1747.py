#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i= a; i<= b; i++)
#define FORD(i,a,b) for(int i= a; i>= b; i--)
#define For(i,a,b) for(int i= a; i< b; i++)
#define Ford(i,a,b) for(int i= a; i> b; i--)
#define FORE(i,v) for (__typeof((v).begin()) i=(v).begin();i!=(v).end();i++)
#define Fill(s,a) memset(s,a,sizeof(s))
#define pb push_back
#define mp make_pair
#define ALL(x) (x).begin(),(x).end()
#define fi first
#define se second

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef unsigned long long ull;

const int N = 100100;

int tests, a[N], cnt;
ll n;

void process(int test)
{
    Fill(a,0);
    cnt = 0;
    while (n != 0)
    {
        a[++cnt] = n % 10;
        n/= 10;
    }
    bool finded = true;
    FORD(i,cnt-1,1)
        if (a[i] < a[i+1])
        {
            int j = i;
            while (j < cnt && a[j] < a[j+1])
            {
                FORD(k,j,0) a[k] = 9;
                a[++j]--;
            }
        }
    FOR(i,1,cnt)
        if (a[i] < 0) finded = false;
    if (a[cnt] == 0) finded = false;
    cout << "Case #" << test << ": ";
    if (!finded)
    {
        FOR(i,1,cnt-1) cout << 9;
        cout << endl;
    }
    else
    {
        FORD(i,cnt,1) cout << a[i];
        cout << endl;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    freopen("B2.in","r",stdin);
    freopen("B2.out","w",stdout);
    cin >> tests;
    FOR(t,1,tests)
    {
        cin >> n;
        process(t);
    }
    return 0;
}

