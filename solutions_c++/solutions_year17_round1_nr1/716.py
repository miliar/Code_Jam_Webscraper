#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
#include <cassert>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <utility>
#include <cmath>
#include <bitset>
#include <climits>
#include <iomanip>
#include <fstream>
#include <unordered_set>
#include <unordered_map>
#include <cstdio>
#include <cstring>

using namespace std;

#define ll long long
#define N (ll)(1e6+5)
#define INF (ll)(1e18+3)
#define EPS (1e-9)
#define PI (3.14159265358979323846)
#define ld double
#define MOD (ll)(1e9+7)

int main() {
    ifstream in("in.txt");
    ofstream out("out.txt");
    int t;
    in >> t;
    
    for (int i = 0; i < t; i++) {
        out << "Case #" << i + 1 << ":\n";
        int r, c;
        in >> r >> c;
        char grid[r][c];
        int upi = -1;
        for (int i = 0; i < r; ++i) {
            char left = ' ';
            for (int j = 0; j < c; ++j) {
                char ch;
                in >> ch;
                if (ch != '?') {
                    if  (left == ' ')
                        for (int k = 0; k < j; k++)
                            grid[i][k] = ch;
                    left = ch;
                }
                if (ch == '?') ch = left;
                grid[i][j] = ch;
            }
            if (left != ' ') {
                if (upi == -1)
                    for (int k = 0; k < i; k++)
                        for (int l = 0; l < c; l++)
                            grid[k][l] = grid[i][l];
                upi = i;
            }
            else if (upi != -1)
                for (int j = 0; j < c; j++)
                    grid[i][j] = grid[upi][j];
        }
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j)
                out << grid[i][j];
            out << endl;
        }
    }
    
    in.close();
    out.close();
}
