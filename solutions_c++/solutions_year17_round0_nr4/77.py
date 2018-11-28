#include<bits/stdc++.h>
using namespace std;

struct BipartiteMatching {
    int n, m;
    vector<vector<int>> graph;
    vector<int> matched, match, edgeview, level;
    vector<int> reached[2];
    BipartiteMatching(int n, int m) : n(n), m(m), graph(n), matched(m, -1), match(n, -1) {}

    bool assignLevel() {
        bool reachable = false;
        level.assign(n, -1);
        reached[0].assign(n, 0);
        reached[1].assign(m, 0);
        queue<int> q;
        for (int i = 0; i < n; i++) {
            if (match[i] == -1) {
                level[i] = 0;
                reached[0][i] = 1;
                q.push(i);
            }
        }
        while (!q.empty()) {
            auto cur = q.front(); q.pop();
            for (auto adj : graph[cur]) {
                reached[1][adj] = 1;
                auto next = matched[adj];
                if (next == -1) {
                    reachable = true;
                }
                else if (level[next] == -1) {
                    level[next] = level[cur] + 1;
                    reached[0][next] = 1;
                    q.push(next);
                }
            }
        }
        return reachable;
    }

    int findpath(int nod) {
        for (int &i = edgeview[nod]; i < graph[nod].size(); i++) {
            int adj = graph[nod][i];
            int next = matched[adj];
            if (next >= 0 && level[next] != level[nod] + 1) continue;
            if (next == -1 || findpath(next)) {
                match[nod] = adj;
                matched[adj] = nod;
                return 1;
            }
        }
        return 0;
    }

    int solve() {
        int ans = 0;
        while (assignLevel()) {
            edgeview.assign(n, 0);
            for (int i = 0; i < n; i++)
                if (match[i] == -1)
                    ans += findpath(i);
        }
        return ans;
    }
};

char mf[100][100], mt[100][100], in[5], str[10];
bool ms[100][100];

int main()
{
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        printf("Case #%d: ",t);
        memset(mf,'.',sizeof(mf));
        memset(mt,'.',sizeof(mt));
        memset(ms,0,sizeof(ms));

        int n,m;
        scanf("%d%d",&n,&m);
        while(m--)
        {
            int a,b;
            scanf("%s%d%d",in,&a,&b);
            mf[a-1][b-1] = mt[a-1][b-1] = in[0];
        }

        BipartiteMatching bm1(n,n), bm2(2*n-1,2*n-1);
        for(int i=0;i<n;i++)
        {
            bool allp = true;
            for(int j=0;j<n;j++)
                if(mf[i][j] == 'x' || mf[i][j] == 'o')
                {
                    allp = false;
                    break;
                }
            if(allp)
                for(int j=0;j<n;j++)
                    ms[i][j] = 1;
        }
        for(int i=0;i<n;i++)
        {
            bool allp = true;
            for(int j=0;j<n;j++)
                if(mf[j][i] == 'x' || mf[j][i] == 'o')
                {
                    allp = false;
                    break;
                }
            for(int j=0;j<n;j++)
                ms[j][i] &= allp;
        }

        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++)
                if(ms[i][j]) bm1.graph[i].push_back(j);
        bm1.solve();
        
        for(int i=0;i<2*n-1;i++)
        {
            bool allp = true;
            for(int x=0;x<n;x++)
            {
                int y = i - x;
                if(y<0 || y>=n) continue;
                if(mf[y][x] == '+' || mf[y][x] == 'o')
                {
                    allp = false;
                    break;
                }
            }
            for(int x=0;x<n;x++)
            {
                int y = i - x;
                if(y<0 || y>=n) continue;
                ms[y][x] = allp;
            }
        }

        for(int i=-n+1;i<n;i++)
        {
            bool allp = true;
            for(int x=0;x<n;x++)
            {
                int y = i + x;
                if(y<0 || y>=n) continue;
                if(mf[y][x] == '+' || mf[y][x] == 'o')
                {
                    allp = false;
                    break;
                }
            }
            for(int x=0;x<n;x++)
            {
                int y = i + x;
                if(y<0 || y>=n) continue;
                ms[y][x] &= allp;
            }
        }
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++)
                if(ms[i][j])
                {
                    int ls = i+j, rs = i-j+n-1;
                    bm2.graph[ls].push_back(rs);
                }
        bm2.solve();

        for(int i=0;i<n;i++)
        {
            int j = bm1.match[i];
            if(j < 0) continue;
            if(mt[i][j] == '+') mt[i][j] = 'o';
            else mt[i][j] = 'x';
        }

        for(int i=0;i<2*n-1;i++)
        {
            int j = bm2.match[i];
            if(j < 0) continue;
            j -= n-1;
            int x = (i-j)/2, y = (i+j)/2;
            if(mt[y][x] == 'x') mt[y][x] = 'o';
            else mt[y][x] = '+';
        }
        
        int ans = 0;
        vector<string> bt;
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++)
            {
                if(mt[i][j] == 'o') ans+=2;
                else if(mt[i][j] == 'x' || mt[i][j] == '+') ans++;
                if(mf[i][j] == mt[i][j]) continue;
                sprintf(str,"%c %d %d",mt[i][j],i+1,j+1);
                bt.push_back(string(str));
            }
        printf("%d %d\n",ans,(int)bt.size());
        for(string s : bt)
            puts(s.c_str());
    }
}
