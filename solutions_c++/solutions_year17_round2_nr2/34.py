#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <unordered_set>
#include <unordered_map>
using namespace std;

int toInt(char a)
{
    int ret = 0;
    if (a == 'R' || a == 'O' || a == 'V') {
        ret |= 1;
    }
    if (a == 'Y' || a == 'O' || a == 'G') {
        ret |= 2;
    }
    if (a == 'B' || a == 'G' || a == 'V') {
        ret |= 4;
    }
    return ret;
}

bool check(char a, char b)
{
    return (toInt(a) & toInt(b)) == 0;
}

void embed(vector<string> &rings, string outside, string inside, int combined, int cntInside)
{
    int segment = combined - cntInside;
    for (int i = 0; i < rings.size() && segment > 0; ++ i) {
        if (rings[i] == outside) {
            if (segment == 1) {
                rings[i] = outside;
                combined -= 1;
                for (int j = 0; j < cntInside; ++ j) {
                    rings[i] += inside + outside;
                    combined -= 1;
                }

                cntInside = 0;
            } else {
                rings[i] = outside + inside + outside;
                combined -= 2;
                -- cntInside;
            }
            -- segment;
        }
    }
    assert(segment == 0);
    assert(cntInside == 0);
    assert(combined == 0);
}

int main()
{
    int tests, test = 1;
    for (scanf("%d", &tests); test <= tests; ++ test) {
        int n, R, O, Y, G, B, V;
        scanf("%d%d%d%d%d%d%d", &n, &R, &O, &Y, &G, &B, &V);
        string answer = "";
//cerr << "hi" << endl;
        if (Y + V == n) {
            if (Y == V) {
                for (int i = 0; i < Y; ++ i) {
                    answer += "YV";
                }
            }
        }
        if (R + G == n) {
            if (R == G) {
                for (int i = 0; i < R; ++ i) {
                    answer += "RG";
                }
            }
        }
        if (B + O == n) {
            if (B == O) {
                for (int i = 0; i < B; ++ i) {
                    answer += "BO";
                }
            }
        }
//cerr << "hi" << endl;
        for (int combinedR = (G == 0) ? 0 : G + 1; combinedR <= 2 * G && combinedR <= R; ++ combinedR) {
            int RR = (R - combinedR) + (combinedR - G);
            for (int combinedY = (V == 0) ? 0 : V + 1; combinedY <= 2 * V && combinedY <= Y; ++ combinedY) {
                int YY = (Y - combinedY) + (combinedY - V);
                for (int combinedB = (O == 0) ? 0 : O + 1; combinedB <= 2 * O && combinedB <= B; ++ combinedB) {
                    int BB = (B - combinedB) + (combinedB - O);

                    int nn = RR + YY + BB;
                    if (nn / 2 >= max(BB, max(RR, YY))) {
//cerr << RR << " " << YY << " " << BB << endl;
                        pair<char, int> order[3];
                        if (RR == max(BB, max(RR, YY))) {
                            order[0] = make_pair('R', RR);
                            order[1] = make_pair('Y', YY);
                            order[2] = make_pair('B', BB);
                        } else if (BB == max(BB, max(RR, YY))) {
                            order[0] = make_pair('B', BB);
                            order[1] = make_pair('Y', YY);
                            order[2] = make_pair('R', RR);
                        } else if (YY == max(BB, max(RR, YY))) {
                            order[0] = make_pair('Y', YY);
                            order[1] = make_pair('B', BB);
                            order[2] = make_pair('R', RR);
                        }

                        vector<string> rings(nn);
                        int ptr = 0;
                        for (int start = 0; start < 2; ++ start) {
                            for (int i = start; i < nn; i = (i + 2) % nn) {
                                if (rings[i] != "") {
                                    break;
                                }
                                while (order[ptr].second == 0) {
                                    ++ ptr;
                                }
                                rings[i] += order[ptr].first;
                                -- order[ptr].second;
                            }
                        }
                        assert(order[0].second == 0);
                        assert(order[1].second == 0);
                        assert(order[2].second == 0);

                        embed(rings, "B", "O", combinedB, O);
                        embed(rings, "R", "G", combinedR, G);
                        embed(rings, "Y", "V", combinedY, V);

                        for (int i = 0; i < rings.size(); ++ i) {
                            answer += rings[i];
                        }


                        if (answer.size() != n) {
                            cerr << rings.size() << endl;
                            cerr << "length !" << " " << answer.size() << " " << n << endl;
                            answer = "IMPOSSIBLE";
                        }
                        for (int i = 0; i < answer.size(); ++ i) {
                            if (!check(answer[i], answer[(i + 1) % answer.size()])) {
                                cerr << "adj wrong!" << endl;
                                answer = "IMPOSSIBLE";
                                break;
                            }
                        }

                        if (answer != "IMPOSSIBLE") {
                            goto Break;
                        }
                    }
                }
            }
        }

        Break:;

//cerr << answer <<endl;
        printf("Case #%d: %s\n", test, answer == "" ? "IMPOSSIBLE" : answer.c_str());

    }
    return 0;
}
