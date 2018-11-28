#include <bits/stdc++.h>

using namespace std;

struct Path {
    list<int> route;
    double rem_dist;
    int speed;
    double time;
};

int main(){
    ifstream input("c.in");
    ofstream output;
    output.open ("c.out");
    unsigned long long T;

    input >> T;
    cout.precision(6);
    for(unsigned int i = 0; i < T; i++) {
        cout << "Progress " << i << " / " << (T - 1) << endl;
        int N, Q;
        input >> N >> Q;
        unsigned int E[N], S[N];
        unsigned int dist[N][N];
        double times[N];
        double times2[N];
        unsigned int rdist[N];
        for(int j = 0; j < N; j++) input >> E[j] >> S[j];
        for(int j = 0; j < N; j++) for(int k = 0; k < N; k++) input >> dist[j][k];
        output << "Case #" << (i + 1) << ":";
        queue<Path> open;
        for(int j = 0; j < Q; j++) {
            for(int k = 0; k < N; k++) times[k] = -1, rdist[k] = 0, times2[k] = -1;
            output << " ";
            int start, dest;
            input >> start >> dest;
            start--; dest--;
            Path stp;
            times[start] = 0;
            rdist[start] = stp.rem_dist;
            stp.route.push_front(start);
            stp.time = 0;
            stp.rem_dist = E[start];
            stp.speed = S[start];
            open.push(stp);
            while(!open.empty()) {
                Path node = open.front();
                open.pop();
                for(int k = 0; k < N; k++) {
                    if(dist[*node.route.begin()][k] != -1 && dist[*node.route.begin()][k] <= node.rem_dist) {
                        Path new_node = node;
                        new_node.route.push_front(k);
                        new_node.rem_dist -= dist[*node.route.begin()][k];
                        new_node.time += (double)dist[*node.route.begin()][k] / new_node.speed;
                        if(rdist[k] < new_node.rem_dist || times2[k] > new_node.time || times2[k] == -1) {
                            open.push(new_node);
                        }
                        if(rdist[k] < new_node.rem_dist && (times2[k] > new_node.time || times2[k] == -1)) {
                            rdist[k] = new_node.rem_dist;
                            times2[k] = new_node.time;
                        }
                        if(times[k] > new_node.time || times[k] == -1 || S[k] > new_node.speed) {
                            new_node.rem_dist = E[k];
                            new_node.speed = S[k];
                            open.push(new_node);
                        }
                        if(times[k] > new_node.time || times[k] == -1) {
                            times[k] = new_node.time;
                        }
                    }
                }
            }
            output << fixed << times[dest];
        }
        output << endl;
    }
    output.close();
    return 0;
}
