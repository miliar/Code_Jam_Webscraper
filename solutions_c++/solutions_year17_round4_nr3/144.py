#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;

class SCC {
    public:
    SCC(int n) : size(n), graph(n), num_scc(0), mapping(n) {};
    void add_edge(int from, int to);
    void add_undirected_edge(int from, int to);
    void decompose();
    int get_size();
    vector <vector <int> > get_graph();
    vector <int> get_mapping();
    vector <int> get_weight();
    
    private:
    vector <vector <int> > graph;
    int size;
    int num_scc;
    vector <int> mapping;
};

void SCC::add_edge(int from, int to) {
    graph[from].push_back(to);
}

void SCC::add_undirected_edge(int from, int to) {
    graph[from].push_back(to);
    graph[to].push_back(from);
}

void SCC::decompose() {
    int num_visit = 0, num_stack = 0, num_dfs = 0;
    int *order = (int *)malloc(sizeof(int) * size);
    int *low = (int *)malloc(sizeof(int) * size);
    bool *in = (bool *)malloc(sizeof(bool) * size);
    int *stack = (int *)malloc(sizeof(int) * size);
    int *dfs_v = (int *)malloc(sizeof(int) * size);
    int *dfs_index = (int *)malloc(sizeof(int) * size);
    
    for (int i = 0; i < size; i++) {
        order[i] = -1;
        in[i] = false;
    }
    for (int i = 0; i < size; i++) {
        if (order[i] != -1) continue;
        dfs_v[num_dfs] = i;
        dfs_index[num_dfs++] = -1;
        while (num_dfs > 0) {
            int v = dfs_v[--num_dfs];
            int index = dfs_index[num_dfs];
            if (index == -1) {
                order[v] = low[v] = num_visit++;
                stack[num_stack++] = v;
                in[v] = true;
            } else {
                low[v] = min(low[v], low[graph[v][index]]);
            }
            for (index++; index < graph[v].size(); index++) {
                int w = graph[v][index];
                if (order[w] == -1) {
                    dfs_v[num_dfs] = v;
                    dfs_index[num_dfs++] = index;
                    dfs_v[num_dfs] = w;
                    dfs_index[num_dfs++] = -1;
                    break;
                } else if (in[w] == true) {
                    low[v] = min(low[v], order[w]);
                }
            }
            if (index == graph[v].size() && low[v] == order[v]) {
                while (true) {
                    int w = stack[--num_stack];
                    in[w] = false;
                    mapping[w] = num_scc;
                    if (v == w) break;
                }
                num_scc++;
            }
        }
    }
    
    free(order);
    free(low);
    free(in);
    free(stack);
    free(dfs_v);
    free(dfs_index);
}

int SCC::get_size() {
    return num_scc;
}

vector <vector <int> > SCC::get_graph() {
    vector <vector <int> > new_graph(num_scc);
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < graph[i].size(); j++) {
            if (mapping[i] != mapping[graph[i][j]]) new_graph[mapping[i]].push_back(mapping[graph[i][j]]);
        }
    }
    return new_graph;
}

vector <int> SCC::get_mapping() {
    return mapping;
}

vector <int> SCC::get_weight() {
    vector <int> weight(num_scc, 0);
    for (int i = 0; i < size; i++) weight[mapping[i]]++;
    return weight;
}

int r, c;
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
char s[50][51];
int a[50][50];
int b[2500][2];
int p[4];

int dfs(int x, int y, int z) {
    if (x < 0 || x >= r || y < 0 || y >= c || s[x][y] == '#') return -1;
    if (s[x][y] == '|') return a[x][y];
    
    if (s[x][y] == '/') {
        z = 3 - z;
    } else if (s[x][y] == '\\') {
        if (z % 2 == 0) {
            z++;
        } else {
            z--;
        }
    }
    
    return dfs(x + dx[z], y + dy[z], z);
}

int main() {
    int t, i;
    
    scanf("%d", &t);
    
    for (i = 0; i < t; i++) {
        int n = 0, f = 0, j, k, l;
        
        scanf("%d %d", &r, &c);
        
        for (j = 0; j < r; j++) scanf("%s", s[j]);
        
        for (j = 0; j < r; j++) {
            for (k = 0; k < c; k++) {
                if (s[j][k] == '|' || s[j][k] == '-') {
                    s[j][k] = '|';
                    a[j][k] = n;
                    b[n][0] = j;
                    b[n][1] = k;
                    n++;
                }
            }
        }
        
        SCC scc(n * 2);
        
        for (j = 0; j < r && f == 0; j++) {
            for (k = 0; k < c && f == 0; k++) {
                if (s[j][k] == '|') {
                    for (l = 0; l < 4; l++) p[l] = dfs(j + dx[l], k + dy[l], l);
                    
                    if (p[0] >= 0 || p[2] >= 0) {
                        scc.add_edge(a[j][k] + n, a[j][k]);
                    }
                    
                    if (p[1] >= 0 || p[3] >= 0) {
                        scc.add_edge(a[j][k], a[j][k] + n);
                    }
                } else if (s[j][k] == '.') {
                    int f1 = -1, f2 = -1;
                    
                    for (l = 0; l < 4; l++) p[l] = dfs(j, k, l);
                    
                    if (p[0] >= 0 && p[2] >= 0) {
                        scc.add_edge(p[0] + n, p[0]);
                        scc.add_edge(p[2] + n, p[2]);
                    } else if (p[0] >= 0) {
                        f1 = p[0];
                    } else if (p[2] >= 0) {
                        f1 = p[2];
                    }
                    
                    if (p[1] >= 0 && p[3] >= 0) {
                        scc.add_edge(p[1], p[1] + n);
                        scc.add_edge(p[3], p[3] + n);
                    } else if (p[1] >= 0) {
                        f2 = p[1];
                    } else if (p[3] >= 0) {
                        f2 = p[3];
                    }
                    
                    if (f1 == -1 && f2 == -1) {
                        f = 1;
                    } else if (f1 >= 0) {
                        scc.add_edge(f1, f1 + n);
                    } else if (f2 >= 0) {
                        scc.add_edge(f2 + n, f2);
                    } else {
                        scc.add_edge(f1, f2);
                        scc.add_edge(f2 + n, f1 + n);
                    }
                }
            }
        }
        
        if (f == 1) {
            printf("Case #%d: IMPOSSIBLE\n", i + 1);
            
            continue;
        }
        
        scc.decompose();
        vector <int> mapping = scc.get_mapping();
        
        for (j = 0; j < n; j++) {
            if (mapping[j] == mapping[n + j]) break;
        }
        
        if (j < n) {
            printf("Case #%d: IMPOSSIBLE\n", i + 1);
        } else {
            printf("Case #%d: POSSIBLE\n", i + 1);
            
            for (j = 0; j < n; j++) {
                if (mapping[j] > mapping[n + j]) s[b[j][0]][b[j][1]] = '-';
            }
            
            for (j = 0; j < r; j++) printf("%s\n", s[j]);
        }
    }
    
    return 0;
}
