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
string s;
void solve(int k)
{
    ll counter=0;
    for(int i =0;i<s.size()-k+1;i++)
    {
        if(s[i]=='-')
        {
            counter++;
            for(int h=i;h<i+k;h++)
            {
                if(s[h]=='-')
                    s[h]='+';
                else
                    s[h]='-';
            }
        }
    }
    for(int i =0;i<s.size();i++)
        if(s[i]=='-')
    {
        cout <<"IMPOSSIBLE"<<endl;
        return ;
    }
    cout << counter << endl;
}
int  main()
{
    std::cin.tie(0);
    std::ios::sync_with_stdio(false);
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t,k;
    cin >> t;
    for(int i =0;i<t;i++)
    {
        cin >> s>>k;
        cout << "Case #"<<i+1<<": ";
        solve(k);
    }
    return 0;
}
