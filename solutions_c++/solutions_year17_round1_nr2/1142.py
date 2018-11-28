#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<math.h>
#include<map>
#include<vector>
#include<string>
#include<set>
#include<queue>
#define MP(x,y) make_pair(x,y)
#define clr(x,y) memset(x,y,sizeof(x))
#define forn(i,n) for(int i=0;i<n;i++)
#define sqr(x) ((x)*(x))
#define MAX(a,b) if(a<b) a=b;
#define ll long long
using namespace std;

int n, p;
int a[100], b[100];
vector<pair<int, int> > v[100];

bool cmp(pair<int, int> a, pair<int, int> b)
{
    if(a.first == b.first) return a.second < b.second;
    else return a.first < b.first;
}
int main() {
    //freopen("in","r",stdin);
    freopen("/home/zyc/Downloads/in","r",stdin);
    freopen("/home/zyc/Downloads/out","w",stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++)
    {
        scanf("%d%d", &n, &p);
        for(int i = 0; i < n ;i++) scanf("%d", &a[i]);
        for(int i = 0; i < n; i++)
        {
            v[i].clear();
            for(int j = 0; j < p; j++)
            {
                int w;
                scanf("%d", &w);
                double lx = w / (a[i] * 1.1);
                double rx = w / (a[i] * 0.9);
                int l, r;
                r = int(rx); 
                l = int(lx);
                if(l < lx) l += 1;
                if(r >= l) v[i].push_back(MP(l, r));
                //printf("%d %d\n", l, r);
            }
        }
        for(int i = 0; i < n; i++) sort(v[i].begin(), v[i].end(), cmp); 
        for(int i = 0; i < n; i++) b[i] = 0;
        
        int res = 0;
        while(true)
        {
            bool flag;
            flag = false;
            for(int i = 0; i < n; i++) 
                if(b[i] == (int)v[i].size()) 
                    flag = true;
            if(flag) break;

            int l_maxx = v[0][b[0]].first, r_minn = v[0][b[0]].second;
            flag = true;
            for(int i = 0; i < n; i++)
            {
                if(v[i][b[i]].first > l_maxx) l_maxx = v[i][b[i]].first;
                if(v[i][b[i]].second < r_minn) r_minn = v[i][b[i]].second;
            }
            if(l_maxx <= r_minn)
            {
                res += 1;
                for(int i = 0; i < n; i++) b[i] += 1;
            }
            else
            {
                for(int i = 0; i < n; i++) if(v[i][b[i]].second == r_minn) b[i] += 1;
            }

        }
        printf("Case #%d: %d\n", cas, res);
    }
    return 0;
}
