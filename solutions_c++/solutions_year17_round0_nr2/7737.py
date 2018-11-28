/*
prob: GCJ17-QB
id: amlansaha
lang: C++
date: 2017-04-09
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

int main ()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    LL i, j, k, l, temp, t, n, m, caseno = 0, ans;
    string str;
    scanf ( "%lld", &t );

    while ( t-- )    {
        cin>>str;
        LL l = str.size();
        for(i = l-1; i >0; i--)  {
            if(str[i-1]>str[i]) {
                str[i-1]--;
                for(j = i; j <l; j++)   str[j] = '9';
            }
        }
        ans = 0;
        FR(i,l) {
            ans*=10;
            ans+= str[i]-'0';
        }
        printf ( "Case #%lld: %lld\n", ++caseno,ans);
    }
    return 0;
}

