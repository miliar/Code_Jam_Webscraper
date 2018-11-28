#include <iostream>
using namespace std;

int num[30];

int main() {
    int T;
    cin >> T;
    for (int c = 1; c <= T; c++) {
        long long N;
        cin >> N;
        int size = 0;
        while (N) {
            num[size] = N%10;
            N /= 10;
            size++;
        }
        num[size] = 0;
        for (int i = 1; i < size; i++) {
            if (num[i - 1] < num[i]) {
                for (int j = 0; j < i; j++) num[j] = 9;
                num[i]--;
            }
        }
        printf("Case #%d: ", c);
        bool lead = true;
        for (int i = size - 1; i >= 0; i--) {
            if (lead && num[i] == 0) continue;
            lead = false;
            printf("%d", num[i]);
        }
        printf("\n");
    }
    return 0;
}
