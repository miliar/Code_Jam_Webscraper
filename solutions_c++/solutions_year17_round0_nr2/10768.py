#include "deque"
#include "iostream"

using namespace std;

deque<int> d(int n) {
    deque<int> digits;

    while (n) {
        digits.push_back(n % 10);

        n /= 10;
    }

    return digits;
}

int isTidy(int n) {
    if (n < 10) return 1;

    deque<int> digits = d(n);

    int msb = digits.back();

    digits.pop_back();

    int size = digits.size();

    for (size_t i = 0; i <= size - 1; ++i) {
        int j = digits.back();

        if (j < msb) {
            return 0;
        }

        msb = j;

        digits.pop_back();
    }

    return 1;
}

int main(int argc, char const *argv[]) {

    int in, c = 0;

    int res[1001];

    for (size_t i = 0; i <= 1000; i++) {
        res[i] = isTidy(i);
    }

    while ((cin >> in).good()) {

        if (c==0) {
            c++;
            continue;
        }

        if (in < 10) {
            printf("Case #%d: %zd\n", c, in);
            c++;
            continue;
        }

        for (size_t i = in; i > 0; i--) {
            if (res[i] == 1) {
                printf("Case #%d: %zd\n", c, i);
                break;
            }
        }

        c++;

    }

    return 0;
}
