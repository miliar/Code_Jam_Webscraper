#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

typedef tuple<int,int,ll> t3;
typedef tuple<double, int, int, ll> t4;

#define INF (1e200)

int N;

int input[100][100];
int input_spd[100];
int input_rem[100];

vector<vector<int>> adjList;

map<t3, double> memo;
set<t3> vis;

double f(int index, int spd, ll rem){
    if(index == N-1){
        return 0;
    }

    t3 state(index, spd, rem);
    auto itr = memo.find(state);
    if(itr != memo.end()){
        return itr->second;
    }


    double best_ret = INF;

    if(rem - input[index][index+1] >= 0){
        double this_horse = (double)input[index][index+1]  / (double) spd + f(index+1, spd, rem-input[index][index+1]);
        best_ret = min(best_ret, this_horse);
    }

    // Use this horse
    if(input_rem[index] - input[index][index+1] >= 0){
        double this_horse = (double) input[index][index+1] / (double) input_spd[index] + f(index+1, input_spd[index], input_rem[index]-input[index][index+1]);
        best_ret = min(best_ret, this_horse);
    }

    memo[state] = best_ret;
    return best_ret;
}

int main(){
    int cases;
    scanf("%d", &cases);

    for(int e = 0; e<cases; e++){
        int Q;
        scanf("%d %d", &N, &Q);
        for(int i = 0; i<N; i++){
            scanf("%d %d", &input_rem[i], &input_spd[i]);
        }
        adjList.assign(N, vector<int>());
        for(int i =0; i<N; i++){
            for(int j = 0; j<N; j++){
                scanf("%d", &input[i][j]);
                if(input[i][j] != -1){
                    adjList[i].push_back(j);
                }
            }
        }

        printf("Case #%d:", e+1);
        for(int q = 0; q<Q; q++){
            int src, dest;
            scanf("%d %d", &src, &dest);
            src--;
            dest--;

            priority_queue<t4, vector<t4>, greater<t4>> pq;
            pq.push(t4(0, src, input_spd[src], input_rem[src]));
            vis.clear();

            double ans = 0;

            while(!pq.empty()){
                t4 t = pq.top();
                pq.pop();

                double dist = get<0>(t);
                int index = get<1>(t);
                int spd = get<2>(t);
                ll rem = get<3>(t);

                t3 state(index, spd, rem);

                if(vis.count(state)){
                    continue;
                }
                // printf("Popped %f %d %d %lld\n", dist, index, spd, rem);
                vis.insert(state);
                if(index == dest){
                    ans = dist;
                    break;
                }

                for(auto adj : adjList[index]){
                    // if same
                    if(rem - input[index][adj] >= 0){
                        double next_cost = (double) input[index][adj] / (double) spd;
                        t3 next_state(adj, spd, rem-input[index][adj]);
                        if(vis.count(next_state)) continue;
                        pq.push(t4(dist+next_cost, adj, spd, rem-input[index][adj]));
                        // printf("Going to %d from %d\n", adj, index);
                    }

                    // use horses
                    if(input_rem[index] - input[index][adj] >= 0){
                        double next_cost = (double) input[index][adj] / (double) input_spd[index];
                        t3 next_state(adj, input_spd[index], input_rem[index]-input[index][adj]);
                        if(vis.count(next_state)) continue;
                        pq.push(t4(dist+next_cost, adj, input_spd[index], input_rem[index]-input[index][adj]));
                        // printf("Going to %d from %d\n", adj, index);
                        
                    }
                }

            }

            printf(" %f", ans);

        }
        printf("\n");

    }
    return 0;
}