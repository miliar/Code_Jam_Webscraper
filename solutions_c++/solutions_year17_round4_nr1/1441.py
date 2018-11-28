#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

template<class T>
inline T read() {
    T value;
    std::cin >> value;
    return value;
}

int main() {
    auto T = read<int>();
    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        int N; std::cin >> N;
        int P; std::cin >> P;
        int G[4] = {0};
        for (int i = 0; i < N; ++i) {
            int g; std::cin >> g;
            ++G[g % P];
        }
        int count = G[0]; // use every mod 0 group, they are free
        switch (P) {
            case 2: {
                // every 2 other groups
                count += (G[1] + 1) / 2;
                break;
            }
            case 3: {
                // use every group from mod 2 and 1 first
                int c = std::min(G[1], G[2]);
                count += c;
                G[1] -= c;
                G[2] -= c;
                // then every 3 other groups if any left
                count += (G[1] + 2) / 3;
                count += (G[2] + 2) / 3;
                break;
            }
            case 4: {
                // use every 2 groups from mod 2
                int c = G[2] / 2;
                count += c;
                G[2] -= c * 2;
                // now G[2] is 0 or 1

                // use every 2 groups, mod 3 + mod 1
                c = std::min(G[3], G[1]);
                count += c;
                G[1] -= c;
                G[3] -= c;
                // now G[3] or G[1] is 0

                // use every 3 groups, 1x mod 2 + 2x mod 1
                c = std::min(G[2], G[1] / 2);
                count += c;
                G[2] -= c;
                G[1] -= c * 2;
                // use every 3 groups, 1x mod 2 + 2x mod 3
                c = std::min(G[2], G[3] / 2);
                count += c;
                G[2] -= c;
                G[3] -= c * 2;
                // if G[2] is still 1 then G[3] or G[1] is less than 2

                // use every 4x mod 1
                c = G[1] / 4;
                count += c;
                G[1] -= c * 4;

                // use every 4x mod 3
                c = G[3] / 4;
                count += c;
                G[3] -= c * 4;

                // if any left, then only 1 of them will get fresh chocolate
                if (G[1] > 0 || G[2] > 0 || G[3] > 0) {
                    ++count;
                }
                break;
            }
            default: {
                fprintf(stderr, "Unexpected P = %d\n", P);
                return 1;
            }
        }
        printf("Case #%d: %d\n", caseNum, count);
    }
    return 0;
}
