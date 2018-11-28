#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <list>
#include <queue>
#include <deque>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <limits>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<long long> vll;

template <typename T>
string tostring ( T value )
{
    ostringstream ss;
    ss << value;
    return ss.str();
}

template <typename T>
T strtonum ( const string &Text )
{
    istringstream ss(Text);
    T result;
    return ss >> result ? result : 0;
}
//----------------------------------

//==================================
void solve()
{
    int numCases = 1;
    cin >> numCases;

    for ( int ncase=1; ncase <= numCases; ncase++ )
    {
        //===== start case
        ll k, n;
        cin >> n >> k;
        map<ll,ll> mymap;
        queue<ll> q;
        mymap.insert(make_pair(n,1));
        q.push(n);
        while (!q.empty())
        {
            ll m = q.front();
            q.pop();
            m--;
            ll p=m/2;
            if (m%2==0)
            {
                if (p>0 && mymap.find(p)!=mymap.end())
                {
                    mymap[p] += mymap[m+1]*2;
                }
                else if (p>0)
                {
                    mymap[p] = mymap[m+1]*2;
                    q.push(p);
                }
            }
            else
            {
                if (p>0 && mymap.find(p)!=mymap.end())
                {
                    mymap[p] += mymap[m+1];
                }
                else if (p>0)
                {
                    mymap[p] = mymap[m+1];
                    q.push(p);
                }
                if (mymap.find(p+1)!=mymap.end())
                {
                    mymap[p+1] += mymap[m+1];
                }
                else
                {
                    mymap[p+1] = mymap[m+1];
                    q.push(p+1);
                }
            }
        }

        ll sum=0;
        for (map<ll,ll>::iterator it=mymap.begin(); it!=mymap.end(); it++)
        {
        }
        vector<pair<ll,ll>> vp;
        ll ans1, ans2;
        for (map<ll,ll>::reverse_iterator it=mymap.rbegin(); it!=mymap.rend(); it++)
        {
            sum += it->second;
            //cout << it->first << " " << it->second << " sum=" << sum << endl;
            if (k<=sum)
            {
                ll x = it->first - 1;
                ans2 = x / 2;
                if (x%2==1)
                    ans1=ans2+1;
                else
                    ans1=ans2;
                break;
            }
        }

        cout << "Case #" << ncase << ": ";
        cout << ans1 << " " << ans2 << endl;

        //===== end case

    }
}

int main()
{
#ifdef CCQTEST
#include "HRCPP1.h"
#endif
    solve();
#ifdef CCQTEST
#include "HRCPP2.h"
#endif
    return 0;
}
