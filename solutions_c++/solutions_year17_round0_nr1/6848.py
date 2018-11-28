#include <cstdio>
#include <cstring>
#include <vector>

int main () {
    char buffer[2048];
    int t;
    std::vector<bool> s;
    int k;

    scanf("%d\n", &t);
    for(int i = 0; i < t; i++) {
        scanf("%s %d\n", buffer, &k);
        for(int j = 0; j < strlen(buffer); j++) {
            if(buffer[j] == '+') {
                s.push_back(true);
            } else {
                s.push_back(false);
            }
        }

        //printf("%lu %d:\n", s.size(), k);
        int flips = 0;
        int start = 0;
        while(true) {
            while(s[start]) {
                start++;
            }

            if(start < s.size()) {
                if(start + k - 1 < s.size()) {
                    for(int j = start; j < start + k; j++) {
                        s[j] = !s[j];
                    }
                    flips++;
                } else {
                    printf("Case #%d: IMPOSSIBLE\n", i + 1);
                    break;
                }
            } else {
                printf("Case #%d: %d\n", i + 1, flips);
                break;
            }

        }
        s.clear();
    }
}
