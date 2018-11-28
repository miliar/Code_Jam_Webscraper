// ༼∩ຈل͜ຈ༽つ━☆ﾟ.*･｡ﾟ .·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º> - code by: kdkdk
#define ONLINE_JUDGE //in case i forget to uncomment this, uncomment this.
#ifdef ONLINE_JUDGE
#include <bits/stdc++.h>
#else
#include "stdc++.h"
#endif

#define int long long
using namespace std;


struct path {
    double time;
    int horseCapacity, to, horseSpeed;
    path(double _time, int _horseCapacity, int _to, int _horseSpeed) : time(_time), horseCapacity(_horseCapacity), to(_to), horseSpeed(_horseSpeed) {}
    
};

bool operator<(const path & lhs, const path & rhs) {
    if(lhs.time != rhs.time) return lhs.time > rhs.time;
    if(lhs.horseCapacity != rhs.horseCapacity) return lhs.horseCapacity < rhs.horseCapacity;
    if(lhs.to != rhs.to) return lhs.to > rhs.to;
    
    return lhs.time < rhs.time;
}


vector<int> hcapacity, kmph;
double dijkstra (int start, int end, vector<vector<pair<int, int> > > & graph) {
    //priority_queue<pair<double,int>, vector<pair<double,int> >, greater<pair<double,int> > > q;
    priority_queue<path> q;
    path startPath(0,0,start,-1);
    q.push(startPath);
    
    map<pair<int,int>,double> visited;
    //vector<vector<double> > visited(graph.size(), vector<double>(10*10*10*10*10*10*10*10*10+1,-1));
    //for(int i = 1; i < 1005; ++i) {
    //    visited[start][i] = 0;
    //}
    while(q.size() != 0){
        path c = q.top();
        q.pop();
        //cout << "current horse " << c.to << " cap: " << c.horseCapacity << " speed: " << c.horseSpeed << " " << " time " << c.time << endl;
        //cout << visited[c.to][c.horseCapacity] << endl;
        if(visited.count({c.to,c.horseCapacity}) == 0) {
            visited[{c.to,c.horseCapacity}] = c.time;
            for(int j = 0; j < graph[c.to].size(); ++j) {
                
                //First stay on horse
                int travelDist1 = graph[c.to][j].first;
                int to1 = graph[c.to][j].second;
                int horseSpeed1 = c.horseSpeed;
                int horseCapacity1 = c.horseCapacity;
                //cout << "To: " << to1 << " " << horseCapacity1 << " " << travelDist1 << endl;

                if(horseCapacity1 >= travelDist1) {
                    double time1 = (double)travelDist1 / (double)c.horseSpeed;
                    horseCapacity1 -= travelDist1;
                    path newPath(c.time + time1, horseCapacity1, to1, horseSpeed1);
                    q.push(newPath);
                }
                
                //Switch horses
                int travelDist2 = travelDist1;
                int to2 = to1;
                int horseCapacity2 = hcapacity[c.to];
                int horseSpeed2 = kmph[c.to];
                if(horseCapacity2 >= travelDist2) {
                    double time2 = (double)travelDist2 / (double) horseSpeed2;
                    horseCapacity2 -= travelDist2;
                    path newPath(c.time + time2, horseCapacity2, to2, horseSpeed2);
                    q.push(newPath);
                }
                
            }
        }
    }
    
    double fastest = -1;
    for(const pair<pair<int, int>,double> & it : visited) {
        if(it.first.first == end) {
            if(fastest == -1 || it.second < fastest) {
                fastest = it.second;
            }
        }
    }
    return fastest;
}

signed main() {
#ifndef ONLINE_JUDGE
    freopen("/Users/kdkdk/Desktop/input.txt", "r", stdin);
    //freopen("/Users/kdkdk/Desktop/output.txt", "w", stdout);
#endif
    cout << std::fixed;
    std::cout << std::setprecision(9);
    int t; cin >> t;
    for(int c = 1; c <= t; ++c) {
        int n, q; cin >> n >> q;
        hcapacity = vector<int> (n);
        kmph = vector<int>(n);
        vector<vector<pair<int,int> > > graph(n);
        for(int i = 0; i < n; ++i) {
            cin >> hcapacity[i] >> kmph[i];
        }
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < n; ++j) {
                int dij;
                cin >> dij;
                if(dij != -1) graph[i].push_back({dij,j});
            }
        }
        
        cout << "Case #" << c << ":";
        
        for(int i = 0; i < q; ++i) {
            int u, v; cin >> u >> v; --u; --v;
            cout << " " << dijkstra(u, v, graph);
        }
        cout << endl;
    }
}


/*
 3 1
 2 3
 2 4
 4 4
 -1 1 -1
 -1 -1 1
 -1 -1 -1
 
 
 
 q.push(path(1,2,0));
 q.push(path(1,3,0));
 q.push(path(2,2,0));
 q.push(path(2,3,0));
 while (q.size() != 0) {
 path c = q.top();
 q.pop();
 cout << c.time << " " << c.horseCapacity << " " << c.to << endl;
 }
*/
