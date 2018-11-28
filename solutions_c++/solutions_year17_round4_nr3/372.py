#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <queue>
#include <string>
#include <iomanip>
#include <list>
#include <algorithm>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

struct Point {
    int x, y;
};

int n;
Point laser[1005];
int v[1005];
int ansV[1005];

struct State{
    int lI;
    bool hor;
};

struct FreePoint {
    int x, y;
    vector<State> s;
};

list<FreePoint> fre;
State ans[2550];

struct Cell {
    FreePoint * p;
    int lI;
    char ch;
};

int r, c;
Cell a[55][55];

bool operator<(const FreePoint& f1, const FreePoint& f2) {
    return f1.s.size() > f2.s.size();
}

bool back(list<FreePoint>::iterator it) {
    int i;
    if(it == fre.end()) {
        for(i =0; i<n; ++i)
            ansV[i] = v[i];
        if(ansV[i] == -1)
            ansV[i] = 0;
        return true;
    }

    FreePoint p = *it;
    if(p.s.empty())
        return false;
    for(State ss : p.s) {
        int li = ss.lI;
        int horS =  ss.hor ? 0 : 1;

        if(v[li] == -1) {
            v[li] = horS;
            list<FreePoint>::iterator it2 = it;
            ++it2;
            if(back(it2))
                return true;
            v[li] = -1;
        }
        else if(v[li] == horS) {
            list<FreePoint>::iterator it2 = it;
            ++it2;
            if(back(it2))
                return true;
        }
    }
    return false;
}

bool solve() {
    //sort(fre.begin(), fre.end());
    //fre.sort();
    return back(fre.begin());
}

void read() {
    int i,j;
    fin >> r >> c;
    fre.clear();
    n=0;
    for(i=0; i<r; ++i) {
        for(j=0; j<c; ++j) {
            fin >> a[i][j].ch;
            a[i][j].p = NULL;
            a[i][j].lI = -1;

            if(a[i][j].ch == '.') {
                fre.push_back(FreePoint());
                fre.back().x = i;
                fre.back().y = j;
                a[i][j].p = &fre.back();
            }
            else if(a[i][j].ch == '-' || a[i][j].ch == '|') {
                a[i][j].ch = '-';
                a[i][j].lI = n;
                laser[n].x = i;
                laser[n].y = j;
                ++n;
            }
        }
    }
    for(i=0; i<n; ++i)
        v[i] = -1;
}



// direction = 0 - up, 1 -right, 2 - down, 3 - left

bool traverse(bool start, int i, int j, int dir, vector<FreePoint*>& p) {
    int ni = i;
    int nj = j;
    if(dir == 0)
        --ni;
    if(dir == 1)
        ++nj;
    if(dir == 2)
        ++ni;
    if(dir == 3)
        --nj;

    if(start)
        return traverse(0, ni, nj, dir, p);

    if(i<0 || j<0)
        return true;

    if(i>=r || j>=c)
        return true;

    if(a[i][j].ch == '-' || a[i][j].ch == '|')
        return false;

    if(a[i][j].ch == '.') {
        p.push_back(a[i][j].p);
        return traverse(0, ni, nj, dir, p);
    }

    if(a[i][j].ch == '#') {
        return true;
    }

    // direction = 0 - up, 1 -right, 2 - down, 3 - left
    if(a[i][j].ch == '/') {
        // up
        if(dir == 0)
            dir = 1;

        else if(dir == 2)
            dir = 3;

        else if(dir == 1)
            dir = 0;

        else if(dir == 3)
            dir = 2;
    }
    else if(a[i][j].ch == '\\')
    {
        if(dir == 0)
            dir = 3;

        else if(dir == 2)
            dir = 1;

        else if(dir == 1)
            dir = 2;

        else if(dir == 3)
            dir = 0;
    }
    ni = i;
    nj = j;
    if(dir == 0)
        --ni;
    if(dir == 1)
        ++nj;
    if(dir == 2)
        ++ni;
    if(dir == 3)
        --nj;
    return traverse(0, ni, nj, dir, p);
}

bool traversLasers() {
    int i, j;
    for(i=0; i<n; ++i) {
        for(j=0; j<2; ++j) {
            State s;
            s.lI = i;
            s.hor = (j==0);
            vector<FreePoint*> p;

            // hor
            if(j == 0) {
                vector<FreePoint*> p2;
                if(traverse(1, laser[i].x, laser[i].y, 1, p2)) {
                    p.insert(p.end(), p2.begin(), p2.end());
                }
                else {
                    if(v[i]==0)
                        return false;
                    v[i] = 1;
                }

                p2.clear();
                if(traverse(1, laser[i].x, laser[i].y, 3, p2)) {
                    p.insert(p.end(), p2.begin(), p2.end());
                }
                else {
                    if(v[i]==0)
                        return false;
                    v[i] = 1;
                }
            }
            else {
                vector<FreePoint*> p2;
                if(traverse(1, laser[i].x, laser[i].y, 0, p2)) {
                    p.insert(p.end(), p2.begin(), p2.end());
                }
                else {
                    if(v[i]==1)
                        return false;
                    v[i] = 0;
                }
                p2.clear();
                if(traverse(1, laser[i].x, laser[i].y, 2, p2)) {
                    p.insert(p.end(), p2.begin(), p2.end());
                }
                else {
                    if(v[i]==1)
                        return false;
                    v[i] = 0;
                }
            }

            for(FreePoint * pp : p) {
                pp->s.push_back(s);
            }
        }
    }
    return true;
}

int main() {
    int t, tt;
    fin >> t;
    for(tt = 1; tt <= t; ++tt) {
        read();
        bool ans1 = traversLasers();

        fout << "Case #" << tt << ": ";
        bool ans = ans1 && solve();
        if(!ans) {
            fout << "IMPOSSIBLE" << endl;
        }
        else {
            fout << "POSSIBLE" << endl;
            for(int i=0; i<r; ++i)
            {
                for(int j=0; j<c; ++j) {
                    if(a[i][j].ch == '-' || a[i][j].ch == '|') {
                        if( ansV[ a[i][j].lI ] == 0 ) {
                            fout << '-';
                        }
                        else {
                            fout << '|';
                        }
                    }
                    else {
                        fout << a[i][j].ch;
                    }
                }
                fout << endl;
            }
        }
    }
    return 0;
}
