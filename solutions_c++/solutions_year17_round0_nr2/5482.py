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

vector<ll> V;


void f(int n, int i, int count, ll num)
{
    if(i == 10) {
        if(count == n) V.push_back(num);
        return;
    }

    for(int j = 0; j <= n-count;j++)
    {
        ll cur = num;
        FR(k, j) cur = cur * 10LL + i;
        f(n, i+1, count+j, cur);
    }
}



int main()
{
    for(int i = 1; i <= 18; i++)
        f(i, 1, 0, 0);
    sort(V.begin(), V.end());
    ifstream cin("a.in");
    ofstream cout("a.out");
    ios::sync_with_stdio(0);
    int T;cin>>T;
    FOR(_,1,T+1)
    {
        cout<<"Case #"<<_<<": ";
        ll x;cin>>x;
        int index = lower_bound(V.begin(), V.end(), x) - V.begin();
        if(V[index] == x) cout<<x<<endl;
        else cout<<V[index-1]<<endl;
    }
}