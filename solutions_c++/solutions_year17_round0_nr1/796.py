#include <iostream>
#include <cstdio>
#include <string>

using std::cin;
using std::string;

void process(int i, string s, int k);

int main(int argc, const char * argv[]) {
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        char s[1000];
        int k;
        scanf("%s %d", s, &k);
        process(i + 1, s, k);
    }
}

void process(int test, string s, int k) {
    int res = 0;
    for (int i = 0; i < s.length(); i++) {
        if (i > s.length() - k && s[i] == '-') {
            printf("Case #%d: IMPOSSIBLE\n", test);
            return;
        }
        if (s[i] == '-') {
            res++;
            for (int j = 0; j < k; j++) {
                s[i + j] = 88 - s[i + j];
            }
        }
    }
    printf("Case #%d: %d\n", test, res);
}
