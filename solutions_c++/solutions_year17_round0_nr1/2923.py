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
    string      m_board;
    uint32_t    m_k;
public:
    int main();
private:
    void solve(uint32_t tcnum);
    uint32_t solve2();
};

int Q::main()
{
    uint32_t ntc;
    cin >> ntc;
    uint32_t i;
    for (i = 1; i <= ntc; ++i) {
        solve(i);
    }
    return 0;
}

void Q::solve(uint32_t tcnum)
{
    cin >> m_board >> m_k;
    uint32_t nflips = solve2();
    cout << "Case #" << tcnum << ": ";
    if (nflips != -1) {
        cout << nflips;
    }
    else {
        cout << "IMPOSSIBLE";
    }
    cout << "\n";
}

uint32_t Q::solve2()
{
    uint32_t nflips = 0;
    size_t i = 0;
    size_t boardsz = m_board.size();
    size_t i_end = i + boardsz - m_k;
    size_t j;
    size_t j_end;
    for (; i < i_end; ++i) {
        if (m_board[i] == '-') {
            for (j = i, j_end = j + m_k; j < j_end; ++j) {
                if (m_board[j] == '+') {
                    m_board[j] = '-';
                }
                else {
                    m_board[j] = '+';
                }
            }
            ++nflips;
        }
    }
    char ch = m_board[i];
    for (++i; i < boardsz; ++i) {
        if (m_board[i] != ch) {
            return -1;
        }
    }
    if (ch == '-') {
        ++nflips;
    }
    return nflips;
}

int
main()
{
    return Q().main();
}
