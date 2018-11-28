#include <iostream>
#include <cstring>
#include <queue>
#include <tuple>

char state[101][201][101][101];

int hd, ad, hk, ak, b, d;

int main() {
    int T;
    std::cin >> T;
    for(int C = 1; C <= T; C ++) {
        std::memset(state, 0, 101*201*101*101);

        std::cin >> hd >> ad >> hk >> ak >> b >> d;
        int ohd = hd;

        int result = -1;
        std::queue<std::tuple<int, int, int, int, int>> q;
        q.push(std::make_tuple(hd, ad, hk, ak, 0));
        state[hd][ad][hk][ak] = 1;
        while(q.size()) {
            auto ns = q.front(); q.pop();

            hd = std::get<0>(ns);
            ad = std::get<1>(ns);
            hk = std::get<2>(ns);
            ak = std::get<3>(ns);
            int cost = std::get<4>(ns);

            // possible actions: attack, cure, buff, debuff
            { // attack
                int nhk = hk - ad;
                if(nhk <= 0) { result = cost + 1; break; }
                int nhd = hd - ak;

                if(nhd > 0 && state[nhd][ad][nhk][ak] == 0) {
                    q.push(std::make_tuple(nhd, ad, nhk, ak, cost+1));
                    state[nhd][ad][nhk][ak] = 1;
                }
            }
            { // cure
                int nhd = ohd - ak;

                if(nhd > 0 && state[nhd][ad][hk][ak] == 0) {
                    q.push(std::make_tuple(nhd, ad, hk, ak, cost+1));
                    state[nhd][ad][hk][ak] = 1;
                }
            }
            { // buff
                int nad = ad + b;
                int nhd = hd - ak;

                if(nhd > 0 && state[nhd][nad][hk][ak] == 0) {
                    q.push(std::make_tuple(nhd, nad, hk, ak, cost+1));
                    state[nhd][nad][hk][ak] = 1;
                }
            }
            { // debuff
                int nak = ak - d;
                if(nak <= 0) nak = 0;
                int nhd = hd - nak;

                if(nhd > 0 && state[nhd][ad][hk][nak] == 0) {
                    q.push(std::make_tuple(nhd, ad, hk, nak, cost+1));
                    state[nhd][ad][hk][nak] = 1;
                }
            }
        }

        std::cout << "Case #" << C << ": ";
        if(result == -1) std::cout << "IMPOSSIBLE" << std::endl;
        else std::cout << result << std::endl;
    }
    return 0;
}
