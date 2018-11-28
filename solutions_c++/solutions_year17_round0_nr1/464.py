//#pragma comment(linker,"/STACK:16777216") /*16Mb*/
#pragma comment(linker,"/STACK:33554432") /*32Mb*/

#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <stack>
#include <cmath>
#include <list>
#include <iomanip>
#include <set>
#include <map>
#include <sstream>
#include <fstream>
#include <sstream>
#include <iterator>
#include <unordered_map>
using namespace std;


typedef  long long LL;
typedef  unsigned long long ULL;
typedef  long double LD;
typedef  pair<long long, long long> PII;
typedef vector<int> VI;

#define FOR(i,a,b) for(int (i)=(a);i<(b);++(i))
#define RFOR(i,a,b) for(int (i)=(a)-1;(i)>=(b);--(i))
#define MP make_pair
#define SZ(a) a.size()
#define MOD 1000000007
#define mod 1000000000
#define INF 1000000000
#define PB push_back
#define y0 kihrbdb
#define y1 ugvrrtgtrg
#define x first
#define y second


const int MAXV = 100*100;

int n, m;
string s;
int t;

int main()
{
    freopen("/Users/Taras/Downloads/A-large.in.txt","r",stdin);
    freopen("/Users/Taras/Downloads/out.txt","w",stdout);
    cin >> t;
    FOR (tst,0,t)
    {
        int k;
        cin >> s >> k;
        int ans = 0;
        FOR (i,0,s.size())
        if (s[i] == '-')
        {
            ans++;
            if (i+k > s.size()) ans = SZ(s)+1;
            else
                FOR (j,i,i+k)
                if (s[j] == '-') s[j] = '+';
                else s[j] = '-';
        }
        printf("Case #%d: ",tst+1);
        if (ans <= s.size()) cout << ans << "\n";
        else cout << "IMPOSSIBLE\n";
    }
    
}


//cout << s.ind<<endl;
//for(set< Segm > :: iterator it = E.begin(); it != E.end(); it++)
//       cout << it->ind<<" ";
//cout << "end"<<endl;
//cout << E.size() <<" "<<s.ind<<" * "<<it->ind<<endl;