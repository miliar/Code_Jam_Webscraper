#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cassert>
#include <cstring>
#include <tuple>
#include <set>
#include <map>
#include <utility>

using ll = long long;
using pii = std::pair<int,int>;

const int MAX = 55;
int N, P;
int R[MAX];
int Q[MAX][MAX];
std::vector<int> serv[MAX][MAX];

bool within(int x, int y)
{
    bool lower = 9 * x <= 10 * y;
    bool upper = 10 * y <= 11 * x;
    return lower && upper;
}

bool all_within(const std::vector<int> & x, const std::vector<int> & y)
{
    for (int i = 0; i < x.size(); ++i)
        if (!within(x[i], y[i]))
            return false;
    return true;
}

int brute()
{
    for (int i = 0; i < N; ++i) {
        std::sort(Q[i], Q[i]+P);
        for (int j = 0; j < P; ++j) {
            serv[i][j].clear();
            int c = Q[i][j] / R[i];
            int lo = c-1;
            while (within(lo * R[i], Q[i][j]))
                --lo;
            if (within((lo+1)*R[i], Q[i][j]))
                serv[i][j].push_back(lo+1);
            /* if (within(c * R[i], Q[i][j])) */
            /*     serv[i][j].push_back(c); */
            int hi = c+1;
            while (within(hi * R[i], Q[i][j]))
                ++hi;
            if (within((hi-1)*R[i], Q[i][j]))
                serv[i][j].push_back(hi-1);
            std::sort(serv[i][j].begin(), serv[i][j].end());
        }
    }
    /* for (int i = 0; i < N; ++i) { */
    /*     for (int j = 0; j < P; ++j) { */
    /*         std::cout << '('; */
    /*         for (int x : serv[i][j]) */
    /*             std::cout << x << ','; */
    /*         std::cout << ") "; */
    /*     } */
    /*     std::cout << std::endl; */
    /* } */
    if (N == 1) {
        int ret = 0;
        for (int i = 0; i < P; ++i)
            if (!serv[0][i].empty())
                ++ret;
        return ret;
    } else {
        assert(N == 2);
        int ret = 0;
        int a = 0, b = 0;
        while (a < P && b < P) {
            if (serv[0][a].empty()) { ++a; continue; }
            if (serv[1][b].empty()) { ++b; continue; }
            if (serv[0][a].back() < serv[1][b].front()) { ++a; continue; }
            if (serv[0][a].front() > serv[1][b].back()) { ++b; continue; }
            ++ret;
            ++a;
            ++b;
        }
        return ret;
    }
}

int solve()
{
    for (int i = 0; i < N; ++i) {
        std::sort(Q[i], Q[i]+P);
        for (int j = 0; j < P; ++j) {
            serv[i][j].clear();
            int c = Q[i][j] / R[i];
            int lo = c-1;
            while (within(lo * R[i], Q[i][j]))
                --lo;
            if (within((lo+1)*R[i], Q[i][j]))
                serv[i][j].push_back(lo+1);
            /* if (within(c * R[i], Q[i][j])) */
            /*     serv[i][j].push_back(c); */
            int hi = c+1;
            while (within(hi * R[i], Q[i][j]))
                ++hi;
            if (within((hi-1)*R[i], Q[i][j]))
                serv[i][j].push_back(hi-1);
            std::sort(serv[i][j].begin(), serv[i][j].end());
        }
    }
    std::vector<int> pos (N);
    int ret = 0;
    bool good = true;
    while (good) {
        for (int i = 0; i < N; ++i)
            if (serv[i][pos[i]].empty()) {
                ++pos[i];
                goto nxt;
            }
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j) {
                if (i == j) continue;
                /* std::cout << i << ' ' << pos[i] << ' ' << j << ' ' << pos[j] << std::endl; */
                if (serv[i][pos[i]].back() < serv[j][pos[j]].front()) {
                    ++pos[i];
                    goto nxt;
                }
                if (serv[i][pos[i]].front() > serv[j][pos[j]].back()) {
                    ++pos[j];
                    goto nxt;
                }
            }
        ++ret;
        for (int &p : pos) ++p;
nxt:;
        for (int p : pos)
            if (p >= P)
                good = false;
    }
    return ret;

}

int main() {
    std::ios_base::sync_with_stdio(false);
    int CS;
    std::cin >> CS;
    for(int cs = 1; cs <= CS; ++cs) {
        std::cin >> N >> P;
        for (int n = 0; n < N; ++n)
            std::cin >> R[n];
        for (int n = 0; n < N; ++n)
            for (int p = 0; p < P; ++p)
                std::cin >> Q[n][p];
        /* int CASE = 7; */
        /* if (cs != CASE) continue; */
        /* if (cs == CASE) { */
        /*     std::cout << N << ' ' << P << std::endl; */
        /*     for (int n = 0; n < N; ++n) */
        /*         std::cout << R[n] << ' '; */
        /*     std::cout << std::endl; */
        /*     for (int n = 0; n < N; ++n) { */
        /*         for (int p = 0; p < P; ++p) { */
        /*             std::cout << Q[n][p] << ' '; */
        /*         } */
        /*         std::cout << std::endl; */
        /*     } */
        /* } */

        int ans = solve();
        std::cout << "Case #" << cs << ": " << ans << std::endl;
    }
}




