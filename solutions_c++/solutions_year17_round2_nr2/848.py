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
#include <cstdlib>
#include <cstring>
#include <unordered_map>
using namespace std;
#define ALL(a) (a).begin(), (a).end()
#define SZ(a) (int)(a).size()
#define FOR(i,s,n) for(int i=(s);i<(n);++i)
#define REP(i,n) FOR(i,0,(n))
#define PB(x) push_back((x))
#define CLR(a,v) memset((a),(v),sizeof((a)))
typedef long long ll;

char res[1010];

void solve()
{
    int n,R,O,Y,G,B,V;
    scanf("%d %d %d %d %d %d %d", &n,&R,&O,&Y,&G,&B,&V);

    if(G>R||V>Y||O>B)
    {
        printf("IMPOSSIBLE\n");
        return;
    }

    int cnt[3] = {R-G, Y-V, B-O};
    char color[3] = {'R', 'Y', 'B'};

    res[n] = 0;
    int init_n = n;
    n = accumulate(cnt,cnt+3,0);

    REP(i,3)if(cnt[i]>n-cnt[i])
    {
        printf("IMPOSSIBLE\n");
        return;
    }

    REP(i,3)FOR(j,i+1,3)if(cnt[i]>cnt[j])swap(cnt[i],cnt[j]),swap(color[i],color[j]);

    priority_queue<pair<int,int>> q;
    REP(i,3)q.push(make_pair(cnt[i],i));

    int i=0;
    REP(j,n)
    {
        pair<int,int> p1 = q.top();
        q.pop();

        if (i==0 || res[i-1]!=color[p1.second])
        {
            res[i++]=color[p1.second];
            if(res[i-1]=='B')while(O>0)res[i++]='O',res[i++]='B',--O;
            if(res[i-1]=='Y')while(V>0)res[i++]='V',res[i++]='Y',--V;
            if(res[i-1]=='R')while(G>0)res[i++]='G',res[i++]='R',--G;

            q.push(make_pair(p1.first-1,p1.second));
            continue;
        }

        pair<int,int> p2 = q.top();
        q.pop();

        if (p2.first==0)
        {
            printf("IMPOSSIBLE\n");
            return;
        }

        res[i++]=color[p2.second];
        if(res[i-1]=='B')while(O>0)res[i++]='O',res[i++]='B',--O;
        if(res[i-1]=='Y')while(V>0)res[i++]='V',res[i++]='Y',--V;
        if(res[i-1]=='R')while(G>0)res[i++]='G',res[i++]='R',--G;
        q.push(make_pair(p2.first-1,p2.second));
        q.push(p1);
    }

    int ccc=0;
    if(O>0)++ccc;
    if(V>0)++ccc;
    if(G>0)++ccc;
    if((i==0 && ccc>1)||(i>0&&ccc>0))
    {
        printf("IMPOSSIBLE\n");
        return;
    }

    while(O>0)res[i++]='O',res[i++]='B',--O;
    while(V>0)res[i++]='V',res[i++]='Y',--V;
    while(G>0)res[i++]='G',res[i++]='R',--G;

    REP(j,init_n)if(res[j]==res[(j+1)%init_n])
    {
        printf("IMPOSSIBLE\n");
        return;
    }

    printf("%s\n",res);
}


int main()
{
    //freopen("../input.txt", "r", stdin);
    //freopen("../data/B-small-attempt1.in", "r", stdin);
    freopen("../data/B-large.in", "r", stdin);

    freopen("../output.txt", "w+", stdout);

    int T;
    scanf("%d", &T);
    REP(i, T)
    {
        printf("Case #%d: ", i+1);
        solve();
    }

    return 0;
}
