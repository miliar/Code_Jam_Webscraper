//
// Created by Denis Mukhametianov on 08.04.17.
//

#include <cstdio>
#include <iostream>
#include <string>
#include <vector>


using namespace std;


string s[50];
int minx[500], miny[500], maxx[500], maxy[500];


bool isEmptyColumn(int x, int from, int to) {
    for(int i = from; i <= to; i++) {
        if(s[x][i] != '?')
            return false;
    }
    return true;
}


void fillColumn(int x, int from, int to, char c) {
    for(int i = from; i <= to; i++) {
        s[x][i] = c;
    }
}

bool isEmptyRow(int x, int from, int to) {
    for(int i = from; i <= to; i++) {
        if(s[i][x] != '?')
            return false;
    }
    return true;
}


void fillRow(int x, int from, int to, char c) {
    for(int i = from; i <= to; i++) {
        s[i][x] = c;
    }
}


void solve(int testNumber) {
    printf("Case #%d:\n", testNumber);
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        cin >> s[i];
    }
    for(char c = 'A'; c <= 'Z'; c++) {
        minx[c] = miny[c] = n + m;
        maxx[c] = maxy[c] = -1;
    }
    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++) {
            minx[s[i][j]] = min(minx[s[i][j]], i);
            maxx[s[i][j]] = max(maxx[s[i][j]], i);
            miny[s[i][j]] = min(miny[s[i][j]], j);
            maxy[s[i][j]] = max(maxy[s[i][j]], j);
        }
    for(char c = 'A'; c <= 'Z'; c++)
        if(maxx[c] != -1) {
            for(int i = minx[c]; i <= maxx[c]; i++)
                for(int j = miny[c]; j <= maxy[c]; j++)
                    s[i][j] = c;
        }
    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
            if(maxx[s[i][j]] != -1) {
                char c = s[i][j];
                while(miny[c] > 0 && isEmptyRow(miny[c] - 1, minx[c], maxx[c])) {
                    fillRow(miny[c] - 1, minx[c], maxx[c], c);
                    miny[c]--;
                }
                while(maxy[c] < m && isEmptyRow(maxy[c] + 1, minx[c], maxx[c])) {
                    fillRow(maxy[c] + 1, minx[c], maxx[c], c);
                    maxy[c]++;
                }
                while(minx[c] > 0 && isEmptyColumn(minx[c] - 1, miny[c], maxy[c])) {
                    fillColumn(minx[c] - 1, miny[c], maxy[c], c);
                    minx[c]--;
                }
                while(maxx[c] < n && isEmptyColumn(maxx[c] + 1, miny[c], maxy[c])) {
                    fillColumn(maxx[c] + 1, miny[c], maxy[c], c);
                    maxx[c]++;
                }
                maxx[s[i][j]] = -1;
            }
    for(int i = 0; i < n; i++)
        printf("%s\n", s[i].c_str());
}


void runA() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int tc;
    cin >> tc;
    for (int i = 0; i < tc; i++)
        solve(i + 1);
}