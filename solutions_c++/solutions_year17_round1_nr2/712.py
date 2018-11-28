#include <bits/stdc++.h>
#define ll long long
using namespace std;

struct st
{
    int l;
    int h;
    int in;
    st(int lo, int hi, int i)
    {
        l = lo;
        h = hi;
        in = i;
    }
    bool operator < (const st &b)
    {
        return l == b.l? h < b.h : l < b.l;
    }
};

int N, P;
int M[1000][1000];
int m[1000];
int lo[1000][1000];
int hi[1000][1000];

bool bi[10];
int ans;

vector<st>v[1000];
vector<st>g;

void findRange(int i, int j)
{
    //cout<<"Trying ingredient "<<i<<" packet "<<j<<" mass "<<M[i][j]<<endl;

    for(int k = 1; ; k++)
    {
        if(1ll * k * m[i] * 9 > 1ll * M[i][j] * 10)
        {
            break;
        }
        if(1ll * M[i][j] * 10 >= 1ll * k * m[i] * 9 && 1ll * M[i][j] * 10 <= 1ll * k * m[i] * 11)
        {
            if(!lo[i][j])
            {
                lo[i][j] = k;
            }
            hi[i][j] = k;
        }
    }
    if(lo[i][j])
    {
        v[i].push_back(st(lo[i][j], hi[i][j], i));
    }
    //cout<<lo[i][j]<<" "<<hi[i][j]<<endl;
}

bool doesIntersect(int Li, int Hi, int Lj, int Hj)
{
    //int Li = lo[ei][i];
    //int Hi = hi[ei][i];

    //int Lj = lo[ej][j];
    //int Hj = hi[ej][j];

    return max(Li, Lj) <= min(Hi, Hj);
}



int sz[1000];
int cur[1000];

int main()
{
    freopen("00.in", "r", stdin);
    freopen("00.out", "w", stdout);

    int tc, n;

    scanf("%d", &tc);
    
    for(int t = 1; t <= tc; t++)
    {
        printf("Case #%d: ", t);
        scanf("%d %d", &N, &P);

        for(int i = 0; i < N; i++)
        {
            scanf("%d", &m[i]);
        }
        int inv = 0;
        for(int i = 0; i < N; i++)
        {
            v[i].clear();
            sz[i] = 0;
            cur[i] = 0;
            for(int j = 0; j < P; j++)
            {
                scanf("%d", &M[i][j]);
                lo[i][j] = 0;
                hi[i][j] = 0;

                findRange(i, j);

                
            }
            sz[i] = v[i].size();
            if(!sz[i])
            {
                inv++;
            }
        }
        ans = 0;

        if(N == 1)
        {
            for(int i = 0; i < P; i++)
            {
                if(lo[0][i])
                {
                    ans++;
                }
            }
            cout<<ans<<endl;
            continue;
        }

        if(inv)
        {
            printf("0\n");
            continue;
        }
        
        for(int i = 0; i < N; i++)
        {
            sort(v[i].begin(), v[i].end());
            //cout<<"ingredient "<<i<<"->";
            for(int j = 0; j < v[i].size(); j++)
            {
                //cout<<v[i][j].l<<","<<v[i][j].h<<" ";
            }//cout<<endl;
        }

        g.clear();

        for(int i = 0; i < N; i++)
        {
            g.push_back(v[i][0]);
        }

        while(1)
        {


            sort(g.begin(), g.end());

            int inv = 0;

            if(doesIntersect(g[0].l, g[0].h, g[N - 1].l, g[N - 1].h))
            {
                //cout<<"Taking current set"<<endl;
                ans++;

                for(int i = 0; i < N; i++)
                {
                    int in = g[i].in;
                    cur[ in ]++;
                    if(cur[in] >= sz[in])
                    {
                        inv++;
                        continue;
                    }
                    g[i] = v[ in ][cur[in]];
                }
            }
            else
            {
                int in = g[0].in;
                cur[in]++;
                //cout<<"evicted "<<g[0].l<<","<<g[0].h<<","<<g[0].in<<endl;
                if(cur[in] >= sz[in])
                {
                    inv++;
                }
                else
                {
                    g[0] = v[in][cur[in]];
                    //cout<<"inserted "<<g[0].l<<","<<g[0].h<<","<<g[0].in<<endl;
                }
            }
            if(inv)
            {
                break;
            }

        }cout<<ans<<endl;
    }



    return 0;
}
