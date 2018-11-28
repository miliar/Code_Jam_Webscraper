#define NDEBUG
NDEBUG


#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <cstring>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <memory>
#include <queue>
#include <random>

#define FOR(i, n) for (int i = 0; i < (n); ++i)


#define all(c) c.begin(), c.end()


using namespace std;

// TC_REMOVE_BEGIN
/// caide keep
bool __hack = std::ios::sync_with_stdio(false);
/// caide keep
auto __hack1 = cin.tie(nullptr);
// TC_REMOVE_END


// Section with adoption of array and vector algorithms.


namespace template_util {
    

    constexpr int bytecount(uint64_t x) {
        return x ? 1 + bytecount(x >> 8) : 0;
    }

    template<int N>
    struct bytetype {
        
    };

    
    /// caide keep
    template<uint64_t N>
    struct minimal_uint : bytetype<bytecount(N)> {
    };
}


template<class T>
T next(istream& in) {
    T ret;
    in >> ret;
    return ret;
}


int n_seats, n_customers, n_tickets;
vector<int> pos, idx;
vector<vector<int>> positions;

bool canSolve(int rides, int& promos) {
    positions = vector<vector<int>>(n_customers);
    promos = 0;
    FOR(i, n_tickets) {
        positions[idx[i]].push_back(pos[i]);
    }
    FOR(i, n_customers) {
        sort(all(positions[i]));
        reverse(all(positions[i]));
        if (positions[i].size() > rides) {
            return false;
        }
    }
    vector<int> count_seats(n_seats, rides);
    FOR(i, n_customers) {
        for (int x : positions[i]) {
            if (count_seats[x]) {
                --count_seats[x];
            } else {
                bool ok = false;
                for (int j = x - 1; j >= 0; --j) {
                    if (count_seats[j]) {
                        --count_seats[j];
                        ok = true;
                        break;
                    }
                }
                if (ok) {
                    ++promos;
                } else {
                    return false;
                }
            }
        }
    }
    return true;
}

void solveTest(istream& in, ostream& out) {
    int le = 1, ri = n_tickets - 1, res = n_tickets;
    while (le <= ri) {
        int e = (le + ri) / 2;
        int val;
        if (canSolve(e, val)) {
            res = e;
            ri = e - 1;
        } else {
            le = e + 1;
        }
    }
    int val;
    canSolve(res, val);
    out << res << ' ' << val << endl;
}

void inputData(istream& in) {
    n_seats = next<int>(in);
    n_customers = next<int>(in);
    n_tickets = next<int>(in);
    pos = vector<int>(n_tickets);
    idx = vector<int>(n_tickets);
    FOR(i, n_tickets) {
        pos[i] = next<int>(in) - 1;
        idx[i] = next<int>(in) - 1;
    }
}

void solve(istream& in, ostream& out, const int test_id = -1) {
    int test = next<int>(in);
    FOR(t, test) {
        inputData(in);
        if (t == test_id || test_id == -1) {
            out << "Case #" << t + 1 << ": ";
            solveTest(in, out);
        }
    }
}
#include <fstream>


int main(int argc, char* argv[]) {
    if (argc == 0) {
        solve(cin, cout);
    } else {
        ifstream in("in.txt");
        int test_id = stoi(argv[1]);
        solve(in, cout, test_id);
    }
    return 0;
}

