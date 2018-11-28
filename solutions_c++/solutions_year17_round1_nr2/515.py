// Compile with MinGW-64 (6.3.0) in MSYS2
// Compile switches: -std=c++11 -Wall -Wconversion -Werror

#include <stdint.h>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <map>
#include <string>
#include <queue>
#include <vector>

using namespace std;

struct ServesData {
    int min;
    int max;
};

ServesData getServes(int n, int per_serve) {
    ServesData serves;
    serves.max = (n*10) / (per_serve * 9);
    serves.min = (n*10) / (per_serve * 11);
    if ((n*10) % (per_serve * 11) > 0)
        serves.min++;
    return serves;
}

void solve(int caseNo) {
    std::cout << "Case #" << caseNo << ": ";

    int n, p;
    std::cin >> n >> p;

    //std::cerr << n << " " << p << "\n";
    vector<int> req;
    for (int i=0; i<n; ++i) {
        int x;
        cin >> x;
        req.push_back(x);
    }
    
    vector<vector<int>> packs;
    for (int i=0; i<n; ++i) {
        vector<int> pack;
        for (int j=0; j<p; ++j) {
            int x;
            cin >> x;
            pack.push_back(x);
        }
        sort(pack.begin(), pack.end());
        packs.push_back(pack);
    }
    
    vector<vector<ServesData>> packs_serves;
    for (int i=0; i<n; ++i) {
        vector<ServesData> pack_serves;
        for (int j=0; j<p; ++j) {
            pack_serves.push_back(getServes(packs[i][j], req[i]));
        }
        packs_serves.push_back(pack_serves);
    }
    
    int numKits = 0;
    vector<int> used(n, 0);
    while (true) {
        int min = 0, max = 999999999;
        for (int i=0; i<n; ++i) {
            min = std::max(min, packs_serves[i][used[i]].min);
            max = std::min(max, packs_serves[i][used[i]].max);
        }
        
        if (min <= max) {
            numKits++;
            for (int i=0; i<n; ++i) {
                used[i]++;
                if (used[i] >= p)
                    goto finish;
            }
        } else {
            for (int i=0; i<n; ++i) {
                if (min > packs_serves[i][used[i]].max) {
                    used[i]++;
                    if (used[i] >= p)
                        goto finish;
                }
            }
        }
    }

finish:
    cout << numKits << "\n";
}

int main(int argc, char** argv) {
    int N;
    std::cin >> N;
    std::string str;
    std::getline(std::cin, str);

    for (int i = 0; i < N; ++i) {
        solve(i + 1);
    }

    return 0;
}