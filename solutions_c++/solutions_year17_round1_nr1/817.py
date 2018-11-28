#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

int r, c;
char m[30][30];
bool check() {
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            if(m[i][j] == '?')
                return false;
        }
    }
    return true;
}

void solve() {

    scanf("%d%d",&r,&c);
    for (int i = 0; i < r; ++i)
        scanf("%s",m[i]);

    int cnt = 1;
    while(cnt != 0) {
        cnt = 0;
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                if (m[i][j] == '?') {
                    if(i-1 >= 0 && m[i-1][j] != '?') {
                        m[i][j] = m[i-1][j];
                        ++cnt;
                    }
                    else if(i+1 < r && m[i+1][j] != '?') {
                        m[i][j] = m[i+1][j];
                        ++cnt;
                    }
                }
            }
        }
    }
    cnt = 1;
    while(cnt != 0) {
        cnt = 0;
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                if (m[i][j] == '?') {
                    if(j-1 >= 0 && m[i][j-1] != '?') {
                        m[i][j] = m[i][j-1];
                        ++cnt;
                    }
                    else if(j+1 < c && m[i][j+1] != '?') {
                        m[i][j] = m[i][j+1];
                        ++cnt;
                    }
                }
            }
        }
    }

    for(int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            printf("%c",m[i][j]);
        }
        printf("\n");
    }
}


int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int test;
    scanf("%d",&test);
    for (int t = 1; t <= test; ++t) {
        printf("Case #%d:\n",t);
        solve();
    }
    return 0;
}
