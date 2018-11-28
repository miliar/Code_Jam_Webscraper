#include <iostream>
#include <limits>

using namespace std;

bool isValid(uint64_t n) {
    int past = n % 10;
    n /= 10;
    while(n) {
        int last = n % 10;
        n /= 10;
        if(last > past) {
            return false;
        }
        past = last;
    }
    return true;
}

int cnt(uint64_t n) {
    int d = 0;
    while(n) {
        d++;
        n /= 10;
    }
    return d;
}

uint64_t nextLower(uint64_t n) {
    int d = cnt(n);
    int digits[d];

    for(int i = 0; i < d; i++) {
        digits[d - i - 1] = n % 10;
        n /= 10;
    }

    int difference = 0;
    int past = digits[0];

    for(int i = 1; i < d; i++) {
        if(digits[i] < past) {
            difference = i - 1;
            break;
        }
        past = digits[i];
    }

    digits[difference] -= 1;
    for(int i = difference + 1; i < d; i++) {
        digits[i] = 9;
    }

    n = 0;
    for(int i = 0; i < d; i++) {
        n = n * 10 + digits[i];
    }

    return n;
}

void solve(int T) {
    uint64_t N;
    cin >> N;

    while(!isValid(N)) {
        N = nextLower(N);
    }
    //while(!isValid(N)) { N--; }

    cout << "Case #" << T << ": " << N << endl;
}

int main()
{
    int T;
    cin >> T;
    for(int i = 1; i <= T; i++) {
        solve(i);
    }
    return 0;
}
