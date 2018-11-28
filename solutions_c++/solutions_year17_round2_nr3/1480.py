#include <bits/stdc++.h>

#define mp make_pair
#define vi vector<int>
#define xx first
#define yy second
#define all(a) a.begin(), a.end()
#define vsort(v) sort(all(v))
#define UNIQUE(a)  sort(all(a)); a.erase(unique(all(a)), a.end())
#define clr(a,k) memset(a,k,sizeof a)
#define bclr(b) memset(b,false,sizeof b)
#define fr(i, a) for(i = 0; i < a; i++)
#define frr(i,a) for(i = a - 1; i >= 0, i--)
#define LL long long
#define ll long long
#define pb push_back
#define pii pair<int, int>
#define pll pair<ll, ll>
#define vll vector<long long>
///***** bit *****///
#define check_bit(a, b) (a&(1ll<<b))
#define set_bit(a, b) (a|(1<<b))
#define total_bit(a) __builtin_popcount(a)

///**** Max/Min********///

#define _max(aa, bb) (aa = max(aa, bb))
#define max2(aa, bb) max(aa, bb)
#define max3(aa, bb, cc) max(aa, max(bb, cc))
#define max4(aa, bb, cc, dd) max(max(aa, dd), max(bb, cc))
#define _min(aa, bb) (aa = min(aa, bb))
#define min2(aa, bb) min(aa, bb)
#define min3(aa, bb, cc) min(aa, min(bb, cc))
#define min4(aa, bb, cc, dd) min(min(aa, dd), min(bb, cc))


///******* File *********///

#define WRITE freopen("output.txt","w",stdout)
#define use_cin  ios_base::sync_with_stdio(0); cin.tie(0);
#define READ  freopen("C-small-attempt0.in","r",stdin)

///***** Input / Output *****///
#define s1(a) scanf("%d", &a)
#define s2(a, b) scanf("%d %d", &a, &b)
#define s3(a, b, c) scanf("%d %d %d", &a, &b, &c)
#define s4(a, b, c, d) scanf("%d %d %d %d", &a, &b, &c, &d)
#define p1(a) printf("%d", a)
#define p2(a, b) printf("%d %d", a, b)
#define p3(a, b, c) printf("%d %d %d", a, b, c)
#define nl printf("\n")
#define eps 1e-13
#define deb cout<<"I am here"<<endl
#define MOD 1000000007
#define MAX (lim+7)
#define INF 1001000000000000009ll
#define PI acos(-1.0)
#define piii pair<int, pii>
#define CLR(aa, nnn) for(int ii = 0; ii <= nnn; ii++) {aa[ii].clear();}

using namespace std;

///******* Template ********///

template <class T> inline T bigmod(T p,T e,T M)
{
    if(e==0)return 1;
    if(e%2==0)
    {
        T t=bigmod(p,e/2,M);
        return (t*t)%M;
    }
    return (bigmod(p,e-1,M)*p)%M;
}
template <class T> inline T gcd(T a,T b)
{
    if(b==0)return a;
    return gcd(b,a%b);
}
template <class T> inline T modinverse(T a,T M)
{
    return bigmod(a,M-2,M);
}

/**
return (a * b) % m;
where a, b, m <= 10^18
**/
template <class T> inline T multimod(T a, T b, T m)
{
    T ans = 0ll;
    a%=m, b%=m;
    while(b)
    {
        if(b&1ll) ans = m - ans > a?(ans + a): (ans + a - m);
        b >>= 1ll;
        a = (m - a)>a?a+a:a+a-m;
    }
    return (T)ans;
}

void sc(int &a)
{
    scanf("%d", &a);
}

void sc(ll &a)
{
    scanf("%lld", &a);
}

void sc(double &a)
{
    scanf("%lf", &a);
}

void sc(int &a, int &b)
{
    scanf("%d %d", &a, &b);
}

void sc(ll &a, ll &b)
{
    scanf("%lld %lld", &a, &b);
}

void sc(int &a, int &b, int &c)
{
    scanf("%d %d %d", &a, &b, &c);
}


void sc(int &a, int &b, ll &c)
{
    scanf("%d %d %lld", &a, &b, &c);
}


void sc(ll &a, ll &b, ll &c)
{
    scanf("%lld %lld %lld", &a, &b, &c);
}

void sc(string &str)
{
    cin>>str;
}


void sc(char *(str))
{
    scanf(" %s", str);
}

void sc(char &c)
{
    scanf(" %c", &c);
}


///****** fast scan ends here ***********///

//int dr[] = {-1, 0, 1, 0};
//int dc[] = {0, 1, 0, -1}; /// 4 sides
//int dr[] = {-1, -1, 0, 1, 1, 1, 0, -1};
//int dc[] = {0, 1, 1, 1, 0, -1, -1, -1}; /// 8 sides


#define LEN(a) strlen(a)
#define ull unsigned long long

#define nl printf("\n")

//#define MX 10000000000000000ll
#define MX (lim*4 + 10)
#define lim 100    /// 10^5


///***** Template ends here *****///
///********************* Code starts here ****************************


ll dpp[MAX][MAX];
ll arr[MAX][MAX];

int n;

ll determine(int s, int t)
{
    ll &ret = dpp[s][t];
    if(ret != -1) return ret;

    ret = arr[s][t];

    for(int i = 1; i <= n; i++)
    {
        if(i == s || i == t) continue;
        ret = min(ret, arr[s][i] + determine(i, t) );
    }

    return ret;
}



ll E[MAX];
ll S[MAX];

double dp[MAX];
bool vis[MAX];

ll sum[MAX];

ll dis(int i, int j)
{

//    cout<<i<<" "<<j<<" "<<sum[j-1] - sum[i-1]<<endl;
    ll ret = determine(i, j);
//    cout<<i<<" "<<j<<" "<<ret<<endl;
    return ret;
}

int st, ed;

double solve(int ind)
{
    if(ind == ed) return 0.0;
    double &ret = dp[ind];
    if(vis[ind]) return ret;
    vis[ind] = 1;
    ret = 10000000000000000.0;

    for(int i = 1; i <= n; i++)
    {
        ll d = dis(ind, i);
        if(d > E[ind]) continue;
        if(i == ind) continue;

        ret = min(ret, (double)d/ (double)S[ind] + solve(i));
    }
//    cout<<ind<<" "<<ret<<endl;

    return ret;
}


int main()
{
    READ;
    WRITE;
    int i, j, k, t;
    int cases = 1;
    int mn, mx, m;

    sc(t);

    while(t--)
    {
        sc(n, m);
        for(i = 1; i <= n; i++)
            cin>>E[i]>>S[i];
        for(i = 1; i <= n; i++)
        {
            for(j = 1; j <= n; j++)
            {
                cin>>arr[i][j];
                if(arr[i][j] == -1) arr[i][j] = 10000000000000000ll;
            }
        }

        for(k = 1; k <= n; k++)
        {
            for(i = 1; i <= n; i++)
            {
                for(j = 1; j <= n; j++)
                {
                    if(i == j) continue;

                    arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j]);
                }
            }
        }
        printf("Case #%d:", cases++);
        while(m--)
        {
            sc(st, ed);
            clr(dpp, -1ll);
            clr(vis, false);
            double ans = solve(st);
            printf(" %.12lf", ans+eps);
        }
        printf("\n");
    }


    return 0;
}

/*


3
3 1
2 3
2 4
4 4
-1 1 -1
-1 -1 1
-1 -1 -1
1 3
4 1
13 10
1 1000
10 8
5 5
-1 1 -1 -1
-1 -1 1 -1
-1 -1 -1 10
-1 -1 -1 -1
1 4
4 3
30 60
10 1000
12 5
20 1
-1 10 -1 31
10 -1 10 -1
-1 -1 -1 10
15 6 -1 -1
2 4
3 1
3 2





*/
