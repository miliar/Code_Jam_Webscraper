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

string s;
int t;

void call(string s)
{
    int pos = -1;
    FOR (i,1,s.size())
    {
        if (s[i] < s[i-1]) pos = i;
    }
    if (pos == -1) {cout << s; return;}
    string s1 = s.substr(0,pos);
    string s2 = s.substr(pos,s.size());
    pos = SZ(s1)-1;
    while (s1[pos] == '0') s1[pos] = 9, pos--;
    s1[pos]--;
    if (s1[0] == '0') s1 = s1.substr(1,SZ(s1)-1);
    call(s1);
    FOR (i,0,s2.size()) cout << "9";
}

int main()
{
    freopen("/Users/Taras/Downloads/B-large.in.txt","r",stdin);
    freopen("/Users/Taras/Downloads/out.txt","w",stdout);
    cin >> t;
    FOR (tst,0,t)
    {
        cout << "Case #"<<tst+1<<": ";
        cin >> s;
        call(s);
        cout << "\n";
    }
    
}


//cout << s.ind<<endl;
//for(set< Segm > :: iterator it = E.begin(); it != E.end(); it++)
//       cout << it->ind<<" ";
//cout << "end"<<endl;
//cout << E.size() <<" "<<s.ind<<" * "<<it->ind<<endl;