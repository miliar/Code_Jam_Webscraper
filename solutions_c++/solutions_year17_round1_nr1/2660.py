#include <bits/stdc++.h>
using namespace std;

void preprocess() {
}

void process_testcase(const int testcase, const int should_run) {
    int r, c;
    cin>>r>>c;
    string grid[r];
    for (int i = 0; i < r; ++i)
        cin>>grid[i];

    if (should_run) {
        map<char, int> minx, maxx, miny, maxy;
        set<char> found;
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                found.insert(grid[i][j]);
            }
        }
        for (char c : found) {
            minx[c] = 1000;
            maxx[c] = 0;
            miny[c] = 1000;
            maxy[c] = 0;
        }
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                minx[grid[i][j]] = min(minx[grid[i][j]], i);
                maxx[grid[i][j]] = max(maxx[grid[i][j]], i);
                miny[grid[i][j]] = min(miny[grid[i][j]], j);
                maxy[grid[i][j]] = max(maxy[grid[i][j]], j);
            }
        }
        for (char c = 'A'; c <= 'Z'; ++c) {
            if (!found.count(c))
                continue;
            for (int i = minx[c]; i <= maxx[c]; ++i)
                for (int j = miny[c]; j <= maxy[c]; ++j)
                    grid[i][j] = c;
        }
        bool stop = false;
        while (!stop) {
            stop = true;
            for (char s : found) {
                if (minx[s] != 0) {
                    bool can = true;
                    for (int i = miny[s]; i <= maxy[s]; ++i)
                        if (grid[minx[s]-1][i] != '?')
                            can = false;
                    if (can) {
                        stop = false;
                        for (int i = miny[s]; i <= maxy[s]; ++i)
                            grid[minx[s]-1][i] = s;
                        --minx[s];
                    }
                }
                if (maxx[s]+1 != r) {
                    bool can = true;
                    for (int i = miny[s]; i <= maxy[s]; ++i)
                        if (grid[maxx[s]+1][i] != '?')
                            can = false;
                    if (can) {
                        stop = false;
                        for (int i = miny[s]; i <= maxy[s]; ++i)
                            grid[maxx[s]+1][i] = s;
                        ++maxx[s];
                    }
                }
                if (miny[s] != 0) {
                    bool can = true;
                    for (int i = minx[s]; i <= maxx[s]; ++i)
                        if (grid[i][miny[s]-1] != '?')
                            can = false;
                    if (can) {
                        stop = false;
                        for (int i = minx[s]; i <= maxx[s]; ++i)
                            grid[i][miny[s]-1] = s;
                        --miny[s];
                    }
                }
                if (maxy[s]+1 != c) {
                    bool can = true;
                    for (int i = minx[s]; i <= maxx[s]; ++i)
                        if (grid[i][maxy[s]+1] != '?')
                            can = false;
                    if (can) {
                        stop = false;
                        for (int i = minx[s]; i <= maxx[s]; ++i)
                            grid[i][maxy[s]+1] = s;
                        ++maxy[s];
                    }
                }
            }
        }

        printf("Case #%d:\n", testcase);
        for (string x : grid)
            cout<<x<<"\n";
    }
}
