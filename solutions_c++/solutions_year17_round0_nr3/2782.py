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
typedef long long ll ;
using namespace std;

int  main()
{
    std::cin.tie(0);
    std::ios::sync_with_stdio(false);
    freopen("C-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    for(int countertest=0; countertest<t; countertest++)
    {
        map<ll,ll> maap;
        ll n,k,x,y,l,r;
        cin >> n>>k;
        maap[n]=1;
        map<ll,ll> ::iterator it=maap.end();
        it--;
        while(it->second<k)
        {
            x=it->first,y=it->second;
            l=r=x/2;
            if(x%2==0)
            {
                l--;
            }
            k-=y;
            maap.erase(it);
            maap[l]+=y;
            maap[r]+=y;
            it=maap.end();
            it--;
        }
        x=it->first,y=it->second;
        l=r=x/2;
        if(x%2==0)
        {
            l--;
        }
        cout << "Case #"<<countertest+1<< ": "<< r << " "<< l << endl;
    }
    return 0;
}
