/*
prob: Codejam17-1B
id: amlansaha
lang: C++
date: 2017-04-22
algo:
*/
#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long LLU;
typedef vector<int> VI;
typedef vector<long long> VLL;
typedef map<int, int> MAPII;
typedef map<string,int> MAPSI;
typedef pair<int, int> PII;
typedef pair<LL, LL> PLL;
typedef pair<double, double> PDD;

#define FOR(i,a,b) for(i=a;i<=b;i++)
#define ROF(i,a,b) for(i=a;i>=b;i--)
#define FR(i,n)    for(i=0;i<n;i++)
#define RF(i,n) for(i=n;i>0;i--)
#define CLR(a) memset ( a, 0, sizeof ( a ) )
#define RESET(a) memset ( a, -1, sizeof ( a ) )
#define PB(a)    push_back ( a )
#define X first
#define Y second

const int INF = 2000000009;
const int Max = 1000007;
const double PI = acos(-1.0);
const double EPS = 1e-8;

int main ()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    long long i, j, k, l, temp, t, d, n, m, caseno = 0, ans;
    string str;
    scanf ( "%lld", &t );

    while ( t-- )    {
        scanf ( "%lld %lld", &d, &n);
        double mxTime = 0;
        int mxPos = 0;
        vector<PII> inp;
        int pos,speed;
        FR(i,n) {
            scanf ( "%lld %lld", &pos, &speed);
            inp.push_back({d-pos,speed});
        }
        sort(inp.begin(),inp.end());
        for(i = 0; i < n; i++)  {
            pos = inp[i].first;
            speed = inp[i].second;
            double diff = pos;
            double timeNeeded = diff/speed;
            if(abs(mxTime-timeNeeded)<EPS)  {
                mxPos = pos;
            }
            else if(mxTime<timeNeeded)  {
                mxTime = timeNeeded;
                mxPos = pos;
            }
        }
        double ans = (d)/mxTime;
        printf ( "Case #%lld: %.10lf\n", ++caseno, ans);
    }
    return 0;
}

