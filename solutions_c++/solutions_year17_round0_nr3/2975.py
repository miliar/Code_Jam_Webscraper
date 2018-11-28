#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <iostream>
#include <map>
#include <string>
#include <utility>
#include <vector>

using namespace std;

class Q
{
public:
    int main();
private:
    void solve(uint32_t tcnum);
};

struct State
{
    uint64_t    blksz;
    uint64_t    mult;
};

int Q::main()
{
    uint32_t i;
    uint32_t ntc;
    cin >> ntc;
    for (i = 1; i <= ntc; ++i) {
        solve(i);
    }
    return 0;
}

void Q::solve(uint32_t tcnum)
{
    uint64_t n;
    uint64_t k;
    cin >> n >> k;
    vector< vector<State> > states(2, vector<State>(2));
    uint32_t ridx = 0;
    uint64_t blksz;
    uint64_t mult;
    pair<uint64_t, uint64_t> res;
    if (n > k) {
        states[ridx][0].blksz = n;
        states[ridx][0].mult = 1;
        for (;; ridx ^= 1) {
            blksz = states[ridx][0].blksz;
            mult = states[ridx][0].mult;
            if (k <= mult) {
                break;
            }
            k -= mult;

            if (blksz > 2) {
                states[ridx ^ 1][0].blksz = blksz >> 1;
                if (blksz & 1) {
                    states[ridx ^ 1][0].mult = mult << 1;
                    states[ridx ^ 1][1].mult = 0;
                }
                else {
                    states[ridx ^ 1][0].mult = mult;
                    states[ridx ^ 1][1].blksz = (blksz >> 1) - 1;
                    states[ridx ^ 1][1].mult = mult;
                }
            }
            else if (blksz == 2) {
                states[ridx][1].blksz = 1;
                states[ridx][1].mult += states[ridx][0].mult;
            }
            else {
                break;
            }

            blksz = states[ridx][1].blksz;
            mult = states[ridx][1].mult;
            if (mult > 0) {
                if (k <= mult) {
                    break;
                }
                k -= mult;
                if (blksz > 1) {
                    if (blksz & 1) {
                        states[ridx ^ 1][1].blksz = blksz >> 1;
                        states[ridx ^ 1][1].mult += mult << 1;
                    }
                    else {
                        states[ridx ^ 1][0].blksz = blksz >> 1;
                        states[ridx ^ 1][0].mult += mult;
                        states[ridx ^ 1][1].blksz = (blksz >> 1) - 1;
                        if (blksz > 2) {
                            states[ridx ^ 1][1].mult += mult;
                        }
                        else {
                            states[ridx ^ 1][1].mult = 0;
                        }
                    }
                }
                else {
                    break;
                }
            }
        }

        res.first = blksz >> 1;
        if (blksz & 1) {
            res.second = res.first;
        }
        else {
            res.second = res.first - 1;
        }
    }
    cout << "Case #" << tcnum << ": " <<
        res.first << " " << res.second << "\n";
}

int
main()
{
    return Q().main();
}
