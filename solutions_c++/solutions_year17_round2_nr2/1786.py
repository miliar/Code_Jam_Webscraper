#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <map>
using namespace std;

int main() {
    int T; scanf("%d", &T); int it = 0;
    while (it < T) { it++;
        printf("Case #%d: ", it);
        int N, R, O, Y, G, B, V;
        scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);

        if (V > 0 && V >= Y) {
            puts("IMPOSSIBLE");
            continue;
        } else {
            Y -= V;
            N -= V;
        }
        
        if (V > 0 && O >= B) {
            puts("IMPOSSIBLE");
            continue;
        } else {
            B -= O;
            N -= O;
        }
        
        if (G > 0 && G >= R) {
            puts("IMPOSSIBLE");
            continue;
        } else {
            R -= G;
            N -= G;
        }
        
        if (max(R, max(B, Y)) > N / 2) {
            puts("IMPOSSIBLE");
            continue;
        }

        string ans;
        for(int i = 0; i < N; i++) ans += "+";
        int r = 0; int b = 0; int y = 0;
        vector<int> order;
        for(int i = 0; i < N; i += 2) order.push_back(i);
        for(int j = 1; j < N; j += 2) order.push_back(j);
        map<char, int> cnts;
        map<char, int> used;
        char chars[3] = {'R', 'Y', 'B'};
        cnts['R'] = R;
        cnts['Y'] = Y;
        cnts['B'] = B;
        for(int i = 0; i < N; i++) {
            int last_id = -1;
            for(int j = 0; j < 3; j++) {
                if (used[chars[j]] == cnts[chars[j]]) {
                   continue; 
                }

                if (last_id == -1 || cnts[chars[last_id]] < cnts[chars[j]]) {
                    last_id = j;
                }
            }

            used[chars[last_id]] += 1;
            ans[order[i]] = chars[last_id];
        }
        cout << ans << endl;
    }
}
