#include <cstdio>
#include <map>

using namespace std;

char inp[30][30];

void fill(int br, int bc, int er, int ec) {
    int sr = -1, sc = -1;
    for (int i = br; i <= er; i++) {
        for (int j = bc; j <= ec; j++) {
            if (inp[i][j] != '?') {
                if (sr != -1) {
                    if (i != sr) {
                        fill(br, bc, sr, ec);
                        fill(sr + 1, bc, er, ec);
                    } else {
                        fill(br, bc, er, sc);
                        fill(br, sc + 1, er, ec);
                    }
                    
                    return;
                }
                
                sr = i;
                sc = j;
            }
        }
    }
    
    char c = inp[sr][sc];
    
    for (int i = br; i <= er; i++) {
        for (int j = bc; j <= ec; j++) {
            inp[i][j] = c;
        }
    }
}

int main() {
    int t, r, c;
    scanf("%d", &t);
    
    for (int tcase = 1; tcase <= t; tcase++) {
        printf("Case #%d:\n", tcase);
        
        scanf("%d %d", &r, &c);
        
        for (int i = 0; i < r; i++) {
            scanf("%s", inp[i]);
        }
        
        fill(0, 0, r - 1, c - 1);
        
        for (int i = 0; i < r; i++) {
            printf("%s\n", inp[i]);
        }
    }
    return 0;
}
