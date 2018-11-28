#include<iostream>
#include<vector>
#include <cmath>
#include<algorithm>
#include <map>
#include <cstdio>
using namespace std;

map<int, vector< vector<int> > > mp;

void init()
{
    /**2**/
    vector< vector<int> >ret;
    vector<int> temp;
    temp.push_back(1);
    temp.push_back(1);
    ret.push_back(temp);
    temp.clear();
    mp[2] = ret;

    /**3**/
    ret.clear();

    temp.push_back(1);
    temp.push_back(2);
    ret.push_back(temp);
    temp.clear();

    temp.push_back(2);
    temp.push_back(2);
    temp.push_back(2);
    ret.push_back(temp);
    temp.clear();

    temp.push_back(1);
    temp.push_back(1);
    temp.push_back(1);
    ret.push_back(temp);
    temp.clear();
    mp[3] = ret;

    /**4**/
    ret.clear();

    temp.push_back(1);
    temp.push_back(3);
    ret.push_back(temp);
    temp.clear();

    temp.push_back(2);
    temp.push_back(2);
    ret.push_back(temp);
    temp.clear();

    temp.push_back(2);
    temp.push_back(3);
    temp.push_back(3);
    ret.push_back(temp);
    temp.clear();

    temp.push_back(1);
    temp.push_back(1);
    temp.push_back(1);
    temp.push_back(1);
    ret.push_back(temp);
    temp.clear();

    temp.push_back(3);
    temp.push_back(3);
    temp.push_back(3);
    temp.push_back(3);
    ret.push_back(temp);
    temp.clear();
    mp[4] = ret;

}

const int N = 1000;

int n, p;
int G[N];

int solve()
{
    vector<int>cnt(p, 0);
    for(int i=0; i<n; i++)
    {
        cnt[G[i]] += 1;
    }
    vector< vector<int> > key = mp[p];
    int ret = 0;
    ret += cnt[0];
    for(int i=0; i<key.size(); i++)
    {
        map<int, int> hh;
        for(int j=0; j<key[i].size(); j++)
        {
            int value = key[i][j];
            if(hh.count(value) == 0)
            {
                hh[value] = 0;
            }
            hh[value] += 1;
        }
        int tt = 1<<29;
        for(map<int, int>::iterator it=hh.begin(); it!=hh.end(); it++)
        {
            int a = it->first;
            int b = it->second;
            tt = min(tt, cnt[a]/b);
        }
        ret += tt;
        for(map<int, int>::iterator it=hh.begin(); it!=hh.end(); it++)
        {
            int a = it->first;
            int b = it->second;
            cnt[a] -= tt*b;
        }
    }
    for(int i=1; i<cnt.size(); i++)
    {
        if(cnt[i]>0)
        {
            ret += 1;
            break;
        }
    }
    return ret;
}

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("ans.txt", "w", stdout);
    init();
    int T;
    scanf("%d", &T);
    for(int t=1; t<=T; t++)
    {
        scanf("%d%d", &n, &p);
        for(int i=0; i<n; i++)
        {
            scanf("%d", &G[i]);
            G[i] %= p;
        }
        int ans = solve();
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
