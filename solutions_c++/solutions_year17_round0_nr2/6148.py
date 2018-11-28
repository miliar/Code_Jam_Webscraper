#include <cstdio>
#include <deque>
using namespace std;

deque<char> digits;

void c(int num) {
    if (digits.size() == 1) {
        printf("Case #%d: %d\n", num+1, int(digits[0]));
        return;
    }
    for (int i = 0; i < digits.size()-1; i++) {
        if (digits[i] <= digits[i+1]) continue;
        for (int j = i+1; j < digits.size(); j++)
            digits[j] = 9;

        int k;
        for (k = i; k >= 0; k--) {
            digits[k]--;
            if (k > 0) {
                if (digits[k-1] <= digits[k])
                    break;
                else
                    digits[k] = 9;
            }
        }
        if (digits[0] == 0) {
            digits.pop_front();
        }
    }

    printf("Case #%d: ", num+1);
    for (int i = 0; i < digits.size(); i++) {
        putchar('0' + digits[i]);
    }
    printf("\n");
}

int main() {
    int n;
    scanf("%d\n", &n);
    for (int i = 0; i < n; i++) {
        digits.clear();
        while (true) {
            char ch = getchar();
            if (ch < '0' || ch > '9') break;
            digits.push_back(ch-'0');
        }
        c(i);
    }
}
