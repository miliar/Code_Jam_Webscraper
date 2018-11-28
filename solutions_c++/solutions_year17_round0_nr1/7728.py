/*
prob: GCJ17-Q-A
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

int findMinStep(string str, int k, char target)
{
    int ret = 0;
    int l = str.size();

    for(int i = 0; i < l; i++)  {
        if(str[i]==target)  continue;
        for(int j = 0; j < k; j++)  {
            int m = i+j;
            if(m>=l)    return INF;
            if(str[m]=='+') str[m]='-';
            else    str[m]='+';
        }
        ret++;
    }
    return ret;
}

int main ()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int i, j, k, l, temp, t, n, m, caseno = 0, ans;
    string str, s2;
    scanf ( "%d", &t );

    while ( t-- )    {
        cin>>str>>k;
        s2=str;
        ans = findMinStep(str,k,'+');
//        ans = min(ans, findMinStep(str,k,'+'));
        reverse(str.begin(),str.end());
        ans = min(ans, findMinStep(str,k,'+'));
//        ans = min(ans, findMinStep(str,k,'-'));

        printf ( "Case #%d: ", ++caseno);
        if(ans==INF)    cout<<"IMPOSSIBLE"<<endl;
        else    cout<<ans<<endl;
    }
    return 0;
}
