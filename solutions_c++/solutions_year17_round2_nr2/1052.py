#include <vector>
#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>

using namespace std;

#define FIN freopen("B-small-attempt0.in", "r", stdin)
#define FOUT freopen("out.ads", "w", stdout)

const int N = 1e3 + 5;

char ans[N];

int main() {
    FIN;
    FOUT;
    int T, ncase = 0;
    scanf("%d", &T);
    while(T--) {
        int n, R, O, Y, G, B, V;
        scanf("%d", &n);
        char colors[] = "ROYGBV";
        vector< pair<int, char> > v;
        for(int i = 0; i < 6; ++i) {
            int cnt;
            scanf("%d", &cnt);
            char color = colors[i];
            v.push_back(make_pair(cnt, color));
        }
        sort(v.begin(), v.end());
        reverse(v.begin(), v.end());

//        for(int i = 0; i < 6; ++i) {
//            //printf("#%c %d\n", v[i].second, v[i].first);
//        }

        if(v[1].first + v[2].first < v[0].first) {
            strcpy(ans, "IMPOSSIBLE");
        }
        else {
            int gbr = v[2].first - (v[0].first - v[1].first);
            int gr = v[0].first - v[1].first;
            int gb = v[0].first - v[2].first;
            int m = 0;
            for(int i = 0; i < gbr; ++i) {
                ans[m++] = v[0].second;
                ans[m++] = v[1].second;
                ans[m++] = v[2].second;
            }
            for(int i = 0; i < gb; ++i) {
                ans[m++] = v[0].second;
                ans[m++] = v[1].second;
            }
            for(int i = 0; i < gr; ++i) {
                ans[m++] = v[0].second;
                ans[m++] = v[2].second;
            }
            ans[m] = '\0';
        }
        //puts("###");
        printf("Case #%d: %s\n", ++ncase, ans);
    }
    return 0;
}
