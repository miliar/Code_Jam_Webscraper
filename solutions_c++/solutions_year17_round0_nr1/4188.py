#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int T;
    cin >> T;
    string s;
    int K;
    for(int t = 1; t <= T; t++) {
        cin >> s >> K;
        int flips = 0;
        vector<bool> flip(s.size());
        bool flipped = false;
        for(int i = 0; i + K <= s.size(); i++) {
            flipped ^= flip[i];
            if((s[i] == '-') != flipped) {
                //printf("Flipped at %d\n", i);
                flip[i+K] = true;
                flipped = !flipped;
                flips++;
            }
        }
        for(int i = s.size() - K + 1; i < s.size(); i++) {
            flipped ^= flip[i];
            if((s[i] == '-') != flipped) {
                printf("Case #%d: IMPOSSIBLE\n", t);
                break;
            }
            if(i == s.size() - 1) printf("Case #%d: %d\n", t, flips);
        }
    }
    return 0;
}
