#include <bits/stdc++.h>

struct Edge{
    int t;
    double d;
};

struct Node{
    double he;
    double hs;
    
    std::vector<Edge*> ed;
    
    std::vector<Edge*> ned;
};

#define MAXN 201
double dis[MAXN];
Node nd[MAXN];

void dijkstra1(int F){
    for(int i=0; i<MAXN; ++i) dis[i] = FLT_MAX;
    
    std::priority_queue<std::pair<double, int>, std::vector<std::pair<double, int > >, std::greater<std::pair<double, int > > > pq;
    dis[F] = 0;
    pq.push(std::make_pair(0, F));
    while(!pq.empty()){
        std::pair<double, int> p = pq.top();
        pq.pop();
        if(dis[p.second] != p.first) continue;
        for(auto iter = nd[p.second].ed.begin(); iter != nd[p.second].ed.end(); ++iter){
            Edge *e = *iter;
            if(p.first + e->d < dis[e->t]){
                dis[e->t] = p.first + e->d;
                pq.push(std::make_pair(dis[e->t], e->t));
            }
        }
    }
}

void dijkstra2(int F){
    for(int i=0; i<MAXN; ++i) dis[i] = FLT_MAX;
    
    std::priority_queue<std::pair<double, int>, std::vector<std::pair<double, int > >, std::greater<std::pair<double, int > > > pq;
    dis[F] = 0;
    pq.push(std::make_pair(0, F));
    while(!pq.empty()){
        std::pair<double, int> p = pq.top();
        pq.pop();
        if(dis[p.second] != p.first) continue;
        for(auto iter = nd[p.second].ned.begin(); iter != nd[p.second].ned.end(); ++iter){
            Edge *e = *iter;
            if(p.first + e->d < dis[e->t]){
                dis[e->t] = p.first + e->d;
                pq.push(std::make_pair(dis[e->t], e->t));
            }
        }
    }
}

void test(int t){
    std::cout << "Case #" << t << ": ";
    
    int N, Q;
    std::cin >> N >> Q;
    
    for(int i=0; i<N; ++i){
        std::cin >> nd[i].he >> nd[i].hs;
        
        for(auto& ed : nd[i].ed){
            delete ed;
        }
        nd[i].ed.clear();
        
        for(auto& ed : nd[i].ned){
            delete ed;
        }
        nd[i].ned.clear();
    }
    
    for(int i=0; i<N; ++i){
        for(double j=0; j<N; ++j){
            int k;
            std::cin >> k;
            if(k == -1) continue;
            
            Edge *e = new Edge;
            e->t = j;
            e->d = k;
            nd[i].ed.push_back(e);
        }
    }
    
    for(int i=0; i<N; ++i){
        dijkstra1(i);
        
        for(int j=0; j<N; ++j) {
            if(i == j) continue;
            if(dis[j] > nd[i].he+1e-9) continue;
                        
            Edge *e = new Edge;
            e->t = j;
            e->d = dis[j]/nd[i].hs;
            nd[i].ned.push_back(e);
        }
    }
    
    for(int i=0; i<Q; ++i){
        int f, t;
        std::cin >> f >> t;
        f--; t--;
        
        dijkstra2(f);
        std::cout << std::fixed << std::setprecision(9) << dis[t];
        if(i != Q-1) std::cout << " ";
    }
    std::cout << std::endl;
}

int main() {
    int T;
    std::cin >> T;
    for(int i=1; i<=T; ++i) {
        test(i);
    }
}
