#include <bits/stdc++.h>
using namespace std ;

#define geti(a) scanf("%d", &a) // i.e. get_int
#define getii(a, b) scanf("%d %d", &a, &b)
#define getiii(a, b, c) scanf("%d %d %d", &a, &b, &c)

#define getl(a) scanf("%lld", &a) // i.e. get_long_long_int
#define getll(a, b) scanf("%lld %lld", &a, &b)
#define getlll(a, b, c) scanf("%lld %lld %lld", &a, &b, &c)

#define gets(a) scanf("%s", &a) // i.e. get_string
#define getss(a, b) scanf("%s %s", &a, &b)

#define printi(a) printf("%d\n", a)
#define printl(a) printf("%lld\n", a)
#define printii(a, b) printf("%d %d\n", a, b)
#define printiii(a, b, c) printf("%d %d %d\n", a, b, c)
#define printll(a, b) printf("%lld %lld\n", a, b)
#define prints(a) printf("%s\n", a)
#define printss(a, b) printf("%s %s\n", a, b)
#define printline printf("\n")

#define ll long long int
#define pb push_back

#define FAST_IO ios_base::sync_with_stdio(0) ; cin.tie(0)
#define SET(list, val) memset(list, val, sizeof(list))

#define pi pair<int, int>
#define pl pair<ll, ll>
#define pii pair<int, pi>
#define f first
#define s second

#define FOR(n) for(int i = 0; i < n; i++) // From 0 to n-1
#define FORA(a, b) for(int i = (a); i <= (b); i++) // From a to b to increasing
#define DFOR(n) for(int i = n; i >= 0; i--) // From n to 0
#define DFORA(a, b) for(int i = (a); i >= (b); i--) // From a to b decrementing

#define N (int)1e6+5
#define INF 10000000000001
const int inf = 1e9 + 1 ;
const int mod = 1e9 + 7 ;

int a[N];

int getLeft(int i)
{
    int dist = 0; i--;
    while(true)
    {
        if(a[i] == 0)
            dist++;
        else
            break ;
        i--;
    }
    return dist ;
}

int getRight(int i)
{
    int dist = 0; i++;
    while(true)
    {
        if(a[i] == 0)
            dist++;
        else
            break ;
        i++;
    }
    return dist ;
}

pi solve(int n, int k)
{
    priority_queue<pii> heap ;
    int num ;
    heap.push({n, {1, n}});
    FOR(k)
    {
        pii top = heap.top();
        int l = top.s.f , r = top.s.s ;
        heap.pop();

        if(l == r)
        {
            num = l; a[l] = 1; continue ;
        }

        num = (l+r)/2 ;
        a[num] = 1;

        if(l <= num-1)
            heap.push({num - l, {l, num - 1}});

        if(num+1 <= r)
            heap.push({r - num, {num+1, r}});
    }
    int ls = getLeft(num);
    int rs = getRight(num);

    return { max(ls, rs), min(ls, rs) };
}

int main()
{
    ofstream fout("C-small-2-attempt3.out");
    ifstream fin("C-small-2-attempt3.in");

    int t; fin >> t ;
    for(int j = 1; j <= t; j++)
    {
        int n, k ;
        fin >> n >> k ;
        /*
        if(k > n/2)
        {
            cout << "Input: " << n << " " << k ;
            cout << "\nCase #" << j << ": " << 0 << " " << 0 << endl << endl ;

            fout << "Case #" << j << ": " << 0 << " " << 0 << endl ;
            continue ;
        }
        */
        FOR(n+3)
            a[i] = 0;

        a[0] = 1 ; a[n+1] = 1;

        pi ans = solve(n, k) ;

        cout << "Input: " << n << " " << k ;
        cout << "\nCase #" << j << ": " << ans.f << " " << ans.s << endl << endl ;

        fout << "Case #" << j << ": " << ans.f << " " << ans.s << endl ;
    }
    return 0;
}


