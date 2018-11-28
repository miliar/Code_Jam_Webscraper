#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstring>
#include <string>

using namespace std;

int mp[5050];
char c[1010];

int main(){
    int t;
    cin >> t;
    for (int cas = 1; cas <= t; ++cas) {
        scanf("%s", c);
        memset(mp, 0, sizeof(mp));
        int n = strlen(c);
        for (int i = 0; i < n; ++i) {
            if (c[i] == '-') {
                mp[i] = 0;
            } else {
                mp[i] = 1;
            }
        }
        int k;
        cin >> k;
        int p = 0;
        
        bool flag = 1;
        int m = 0;
        
        while (p < n) {
            while (p < n && mp[p] == 1) {
                p++;
            }
            if (p < n) {
                m++;
                for (int j = p; j < p + k; ++j) {
                    mp[j] = !mp[j];
                    if (j == n) {
                        flag = 0;
                    }
                }
            }
        }

        printf("Case #%d: ", cas);
        if (!flag) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << m << endl;
        }
    }
    
}
