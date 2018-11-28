#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <set>
#include <iomanip>
#include <deque>
#include <stdio.h>
#include <fstream>
using namespace std;

#define REP(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define RREP(i,n) for(int (i)=(int)(n)-1;i>=0;i--)
#define REMOVE(Itr,n) (Itr).erase(remove((Itr).begin(),(Itr).end(),n),(Itr).end())
#define UNIQUE(Itr) sort((Itr).begin(),(Itr).end()); (Itr).erase(unique((Itr).begin(),(Itr).end()),(Itr).end())
#define LBOUND(Itr,val) lower_bound((Itr).begin(),(Itr).end(),(val))
#define UBOUND(Itr,val) upper_bound((Itr).begin(),(Itr).end(),(val))
#define MOD 1000000007
typedef long long ll;

int N,Q;
double dist[110][110];
double G[110][110];
double E[110],S[110];
double ans[110];
bool used[110];
vector<int> Graph[110];

void bfs(int v) {
    REP(i,110) used[i] = false;
    queue<int> que;
    que.push(v);
    while(que.size()!=0) {
        int vt = que.front();
        que.pop();
        if(used[vt])continue;
        used[vt] = true;
        double limit =  E[vt];
        double speed = S[vt];
        for(int i=1; i<=N; i++) {
            if(dist[vt][i] <= limit) {
                ans[i] = min(ans[i],ans[vt] + dist[vt][i] / speed);
            }
        }
        REP(i,Graph[vt].size()){
            que.push(Graph[vt][i]);
        }
    }
}

int main() {
    
    ifstream ifs("/Users/kurodakousaku/GCJ/2017/R1B/C/Csmallin.txt");
    int T; ifs >> T;
    REP(kai,T) {
        ifs >> N >> Q;
        REP(i,N) ifs >> E[i+1] >> S[i+1];
        int u,v;
        REP(i,N)REP(j,N) ifs >> G[i+1][j+1];
        ifs >> u >> v;
        
        REP(i,110)REP(j,110) dist[i][j] = 1.0e18;
        REP(i,N) dist[i+1][i+1] = 0.0;
        for(int i=1; i<=N; i++) {
            for(int j=1; j<=N; j++) {
                if(G[i][j] >= 0.0) {
                    dist[i][j] = G[i][j];
                    Graph[i].push_back(j);
                }
            }
        }
        for(int k=1; k<=N; k++) {
            for(int i=1; i<=N; i++) {
                for(int j=1; j<=N; j++) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
        
        REP(i,110) ans[i] = 1.0e18;
        ans[1] = 0.0;
        bfs(1);
        cout << fixed << setprecision(10) << "Case #" << kai + 1 << ": " << ans[N] << endl;
    }
    
    return 0;
}
