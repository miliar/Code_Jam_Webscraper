#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
typedef pair<int, int> pi;
int TC, N, P;
int R[50], G[50][50];
vector<pi> sorted[50];
priority_queue <int, vector<int>, greater<int> > pq[50];
pi decom(int g, int b){
    int r1 = 10 * g;
    int x = r1 / (9*b), y = r1/(11 * b) + (int)(r1 %(11*b) > 0);
    if(x < y) return pi(-1, -1);
    else return pi(y, x);
}
vector<int> starts;
int ptr[50];
int main(){
    scanf("%d", &TC);
    for(int tc = 1; tc <= TC; ++tc){
        starts.clear();
        scanf("%d %d", &N, &P);
        for(int i = 0; i < N; ++i){
            scanf("%d", &R[i]);
            while(!pq[i].empty()) pq[i].pop();
        }
        for(int i = 0; i < N; ++i){
            sorted[i].clear();
            for(int j = 0; j < P; ++j){
                scanf("%d", &G[i][j]);
                pi t = decom(G[i][j], R[i]);
                if(t.first != -1){
                    sorted[i].push_back(t);
                    starts.push_back(t.first);
                    starts.push_back(t.second);
                }
            }
            sort(sorted[i].begin(), sorted[i].end());
            ptr[i] = 0;
        }/*
        for(int i = 0; i < N; ++i){
            for(int j = 0; j < sorted[i].size(); ++j) printf(" ( %d %d ) ", sorted[i][j].first, sorted[i][j].second);
            printf("\n");
        }//*/
        sort(starts.begin(), starts.end());
        starts.resize(distance(starts.begin(), unique(starts.begin(), starts.end())));
        int ans = 0;
        for(auto x : starts){
            for(int i = 0; i < N; ++i){
                while(ptr[i] < sorted[i].size() && sorted[i][ptr[i]].first == x){
                    pq[i].push(sorted[i][ptr[i]].second);
                    ++ptr[i];
                }
            }
            while(true){
                bool safe = true; bool danger = true;
                for(int i = 0; i < N; ++i){
                    while(!pq[i].empty() && pq[i].top() < x) pq[i].pop();
                    if(pq[i].empty()) safe = false;
                    else if(pq[i].top() == x) danger = false;
                }
                if(safe && !danger){
                    for(int i = 0; i < N; ++i) pq[i].pop();
                    ++ans;
                }
                else break;
            }
        }
        bool safe = true;
        for(int i = 0; i < N; ++i){
            if(pq[i].empty()) safe = false;
        }
        if(safe){
            for(int i = 0; i < N; ++i) pq[i].pop();
            ++ans;
        }
        
        printf("Case #%d: %d\n", tc, ans);
    }
}
        
        
