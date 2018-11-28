#include <bits/stdtr1c++.h>

#define clr(ar) memset(ar, 0, sizeof(ar))
#define read() freopen("lol.txt", "r", stdin)
#define write() freopen("out.txt", "w", stdout)
#define dbg(x) cout << #x << " = " << x << endl
#define ran(a, b) ((((rand() << 15) ^ rand()) % ((b) - (a) + 1)) + (a))

using namespace std;

int adj[101][101];
long double dis[101][101];
int n, q, max_dis[101], speed[101];

struct compare{
    inline bool operator() (pair<int, int> a, pair<int, int> b){
        return dis[a.first][a.second] > dis[b.first][b.second];
    }
};

long double dijkstra(int s, int t){
    priority_queue <pair<int, int>, vector<pair<int, int>>, compare> PQ;
    for (int i = 0; i < 101; i++){
        for (int j = 0; j < 101; j++){
            dis[i][j] = 1e100;
        }
    }

    dis[s][s] = 0.0;
    PQ.push(make_pair(s, s));

    while (!PQ.empty()){
        pair<int, int> cur = PQ.top();
        PQ.pop();

        int i = cur.first, l = cur.second;
        if (i == t) return dis[i][l];

        for (int j = 1; j <= n; j++){
            if (adj[i][j] != -1){
                if (( (dis[i][l] - dis[l][l]) * speed[l] + adj[i][j] - 1e-9) <= max_dis[l]){
                    long double w = (long double)adj[i][j] / (long double)speed[l];
                    if (dis[j][l] > dis[i][l] + w){
                        dis[j][l] = dis[i][l] + w;
                        PQ.push(make_pair(j, l));
                    }

                    if (dis[j][j] > dis[i][l] + w){
                        dis[j][j] = dis[i][l] + w;
                        PQ.push(make_pair(j, j));
                    }
                }
            }
        }
    }
    return -1.0;
}

int main(){
    read();
    write();
    int T = 0, t, i, j, k, u, v;

    scanf("%d", &t);
    while (t--){
        scanf("%d %d", &n, &q);
        for (i = 1; i <= n; i++) scanf("%d %d", &max_dis[i], &speed[i]);

        for (i = 1; i <= n; i++){
            for (j = 1; j <= n; j++){
                scanf("%d", &adj[i][j]);
            }
        }

        printf("Case #%d:", ++T);
        while (q--){
            scanf("%d %d", &u, &v);
            printf(" %0.12f", (double)dijkstra(u, v) + 1e-15);
        }
        puts("");
    }
    return 0;
}
