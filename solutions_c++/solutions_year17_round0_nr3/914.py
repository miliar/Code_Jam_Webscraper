#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <math.h>
#include <cstdlib>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define _CRT_SECURE_NO_WARNINGS
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
const double pi=acos(-1.0);
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}
typedef pair<int,int> ipair;
typedef map<string, int> simp;
#define sz(A) ((int)A.size())
#define MP(A,B) make_pair(A,B)
#define rep(i,b) for(int i=0;i<b;i++)
#define For(i,a,b) for(int i=a;i<b;i++)
template<class T> inline void Swap(T &a,T &b){T c=a;a=b;b=c;}
#define Sort(v) sort((v).begin(), (v).end())
#define Uni(v) Sort(v),(v).erase(unique((v).begin(), (v).end()), (v).end())
#define cl(a,b) memset(a,b,sizeof(a))

const int oo=1000000;

#pragma warning(disable:4996)

#define QX "C"

// get 2^k, where 2^k <= n < 2^(k+1)
// e.g., [1] => return 1, [2-3] => 2, [4-7] => 4, [8-15] => 8, ...
long long prev(long long n) {
    if (n <= 1) {
        return 0;
    }
    long long ret = 1;
    while ((ret << 1) <= n) {
        ret <<= 1;
    }
    return ret;
}

int main()
{
//	freopen(QX ".txt","r",stdin);
//	freopen(QX "-small-1-attempt0.in","r",stdin);freopen(QX "-small-1-attempt0.out","w",stdout);
//	freopen(QX "-small-attempt1.in","r",stdin);freopen(QX "-small-attempt1.out","w",stdout);
//	freopen(QX "-small-2-attempt0.in","r",stdin);freopen(QX "-small-2-attempt0.out","w",stdout);
	freopen(QX "-large.in","r",stdin);freopen(QX "-large.out","w",stdout);
//	freopen(QX "-large-practice.in","r",stdin);freopen(QX "-large-practice.out","w",stdout);

    int T=0;
	scanf("%d",&T);
    for (int caseId=1;caseId<=T;caseId++)
	{
        // input
        long long N, K;
        cin>>N>>K;
        long long r = N;
        if (K > 1) {
            long long p = prev(K);
            N -= p - 1;
            long long base = N / p;
            long long extra = N - base * p;
            long long rest = K - p + 1;
            r = rest > extra ? base : base + 1;
        }
        if (r == 0) {
            cout << "!!!r == 0" << endl;
        }
        cout << "Case #" << caseId << ": " << r / 2 << " " << (r - 1) / 2 << endl;
	}
    return 0;
}
