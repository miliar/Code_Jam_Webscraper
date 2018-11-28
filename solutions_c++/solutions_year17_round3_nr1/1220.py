#pragma comment(linker,"/STACK:268435456")
#include <iostream>
#include <iomanip>
#include <fstream>
#include <set>
#include <algorithm>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <cmath>
#include <climits>
#include <cstring>
#include <string>
#include <sstream>
#include <bitset>
#include <iterator>
#include <list>
#include <ctime>
#include <functional>
#include <numeric>
#include <cassert>
//#include <unordered_map>

#define FR(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,c,n) for(int (i)=(c);(i)<(n);(i)++)
#define REP(it,v,cont) for((cont)::iterator (it)=(v).begin();(it)!=(v).end();++(it))
#define CLR(a,c) memset((a),(c),sizeof (a))
#define ALL(v) (v).begin(),(v).end()
#define VCPRINT(v) for(int iii = 0;iii < (v).size();iii++) cout<<(v)[iii]<<" ";cout<<endl;
#define SETPRINT(v,cont) for((cont)::iterator iiit = (v).begin();iiit != (v).end();iiit++) cout<<*iiit<<" ";cout<<endl;

bool ascending (int i,int j) { return (i<j); }
bool descending (int i,int j) { return (i>j); }

typedef long long ll;
typedef unsigned long long ull;
#define PII pair<int,int>
#define PLL pair<long long,long long>
#define PULI pair<unsigned long long,int>
#define PIL pair<int,long long>
#define PSI pair<string,int>
#define PSS pair<string,string>
#define PDD pair<double,double>
#define PIB pair<int,bool>
typedef long double ld;
#define PLI pair<ll,int>
#define PLDD pair<ld,ld>

using namespace std;

int n, k;

PLL Pancake[1100];
ll dp[1100][1100];



ll f(int i, int j)
{
    if(j==0) return 0;
    if(i==n) return 0;

    if(dp[i][j]!= -1) return dp[i][j];

    ll num = 0;
    if(j==1)
        num = f(i+1, j-1) + 2*Pancake[i].first*Pancake[i].second + Pancake[i].first*Pancake[i].first;
    else
        num = f(i+1, j-1) + 2*Pancake[i].first*Pancake[i].second;
    return dp[i][j]=max(f(i+1, j), num);
}


long double PI = (ld)4.0*atan((ld)1.0);

int main()
{
    ifstream cin("a.in");
    ofstream cout("a.out");
    ios::sync_with_stdio(0);
    int T;cin>>T;
    FOR(_,1,T+1)
    {
        CLR(dp, 255);
        cout<<"Case #"<<_<<": ";
        cin>>n>>k;
        FR(i, n) cin>>Pancake[i].first>>Pancake[i].second;
        sort(Pancake, Pancake+n);

        cout<<setprecision(13)<<fixed;
        cout<<PI*f(0, k)<<endl;
    }
}