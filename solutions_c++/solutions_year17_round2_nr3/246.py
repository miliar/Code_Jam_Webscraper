#include <algorithm>
#include <assert.h>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <memory.h>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <utility>
#include <vector>
using namespace std;

typedef pair<double,int> PII;
typedef long long LL;

#define ALL(x) x.begin(),x.end()

#define DEB(args...) fprintf(stderr,args)

#define PB push_back
#define MP make_pair
#define ST first
#define ND second 

const long long INF = 0x3f3f3f3f3f3f3f3fll;

const int N = 110;

int e[N], s[N];
long long dist[N][N];
double resp[N][N];

vector<int>adj[N];
vector<double>pes[N];

priority_queue<PII, vector<PII>, greater<PII> > pq;

int main(){
    int t;
    scanf("%d", &t);
    for(int cas = 1; cas <= t; cas++){
        
        long long ans = 0;
        int n, q;
        scanf("%d %d", &n, &q);
        for(int i = 0; i < n; i++){
            adj[i].clear();
            pes[i].clear();
            scanf("%d %d", e+i, s+i);
        }
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                scanf("%lld",&dist[i][j]);
            }
        }
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(dist[i][j]==-1)dist[i][j]=INF;
                //printf("%lld\n",dist[i][j]);
            }
            dist[i][i]=0;
        }
        for(int k = 0; k < n; k++){
            for(int i = 0; i < n; i++){
                for(int j = 0; j < n; j++){
                    if(dist[i][j]>dist[i][k]+dist[k][j]){
                        dist[i][j]=dist[i][k]+dist[k][j];
                    }
                }
            }
        }
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(i==j)continue;
                //printf("dist %lld %d\n",dist[i][j],e[i]);
                if(dist[i][j]<=e[i]){
                    //printf("%d %d\n", i, j);
                    adj[i].push_back(j);
                    pes[i].push_back(dist[i][j]*1.0/((1.0)*s[i]));
                }
            }
        }
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                resp[i][j]=INF;
            }
            resp[i][i]=0.0;
            pq.push(PII(0.0,i));

            while(!pq.empty()){
                PII top = pq.top();
                pq.pop();

                int v = top.ND;
                double d = top.ST;
                if(d<=resp[i][v]){
                    for(int k = 0; k < adj[v].size(); k++){
                        int v2 = adj[v][k];
                        double cost = pes[v][k];
                        if(resp[i][v2] > resp[i][v] + cost){
                            resp[i][v2] = resp[i][v] + cost;
                            pq.push(PII(resp[i][v2],v2));
                        }
                    }
                }
            }
            
            
        }
        printf("Case #%d: ",cas);
        for(int i = 0; i < q; i++){
            int a, b;
            scanf("%d %d",&a,&b);
            a--,b--;
            printf("%lf ",resp[a][b]);
        }
        printf("\n");
    }
    
}
