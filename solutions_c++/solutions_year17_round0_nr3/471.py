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
#define SZ(a) (int)a.size()
#define MOD 1000000007
#define mod 1000000000
#define INF 1000000000
#define PB push_back
#define y0 kihrbdb
#define y1 ugvrrtgtrg
#define x first
#define y second


const int MAXV = 100*100;

map<LL,LL> F;
int t;
LL n, k;

int main()
{
    freopen("/Users/Taras/Downloads/C-large.in.txt","r",stdin);
    freopen("/Users/Taras/Downloads/out.txt","w",stdout);
    cin >> t;
    FOR (tst,0,t)
    {
        cout << "Case #"<<tst+1<<": ";
        cin >> n >> k;
        F.clear();
        F[-n] = 1;
        while (k > 1)
        {
            LL num = F.begin()->second;
           // cout << num<<" -> "<<k<<endl;
            if (num >= k) k = 1;
            else
            {
                k -= num;
                F[-(-F.begin()->first/2)] += num;
                F[-((-F.begin()->first-1)/2)] += num;
                F.erase(F.begin());
            }
        }
        cout << (-F.begin()->first)/2<<" "<<(-F.begin()->first-1)/2<<"\n";
    }
    
}


//cout << s.ind<<endl;
//for(set< Segm > :: iterator it = E.begin(); it != E.end(); it++)
//       cout << it->ind<<" ";
//cout << "end"<<endl;
//cout << E.size() <<" "<<s.ind<<" * "<<it->ind<<endl;