/*
prob: Codejam17
id: amlansaha
lang: C++
date: 2017-05-13
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

LL remainderFreq[5];

int countFor2()
{
    return remainderFreq[0] +  (remainderFreq[1]/2) + remainderFreq[1]%2;
}

int countFor3()
{
    int ret = remainderFreq[0];
    int temp = min(remainderFreq[1],remainderFreq[2]);
    ret+= temp;
    remainderFreq[1]-=temp;
    remainderFreq[2]-=temp;

    int leftOver = 1;
    if(remainderFreq[2])    {
        leftOver = 2;
    }
//    else if(remainderFreq[2])    {
//        temp = (remainderFreq[2]*2)/3;
//        ret+= temp;
//        if(temp%3)  ret++;
//    }


    temp = (remainderFreq[leftOver]);
    ret+= temp/3;

    if(temp%3)  ret++;
//    ret+= temp/3;
//    if(temp%3)  ret++;
    return ret;
}

int countFor4()
{
    return remainderFreq[0] +  (remainderFreq[1]/2) + remainderFreq[1]%2;
}


int main ()
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);

    LL i, j, k, l, temp, t, n, m, p,caseno = 0, ans;
    string str;
    scanf ( "%lld", &t );

    while ( t-- )    {
        CLR(remainderFreq);
        scanf ( "%lld %lld", &n, &p);
        FR(i,n) {
            scanf ( "%lld", &k);
            remainderFreq[k%p]++;
        }

        if(p==2)    ans = countFor2();
        if(p==3)    ans = countFor3();


        printf ( "Case #%lld: %lld\n", ++caseno,ans);
    }
    return 0;
}

