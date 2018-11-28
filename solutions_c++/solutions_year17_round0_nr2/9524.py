
#include <bits/stdc++.h>

using namespace std;

int T, N;

int main(){
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("tidy_1.txt", "w", stdout);
    cin >> T;

    for (int c = 1; c <= T; c++){
        cin >> N;
        for (int i = N; i >= 1; i--){
            stringstream ss;
            ss << i;
            string str = ss.str();

            bool valid = true;
            for (int j = 0; j < str.size() - 1; j++){
                if (str[j + 1] < str[j]){
                    valid = false;
                    break;
                }
            }

            if (valid){
                printf("Case #%d: %d\n", c, i);
                break;
            }
        }
    }
}
