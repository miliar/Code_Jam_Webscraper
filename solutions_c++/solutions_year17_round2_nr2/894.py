#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
using namespace std;

int mat[6][6];
int deg[6];
int inp[6];
char tochar[7] = "ROYGBV";

void addedge(int a,  int b, int c) {
    if (a > b) swap(a, b);
    mat[a][b] = c;
}
void rmedge(int a, int b) {
    if (a > b) swap(a, b);
    mat[a][b] -= 1;
}
bool cango(int a, int b) {
    if (a > b) swap(a, b);
    return (mat[a][b] > 0);
}

bool tri(int a, int b, int c) {
    int x = inp[a] - inp[b] + inp[c];
    int y = inp[b] + inp[c] - inp[a];
    int z = inp[a] + inp[b] - inp[c];
    if ((x<0) || (y<0) || (z<0) || (x & 1) || (y & 1) || (z & 1) ) return false;
    addedge(a, c, x / 2);
    addedge(c, b, y / 2);
    addedge(a, b, z / 2);
    return true;
}

void dfs(deque<int> &ans, int cur) {
    for (int i = 0; i < 6;++i) {
        if (cango(cur, i)) {
            rmedge(cur, i);
            dfs(ans, i);
        }
    }
    ans.push_front(cur);
}

int main()
{
    ios_base::sync_with_stdio(false);
    int testcase;
    cin >> testcase;
    for (int tc = 1; tc <= testcase; ++tc) {
        int N;
        bool ans = true;
        cout << "Case #" << tc << ": ";
        for (int i = 0; i < 6; ++i) {
            deg[i] = 0;
            for (int j = 0; j < 6; ++j) {
                mat[i][j] = 0;
            }
        }
        cin >> N;
        for (int i = 0; i < 6; ++i) {
            cin >> inp[i];
            inp[i] = inp[i] * 2;
            deg[i] = inp[i];
        }
        for (int i = 1; i < 6 && ans; i += 2) {
            inp[(i + 3) % 6] -= inp[i];
            if (inp[(i + 3) % 6] < 0) ans = false;
            addedge(i, (i + 3) % 6, inp[i]);
            inp[i] = 0;
        }
        if(ans) {
            bool done = false;
            vector<int> p = { 0,2,4 };
            do {
                if (tri(p[0], p[1], p[2])) {
                    done = true;
                    break;
                }
            } while (next_permutation(p.begin(), p.end()));
            if (!done) ans = false;
        }
        if (!ans) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        int st = 0;
        for (int i = 0; i < 6; ++i) {
            if (deg[i] > 0) {
                st = i;
                break;
            }
        }
        deque<int> seq;
        dfs(seq, st);
        seq.pop_front();
        if (seq.size() == N) {
            for (const int &e : seq) {
                cout << tochar[e];
            }
            cout << endl;
        }
        else {
            cout << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}