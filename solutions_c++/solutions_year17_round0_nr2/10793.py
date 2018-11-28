#include <iostream>
#include <cstdio>
using namespace std;

bool isNonDecreasing(int n)
{
    int last = 10;
    while (n > 0) {
        int tail = n % 10;
        n /= 10;
        if (tail <= last) {
            last = tail;
        } else {
            return false;
        }
    }
    return true;
}

int solve(int num)
{
    while (num >= 9) {
        if (isNonDecreasing(num))
        return num;
        num--;
    }
    return num;
}

int main(int argc, char *argv[])
{
    int N;
    cin >> N;
    for (int t = 1; t <= N; ++t) {
        int num;
        cin >> num;
        printf("Case #%d: %d\n", t, solve(num));
    }
    return 0;
}
