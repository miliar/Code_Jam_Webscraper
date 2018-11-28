
/*

 'Tiocfaidh ár lá'

 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++) {
        string pancakes;
        int k;
        cin >> pancakes;
        scanf("%d", &k);
        bool valid = true;
        int flips = 0;
        for(int i = 0; i < pancakes.size(); i++) {
            if(pancakes[i] == '-') {
                if(i > pancakes.size() - k) {
                    valid = false;
                    printf("Case #%d: IMPOSSIBLE\n", t);
                    break;
                }
                flips++;
                for(int j = i; j < i + k; j++) {
                    pancakes[j] = pancakes[j] == '-' ? '+' : '-';
                }
            }
        }
        if(valid) {
            printf("Case #%d: %d\n", t, flips);
        }
    }

    return 0;
}