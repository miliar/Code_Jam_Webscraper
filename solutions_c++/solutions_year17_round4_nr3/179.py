#include <cstdint>
#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;

struct candidate {
    int x;
    int y;
    char target;
    
    candidate() : x(-1), y(-1) {}
};

int R, C;
vector<string> m;

char reverse(char c) {
    return c == '-' ? '|' : '-';
}

tuple<int, int, char> ray(int x, int y, int offx, int offy) {
    while (true) {
        x += offx;
        y += offy;
        if (x < 0 || x >= R || y < 0 || y >= C) break;
        if (m[x][y] == '#') break;
        if (m[x][y] == '|' || m[x][y] == '-' || m[x][y] == '?') return make_tuple(x, y, offx == 0 ? '|' : '-');
        if (m[x][y] == '/') {
            if (offx == 0) {
                offx = offy == 1 ? -1 : 1;
                offy = 0;
            } else {
                offy = offx == 1 ? -1 : 1;
                offx = 0;
            }
        } else if (m[x][y] == '\\') {
            if (offx == 0) {
                offx = offy == 1 ? 1 : -1;
                offy = 0;
            } else {
                offy = offx == 1 ? 1 : -1;
                offx = 0;
            }
        }

    }
    return make_tuple(-1, -1, '?');
}

void solve() {
    m.clear();
    vector<pair<int, int>> ps;
    cin >> R >> C;
    for (int i = 0; i < R; i++) {
        string l;
        cin >> l;
        for (int j = 0; j < C; j++) {
            if (l[j] == '-' || l[j] == '|') {
                ps.emplace_back(i, j);
                l[j] = '?';
            }
        }
        m.push_back(l);
    }

//cout << endl;
//for (int i = 0; i < R; i++) cout << m[i] << endl;

    for (int i = 0; i < ps.size(); i++) {
        int x, y;
        int other_x, other_y;
        char avoid;
        tie(x, y) = ps[i];
        tie(other_x, other_y, avoid) = ray(x, y, 1, 0);
        if (other_x >= 0) {
            m[x][y] = '-';
            m[other_x][other_y] = avoid;
        }
        tie(other_x, other_y, avoid) = ray(x, y, -1, 0);
        if (other_x >= 0) {
            m[x][y] = '-';
            m[other_x][other_y] = avoid;
        }
        tie(other_x, other_y, avoid) = ray(x, y, 0, 1);
        if (other_x >= 0) {
            m[x][y] = '|';
            m[other_x][other_y] = avoid;
        }
        tie(other_x, other_y, avoid) = ray(x, y, 0, -1);
        if (other_x >= 0) {
            m[x][y] = '|';
            m[other_x][other_y] = avoid;
        }
    }

    for (int i = 0; i < ps.size(); i++) {
        int x, y;
        int other_x, other_y;
        char avoid;
        tie(x, y) = ps[i];
        if (m[x][y] == '|') {
            tie(other_x, other_y, avoid) = ray(x, y, 1, 0);
            if (other_x >= 0) {
                cout << "IMPOSSIBLE" << endl; return;
            }
            tie(other_x, other_y, avoid) = ray(x, y, -1, 0);
            if (other_x >= 0) {
                cout << "IMPOSSIBLE" << endl; return;
            }
        } else if (m[x][y] == '-') {
            tie(other_x, other_y, avoid) = ray(x, y, 0, 1);
            if (other_x >= 0) {
                cout << "IMPOSSIBLE" << endl; return;
            }
            tie(other_x, other_y, avoid) = ray(x, y, 0, -1);
            if (other_x >= 0) {
                cout << "IMPOSSIBLE" << endl; return;
            }
        }
    }

    bool progress = true;
    while (progress) {
        progress = false;
        for (int x = 0; x < R; x++) {
            for (int y = 0; y < C; y++) {
                if (m[x][y] != '.') continue;
                
                candidate c1, c2;
                int ox, oy;
                char avoid;
                tie(ox, oy, avoid) = ray(x, y, 1, 0);
                if (ox >= 0) {
                    if (m[ox][oy] == '?') {
                        c1.x = ox;
                        c1.y = oy;
                        c1.target = reverse(avoid);
                    } else if (m[ox][oy] != avoid) {
                        continue;
                    }
                }
                tie(ox, oy, avoid) = ray(x, y, -1, 0);
                if (ox >= 0) {
                    if (m[ox][oy] == '?') {
                        c1.x = ox;
                        c1.y = oy;
                        c1.target = reverse(avoid);
                    } else if (m[ox][oy] != avoid) {
                        continue;
                    }
                }
                tie(ox, oy, avoid) = ray(x, y, 0, 1);
                if (ox >= 0) {
                    if (m[ox][oy] == '?') {
                        c2.x = ox;
                        c2.y = oy;
                        c2.target = reverse(avoid);
                    } else if (m[ox][oy] != avoid) {
                        continue;
                    }
                }
                tie(ox, oy, avoid) = ray(x, y, 0, -1);
                if (ox >= 0) {
                    if (m[ox][oy] == '?') {
                        c2.x = ox;
                        c2.y = oy;
                        c2.target = reverse(avoid);
                    } else if (m[ox][oy] != avoid) {
                        continue;
                    }
                }
//if (x == 1 && y == 7) {

                if (c1.x < 0 && c2.x < 0) {
                    cout << "IMPOSSIBLE" << endl; return;
                } else if (c1.x < 0) {
                    m[c2.x][c2.y] = c2.target;
                    progress = true;
                } else if (c2.x < 0) {
                    m[c1.x][c1.y] = c1.target;
                    progress = true;
                } else if (c1.x != c2.x || c1.y != c2.y) {
                    // TODO
                }
            }
        }
    }

//cout << endl;
//for (int i = 0; i < R; i++) cout << m[i] << endl;

    progress = true;
    while (progress) {
        progress = false;
        for (int x = 0; x < R; x++) {
            for (int y = 0; y < C; y++) {
                if (m[x][y] != '.') continue;
                
                candidate c1, c2;
                int ox, oy;
                char avoid;
                tie(ox, oy, avoid) = ray(x, y, 1, 0);
                if (ox >= 0) {
                    if (m[ox][oy] == '?') {
                        c1.x = ox;
                        c1.y = oy;
                        c1.target = reverse(avoid);
                    } else if (m[ox][oy] != avoid) {
                        continue;
                    }
                }
                tie(ox, oy, avoid) = ray(x, y, -1, 0);
                if (ox >= 0) {
                    if (m[ox][oy] == '?') {
                        c1.x = ox;
                        c1.y = oy;
                        c1.target = reverse(avoid);
                    } else if (m[ox][oy] != avoid) {
                        continue;
                    }
                }
                tie(ox, oy, avoid) = ray(x, y, 0, 1);
                if (ox >= 0) {
                    if (m[ox][oy] == '?') {
                        c2.x = ox;
                        c2.y = oy;
                        c2.target = reverse(avoid);
                    } else if (m[ox][oy] != avoid) {
                        continue;
                    }
                }
                tie(ox, oy, avoid) = ray(x, y, 0, -1);
                if (ox >= 0) {
                    if (m[ox][oy] == '?') {
                        c2.x = ox;
                        c2.y = oy;
                        c2.target = reverse(avoid);
                    } else if (m[ox][oy] != avoid) {
                        continue;
                    }
                }

                if (c1.x >= 0 && c2.x >= 0) {
                    m[c1.x][c1.y] = c1.target;
                    progress = true;
                }
            }
        }
    }

    for (int x = 0; x < R; x++) {
        for (int y = 0; y < C; y++) {
            if (m[x][y] == '?') m[x][y] = '|';
        }
    }

    cout << "POSSIBLE" << endl;
    for (int i = 0; i < R; i++) cout << m[i] << endl;
}

int main() {
    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; testcase++) {
        cout << "Case #" << testcase << ": ";
        solve();
    }
    return 0;
}
