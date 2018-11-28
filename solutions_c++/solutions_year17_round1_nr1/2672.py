#include <bits/stdc++.h>

using namespace std;

const int N = 115;

int grid[N][N];

int c, r;

bool fill(int x1, int y1, int x2, int y2, bool should, int letter) {
    if (x1+x2 > r) return false;
    if (y1+y2 > c) return false;
    bool found = false;;
    for(int i=x1;i<x1+x2;i++) {
        for(int j=y1;j<y1+y2;j++) {
            if (grid[i][j] != 0 && grid[i][j] != letter) return false;
            if (grid[i][j] == letter) {
                found = true;
            }
        }
    }
    if (!should) return found;
    for(int i=x1;i<x1+x2;i++) {
        for(int j=y1;j<y1+y2;j++) {
            grid[i][j] = letter;
        }
    } 
    return true;
}

int main() {
    int t;
    scanf("%d", &t);
    int te = 1;
    while(t--) {
        set<int> used;
        scanf("%d %d", &r, &c);
        getchar();
        for(int i=0;i<r;i++) {
            for(int j=0;j<c;j++) {
                char c = getchar();
                if (c == '?') grid[i][j] = 0;
                else grid[i][j] = c;
            }
            getchar();
        }
        for(int i=0;i<r;i++) {
            for(int j=0;j<c;j++) {
                if (grid[i][j] != 0 && used.find(grid[i][j]) == used.end()) {
                    int mxc=0, mxr=0;
                    int mx0=0, my0=0;
                    for(int x0=0;x0<r;x0++) {
                        for(int y0=0;y0<=c;y0++) {
                            for(int x=1;x<=r;x++) {
                                for(int y=0;y<=c;y++) {
                                    if (x0 > i || x0+x < i+1 || y0 > j || y0+y < j+1) continue;
                                    bool t = fill(x0, y0, x, y, false, grid[i][j]);
                                    //printf("%c %d %d %d %d = %d\n", grid[i][j], x0, y0, x, y, t);
                                    //getchar(); 
                                    if (t) {
                                        if (mxc*mxr < x*y) {
                                            mxr = x;
                                            mxc = y;
                                            mx0 = x0;
                                            my0 = y0;
                                        }
                                    }
                                }
                            }
                        }
                    }
                    fill(mx0, my0, mxr, mxc, true, grid[i][j]);
                    used.insert(grid[i][j]);
                }
            }
        }
        printf("Case #%d:\n", te++);
        for(int i=0;i<r;i++) {
            for(int j=0;j<c;j++) {
                printf("%c", grid[i][j] == 0? '?' : grid[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}

