#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdint>
#include <climits>
#include <queue>
#include <iomanip>

struct Horse {
    int city;
    double km;
    double speed; //km/h

    double left_km;
};

struct Testcase {
    int n_cities;
    int n_routes;
    std::vector<Horse> horses;
    std::vector<std::vector<double>> map;
    std::vector<std::pair<int, int>> routes;
};

std::vector<Testcase> tcs;
std::vector<double> solution;
int n_testcases = 0;

void read_input() {
    std::cin >> n_testcases;
    for(int i=0; i < n_testcases; i++) {
        Testcase tc;
        std::cin >> tc.n_cities >> tc.n_routes;
        tc.horses.reserve(tc.n_cities);
        for(int c=0; c < tc.n_cities; c++) {
            Horse horse;
            horse.city = c;
            std::cin >> horse.km >> horse.speed;
            horse.left_km = horse.km;
            tc.horses.push_back(horse);
        }
        tc.map.resize(tc.n_cities);
        for(int ci=0; ci < tc.n_cities; ci++) {
            tc.map[ci].resize(tc.n_cities);
            for(int cj=0; cj < tc.n_cities; cj++) {
                std::cin >> tc.map[ci][cj];
            }
        }
        tc.routes.reserve(tc.n_routes);
        for(int r=0; r < tc.n_routes; r++) {
            std::pair<int, int> route;
            std::cin >> route.first >> route.second;
            tc.routes.push_back(route);
        }
        tcs.push_back(tc);
    }
    solution.reserve(n_testcases);
}

void write_output() {
    for(int i=0; i < n_testcases; i++) {
        auto& s_tc = solution[i];
        std::cout << "Case #" << i+1 << ": ";
        // for(auto y : s_tc)
            std::cout << std::setprecision(10) << s_tc << std::endl;
        // std::cout << std::endl;
    }
}

struct Node {
    int city;
    double time;
    Horse horse;
    int source;
    void print() {
        std::cout << "Node: city, horse, left_km, time, source: " << city << ", "
                  << horse.city << ", " << horse.left_km << ", " << time << ", " << source << std::endl;
    }
};

bool operator>(const Node lhs, const Node rhs) {
    return lhs.time > rhs.time;
}

void solve() {
    for(auto& tc: tcs) {
        int start = tc.routes[0].first - 1;
        int end = tc.routes[0].second - 1;
        std::priority_queue<Node, std::vector<Node>, std::greater<Node>> pq;
        std::map<std::pair<int, int>, double> time;
        Node src;
        src.time = 0;
        src.horse = tc.horses[start];
        src.city = start;
        src.source = start;
        // src.print();
        time[{start, start}] = 0;
        pq.push(src);
        Node node;
        do {
            node = pq.top();
            // std::cout << "Choose ";
            // node.print();
            pq.pop();
            auto& adj = tc.map[node.city];
            for(int c=0; c < adj.size(); c++) {
                if(adj[c] != -1) {
                    if(node.horse.left_km - adj[c] >= 0) {
                        std::pair<int, int> n = {c, node.horse.city};
                        if(time.find(n) == time.end() || time[n] > node.time + adj[c] / node.horse.speed) {
                            Node adjc;
                            adjc.time = node.time + adj[c] / node.horse.speed;
                            Horse horse = node.horse;
                            horse.left_km = horse.left_km - adj[c];
                            adjc.horse = horse;
                            adjc.city = c;
                            adjc.source = node.city;
                            time[n] = adjc.time;
                            pq.push(adjc);
                            // std::cout << "Use old horse ";
                            // adjc.print();
                        }
                    }
                    std::pair<int, int> n = {c, node.city};
                    if(time.find(n) != time.end()) {
                        // std::cout << "Found node (c, src): (" << c << ", " << node.city << ") with time " << time[n] << std::endl;
                    }

                    if(time.find(n) == time.end() || time[n] > node.time + adj[c] / tc.horses[node.city].speed) {
                        Node adjc;
                        Horse horse = tc.horses[node.city];
                        adjc.time = node.time + adj[c] / horse.speed;
                        horse.left_km = horse.left_km - adj[c];
                        adjc.horse = horse;
                        adjc.city = c;
                        adjc.source = node.city;
                        time[n] = adjc.time;
                        pq.push(adjc);
                        // std::cout << "Use new horse ";
                        // adjc.print();
                    }
                }
            }
        } while (!pq.empty() && node.city != end);
        solution.push_back(node.time);
        // if(node.city == end) {
        //     std::cout << "Reached end within " << std::setprecision(10) << node.time << std::endl;
        // }
    }
}

int main() {
    read_input();
    solve();
    write_output();
}
