#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <deque>
#include <vector>

using namespace std;

char ans[1001];
int placed = 0;

void placeLoop(char s, int* co, int* cg, int* cv) {
    int i;
    if (s == 'R') {
        for (i = 0; i < *cg; i++) {
            ans[placed] = 'G';
            placed++;
            ans[placed] = 'R';
            placed++;
        }
        *cg = 0;
    }
    if (s == 'B') {
        for (i = 0; i < *co; i++) {
            ans[placed] = 'O';
            placed++;
            ans[placed] = 'B';
            placed++;
        }
        *co = 0;
    }
    if (s == 'Y') {
        for (i = 0; i < *cv; i++) {
            ans[placed] = 'V';
            placed++;
            ans[placed] = 'Y';
            placed++;
        }
        *cv = 0;
    }
    
}

int main() {
    int TT, T;
    scanf("%d", &TT);
    
    
    for (T = 1; T <= TT; T++) {
        printf("Case #%d: ", T);
        
        int n;
        int r, o, y, g, b, v;
        int cr, co, cy, cg, cb, cv;
        int i, j;
        
        scanf("%d", &n);
        scanf("%d%d%d%d%d%d", &r, &o, &y, &g, &b, &v);
        
        //check that it is possible
        cr = r;
        co = o;
        cy = y;
        cg = g;
        cb = b;
        cv = v;
        if (cg > cr || cv > cy || co > cb) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        cr -= cg;
        cy -= cv;
        cb -= co;
        if ((cr == 0 && cg > 0 && (y > 0 || b > 0)) || (cy == 0 && cv > 0 && (b > 0 || r > 0)) || (cb == 0 && co > 0 && (r > 0 || y > 0))) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        
        int biggest = max(max(cr, cy), cb);
        if (biggest > cr + cy + cb - biggest) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        
        //now build the path greedily
        placed = 0;
        char last = '0';
        char first = '0';
        while (cr + cb + cy > 0) {
            char curr = '0';
            int best = 0;
            if ((cr > best || (cr == best && first == 'R')) && last != 'R') {
                best = cr;
                curr = 'R';
            }
            if ((cb > best || (cb == best && first == 'B')) && last != 'B') {
                best = cb;
                curr = 'B';
            }
            if ((cy > best || (cy == best && first == 'Y')) && last != 'Y') {
                best = cy;
                curr = 'Y';
            }
            ans[placed] = curr;
            placed++;
            placeLoop(curr, &co, &cg, &cv);
            if (last == '0')
                first = curr;
            last = curr;
            if (curr == 'R')
                cr--;
            if (curr == 'B')
                cb--;
            if (curr == 'Y')
                cy--;
            
                
        }
        
        /*int rm = min(min(cr, cy), cb);
        cr -= rm;
        cy -= rm;
        cb -= rm;
        
        if ((cr > 0) + (cy > 0) + (cb > 0) == 1) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        int bounce = max(max(cr, cy), cb);
        if ((cr != 0 && cr != bounce) || (cy != 0 && cy != bounce) || (cb != 0 && cb != bounce)) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        
        //now working backwards, build the path
        placed = 0;
        if (bounce > 0) {
            char chars[2];
            int t = 0;
            if (cr > 0) {
                chars[t] = 'R';
                t++;
            }
            if (cb > 0) {
                chars[t] = 'B';
                t++;
            }
            if (cg > 0) {
                chars[t] = 'G';
                t++;
            }
            for (i = 0; i < bounce; i++) {
                ans[placed] = chars[0];
                placed++;
                placeLoop(chars[0], &co, &cg, &cv);
                
                ans[placed] = chars[1];
                placed++;
                placeLoop(chars[0], &co, &cg, &cv);

            }
        }
        
        if (rm > 0) {
            char chars[3] = {'R', 'B', 'Y'};
            if (placed > 0 && ans[placed-1] == 'R') {
                chars[0] = 'B';
                chars[1] = 'Y';
                chars[2] = 'R';
            }
            
            for (i = 0; i < rm; i++) {
                ans[placed] = chars[0];
                placed++;
                placeLoop(chars[0], &co, &cg, &cv);
                
                ans[placed] = chars[1];
                placed++;
                placeLoop(chars[1], &co, &cg, &cv);
                
                ans[placed] = chars[2];
                placed++;
                placeLoop(chars[2], &co, &cg, &cv);
                
            }
        }*/
        
        placeLoop('R', &co, &cg, &cv);
        placeLoop('Y', &co, &cg, &cv);
        placeLoop('B', &co, &cg, &cv);
        
        ans[placed] = 0;
        printf("%s\n", ans);
        

    }
}
        