#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;
int z[1600][800][2][2];

void select_best(int &a, int b) {
    a = min(a, b);
}

int main() {
    int T; scanf("%d", &T); int test_id = 0;
    while (test_id < T) { test_id ++;
        cerr << test_id << endl;
        printf("Case #%d: ", test_id);
        int n[2] = {0, 0};
        scanf("%d %d", &n[0], &n[1]);
        vector< vector<int> > r(2, vector<int> (1500, 0));

        for(int it = 0; it < 2; it++) {
            for(int i = 0; i < n[it]; i++) {
                int c, d;

                scanf("%d %d", &c, &d);

                for(int j = c; j < d; j++) {
                    r[it][j] = 1;
                }
            }
        }
        for(int i = 0; i <= 1500; i++) for(int j = 0; j <= 730; j++) for(int last = 0; last < 2; last++) for(int first = 0; first < 2; first++)
            z[i][j][last][first] = 80000;

        if (r[0][0] == 0)
            z[1][1][0][0] = 1;
        if (r[1][0] == 0) 
            z[1][0][1][1] = 1;

        for(int i = 1; i < 1440; i++) {
            for(int j = 0; j <= 720; j++) {
                for(int last = 0; last < 2; last++) {
                    for(int first = 0; first < 2; first++) {
                        if (r[0][i] == 0) 
                            select_best(z[i + 1][j + 1][0][first], z[i][j][last][first] + (last != 0));
                        if (r[1][i] == 0) 
                            select_best(z[i + 1][j][1][first], z[i][j][last][first] + (last != 1));
                    }
                }
            }
        }
        int ans = 800000;
        select_best(ans, z[1440][720][0][0] - 1);
        select_best(ans, z[1440][720][1][0]);
        select_best(ans, z[1440][720][0][1]);
        select_best(ans, z[1440][720][1][1] - 1);
        printf("%d\n", ans);
    }
}
