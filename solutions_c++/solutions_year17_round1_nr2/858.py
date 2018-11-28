//
//  main.cpp
//  Dolphin
//
//  Created by Mahmud on 15/11/17.
//  Copyright © 2017 Mahmud. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <numeric>
#include <algorithm>
#include <functional>
#include <vector>
#include <queue>
#include <set>
#include <unordered_set>
#include <map>
#include <utility>
#include <cassert>
#include <iomanip>
#include <ctime>
#include <sstream>
#include <istream>

using namespace std;

const int me = 125;
const int MAXN = 2555; // число вершин
const int INF = 1000000000; // константа-бесконечность

int T, N, P;
int result;
double R[me], Q[me][me];

pair<int, int> calc(double a, int id){
    double ls = R[id] * 0.9;
    double rs = R[id] * 1.1;
    int l = a / ls;
    int r = a / rs;
    if(r * rs < a)
        r ++;
    return make_pair(r, l);
}
int get(double a, double b, int id1, int id2){
    pair<int, int> f = calc(a, id1);
    pair<int, int> s = calc(b, id2);
    //cout << "f = " << f.first << " and " << f.second << endl;
    //cout << "s = " << s.first << " and " << s.second << endl;
    if(f.first > f.second || s.first > s.second)
        return 0;
    if(f.second < s.first || f.first > s.second)
        return 0;
    return min(f.second, s.second);
}
/*
 void solve(vector<vector<double>> v, int sum){
 result = max(result, sum);
 int L = (int)v[0].size();
 for(int i = 0; i < L; i ++)
 for(int j = 0; j < L; j ++)
 if(get(v[0][i], v[1][j]) != 0){
 vector<vector<double>> to = v;
 to[0].erase(to[0].begin() + i);
 to[1].erase(to[1].begin() + j);
 solve(to, sum + 1);
 }
 }
 */
struct edge {
    int a, b, cap, flow;
};

int n, s, t, d[MAXN], ptr[MAXN], q[MAXN];
vector<edge> e;
vector<int> g[MAXN];

void add_edge (int a, int b, int cap) {
    edge e1 = { a, b, cap, 0 };
    edge e2 = { b, a, 0, 0 };
    g[a].push_back ((int) e.size());
    e.push_back (e1);
    g[b].push_back ((int) e.size());
    e.push_back (e2);
}

bool bfs() {
    int qh=0, qt=0;
    q[qt++] = s;
    memset (d, -1, (n + 10) * sizeof d[0]);
    d[s] = 0;
    while (qh < qt && d[t] == -1) {
        int v = q[qh++];
        for (size_t i=0; i<g[v].size(); ++i) {
            int id = g[v][i],
            to = e[id].b;
            if (d[to] == -1 && e[id].flow < e[id].cap) {
                q[qt++] = to;
                d[to] = d[v] + 1;
            }
        }
    }
    return d[t] != -1;
}

int dfs (int v, int flow) {
    if (!flow)  return 0;
    if (v == t)  return flow;
    for (; ptr[v]<(int)g[v].size(); ++ptr[v]) {
        int id = g[v][ptr[v]],
        to = e[id].b;
        if (d[to] != d[v] + 1)  continue;
        int pushed = dfs (to, min (flow, e[id].cap - e[id].flow));
        if (pushed) {
            e[id].flow += pushed;
            e[id^1].flow -= pushed;
            return pushed;
        }
    }
    return 0;
}

int dinic() {
    int flow = 0;
    for (;;) {
        if (!bfs())  break;
        memset (ptr, 0, (n + 10) * sizeof ptr[0]);
        //cout << "here in dfs" << endl;
        while (1){
            int pushed = dfs (s, INF);
            //cout << "pushed = " << pushed << endl;
            flow += pushed;
            if(pushed == 0)
                break;
        }
        
    }
    return flow;
}



int main(int argc, const char * argv[]) {
    //ios_base::sync_with_stdio(0);
    //cin.tie(0);
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    cin >> T;
    for(int c = 0; c < T; c ++){
        cin >> N >> P;
        for(int i = 1; i <= N; i ++)
            cin >> R[i];
        for(int i = 1; i <= N; i ++)
            for(int j = 1; j <= P; j ++)
                cin >> Q[i][j];//cout << "here1" << endl;
        result = 0;
        if(N == 1){
            for(int i = 1; i <= P; i ++){
                pair<int, int> p = calc(Q[1][i], 1);
                if(p.first <= p.second)
                    result ++;
            }
        }
        else{
            for(int i = 1; i < N; i ++)
                for(int j = 1; j <= P; j ++)
                    for(int k = 1; k <= P; k ++){
                        int go = get(Q[i][j], Q[i + 1][k], i, i + 1);
                        if(go != 0)
                            //cout << (i - 1) * P + j << " to " << i * P + k << endl,
                            add_edge((i - 1) * P + j, i * P + k, 1);
                    }
            //cout << "here" << endl;
            s = 0, t = N * P + 1;
            n = t - 1;
            for(int i = 1; i <= P; i ++){
                add_edge(s, i, 1);
                add_edge((N - 1) * P + i, t, 1);
            }
            //for(auto i : e)
            //    cout << i.a << " " << i.b << " " << i.cap << endl;
            result = dinic();
            e.clear();
            fill(ptr, ptr + MAXN, 0);
            for(int i = 0; i < MAXN; i ++){
                g[i].clear();
            }
        }
        
        cout << "Case #" << c + 1 << ": " << result << endl;
        
    }
    
    return 0;
}
