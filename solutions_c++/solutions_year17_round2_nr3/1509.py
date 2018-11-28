#include <bits/stdc++.h>

using namespace std;

constexpr int MAX_N = 100 + 1;
constexpr double INF = numeric_limits<double>::max() / 3;

struct Horse{
    double speed;
    double maxDist;
};

struct State{
    Horse horse;
    int node;
    double dist;
    
    bool operator < (const State &S) const{
        return dist < S.dist;
    }
};

Horse horses[MAX_N];
double dist[MAX_N];
double D[MAX_N][MAX_N], newD[MAX_N][MAX_N];
bool expanded[MAX_N];

void expand_node(int source, int N){
    for (int i = 1; i <= N; i++)
        dist[i] = INF;
    
    priority_queue<State> Q;
    
    dist[source] = 0;
    Q.push({horses[source], source, dist[source]});
    
    while (!Q.empty()){
        State state = Q.top();
        Q.pop();
        
        Horse horse = state.horse;
        int node = state.node;
        
        for (int u = 1; u <= N; u++){
            if (D[node][u] != -1){
                double cost = D[node][u] / horse.speed;
                
                if (horse.maxDist >= D[node][u] && dist[u] > dist[node] + cost){
                    dist[u] = dist[node] + cost;
                    
                    Horse newHorse;
                    newHorse.speed = horse.speed;
                    newHorse.maxDist = horse.maxDist - D[node][u];
                    
                    Q.push({newHorse, u, dist[u]});
                }
            }
        }
    }
    
    for (int i = 1; i <= N; i++)
        if (i != source && dist[i] != INF){
            
            if (newD[source][i] == -1)
                newD[source][i] = dist[i];
            else
                newD[source][i] = min(newD[source][i], dist[i]);
        }
}

int main()
{   
    assert(freopen("C-small-attempt0.in", "r", stdin));
    freopen("C-small-attempt0.out", "w", stdout);
    ios_base::sync_with_stdio(false);
    
    int TESTS;
    cin >> TESTS;
    
    for (int test = 1; test <= TESTS; test++){
        int N, Q;
        cin >> N >> Q;
        
        assert(1 <= N && N <= 100);
        assert(1 <= Q && Q <= 100);
        
        for (int i = 1; i <= N; i++)
            cin >> horses[i].maxDist >> horses[i].speed;
            
        for (int i = 1; i <= N; i++)
            for (int j = 1; j <= N; j++){
                cin >> D[i][j];
                newD[i][j] = D[i][j];
            }
                
        for (int i = 1; i <= N; i++)
            expand_node(i, N);
            
        for (int i = 1; i <= N; i++){
            for (int j = 1; j <= N; j++){
                D[i][j] = newD[i][j];
            }
        }
            
        for (int k = 1; k <= N; k++)
            for (int i = 1; i <= N; i++)
                for (int j = 1; j <= N; j++)
                    if (D[i][k] != -1 && D[k][j] != -1)
                        if (D[i][j] == -1 || D[i][j] > D[i][k] + D[k][j])
                            D[i][j] = D[i][k] + D[k][j];
                
        vector<double> answers;
        
        for (int q = 0; q < Q; ++q){
            int U, V;
            cin >> U >> V;
            answers.push_back(D[U][V]);
        }
        
        cout << "Case #" << test << ": ";
        
        if (answers.size() > 0){
            cout << fixed << setprecision(10);
            cout << answers[0];
        }
            
        for (int i = 1; i < answers.size(); i++){
            cout << fixed << setprecision(10);
            cout << " " << answers[i];
        }
        
        cout << endl;
    }
    
    return 0;
}