#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <cmath>
#include <string.h>
#include <cstdlib>
#include <ctime>
#include <assert.h>
#include <unordered_map>
typedef unsigned long long ll ;
using namespace std;
vector<ll> v;
void dfs(ll i,ll cur)
{
    if(i>=10||cur>=1000000000000000000)
    {
        if(cur<=1000000000000000000)
            v.push_back(cur);
        return ;
    }
    dfs(i,cur*10+i);
    dfs(i+1,cur);
}
int  main()
{
    std::cin.tie(0);
    std::ios::sync_with_stdio(false);
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    dfs(1,0);
    sort(v.begin(),v.end());
    int  t;
    ll x;
    cin >> t;
    for(int i =0;i<t;i++)
    {
        cin >> x;
        vector<ll> ::iterator it=upper_bound(v.begin(),v.end(),x);
        it--;
        cout <<"Case #"<< i+1<< ": "<< *it << endl;
    }
    return 0;
}
