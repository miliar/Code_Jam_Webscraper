#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdint>

struct Distance
{
    uint64_t L;
    uint64_t R;
    uint64_t S;
    bool free;
    Distance(uint64_t l, uint64_t r, uint64_t s) : L(l), R(r), S(s), free(true) {}

    uint64_t max() const { return L > R ? L : R; };
    uint64_t min() const { return L < R ? L : R; };
};

std::vector<uint64_t> stalls;
std::vector<uint64_t> pepoles;
std::vector<Distance> solution;
int n_testcases = 0;

void read_input() {
    std::cin >> n_testcases;
    stalls.resize(n_testcases);
    pepoles.resize(n_testcases);
    for(int i=0; i < n_testcases; i++) {
        std::cin >> stalls[i];
        std::cin >> pepoles[i];
    }
    solution.reserve(n_testcases);
}

void write_output() {
    for(int i=0; i < n_testcases; i++) {
        std::cout << "Case #" << i+1 << ": ";
        std::cout << solution[i].max() << " " << solution[i].min() << std::endl;
    }
}

void update_distance(std::vector<Distance>& dist, std::vector<Distance*>& max, uint64_t from)
{
    auto s = from;
    int right = 0;
    for(int i = s-1; i >= 0; i--) {
        if(not dist[i].free) break;
        dist[i].R = right;
        right++;
    }

    int left = 0;
    for(int i = s+1; i < dist.size(); i++) {
        if(not dist[i].free) break;
        dist[i].L = left;
        left++;
    }

    dist[s].free = false;
    auto er = std::find(max.begin(), max.end(), &(dist[s]));
    max.erase(er);

    // std::cout << "DIST \n";
    // for(auto d: dist) { std::cout << d.L << " " << d.R << " " << d.S << " " << d.free <<  std::endl; }
}

void solve() {
    for(int i=0; i < n_testcases; i++) {
        uint64_t stall = stalls[i];
        uint64_t pepole = pepoles[i];
        // std::cout << "Test " << i << " stalls " << stall << " pepole " << pepole << std::endl;
        std::vector<Distance> dist;
        dist.reserve(stall);
        std::vector<Distance*> max(stall);
        for(uint64_t s=0; s < stall; s++) {
            dist.push_back({s, stall-1-s, s});
            max[s] = &(dist[s]);
        }

        // std::cout << "DIST \n";
        // for(auto d: dist) { std::cout << d.L << " " << d.R << " " << d.S  << std::endl; }

        Distance winner = dist[0];

        for(uint64_t person=0; person < pepole; person++) {

            std::sort(max.begin(), max.end(),
                [](const Distance* a, const Distance* b) { return a->min() > b->min(); });

            // std::cout << "MAX \n";
            // for(auto d: max) { std::cout << d->L << " " << d->R << " " << d->S  << std::endl; }

            auto it = max.begin();
            auto it2 = max.begin()+1;
            std::vector<Distance*> min;
            min.push_back(*it);
            while(it2 != max.end() && (*it)->min() == (*it2)->min()) {
                min.push_back(*it2);
                it++; it2++;
            }

            if(min.size() == 1) {
                winner = *(min[0]);
                update_distance(dist, max, winner.S);
                continue;
            } else {
                std::sort(min.begin(), min.end(),
                    [](const Distance* a, const Distance* b) { return a->max() > b->max(); });
            }
            //
            // std::cout << "MIN \n";
            // for(auto d: min) { std::cout << d->L << " " << d->R << " " << d->S  << std::endl; }

            auto it3 = min.begin();
            auto it4 = min.begin()+1;
            std::vector<Distance*> leftmost;
            leftmost.push_back(*it3);
            while(it4 != min.end() && (*it3)->max() == (*it4)->max()) {
                leftmost.push_back(*it4);
                it3++; it4++;
            }

            if(leftmost.size() > 1) {
                std::sort(leftmost.begin(), leftmost.end(),
                    [](const Distance* a, const Distance* b) { return a->S < b->S; });
            }

            // std::cout << "leftmost \n";
            // for(auto d: leftmost) { std::cout << d->L << " " << d->R << " " << d->S  << std::endl; }

            winner = *(leftmost[0]);
            update_distance(dist, max, winner.S);
        }

        solution[i] = winner;
    }
}

int main() {
    read_input();
    solve();
    write_output();
}
