#include <fstream>
#include <string>

using namespace std;

bool f(long long n) {
    long long last = n % 10;
    n /= 10;
    while (n > 0) {
        if (n % 10 > last)
            return false;
        last = n % 10;
        n /= 10;
    }
    return true;
}


ifstream cin("input.txt");
ofstream cout("output.txt");


void rec(long long n) {
    if (n == 0)
        return;
    if (f(n))
        cout << n;
    else {
        rec(n / 10 - 1);
        cout << 9;
    }
}

int main() {
    
    int t;
    cin >> t;
    for (int j = 0; j < t; ++j) {
        long long n;
        cin >> n;
        cout << "Case #" << j + 1 << ": ";
        rec(n);
        cout << '\n';
    }

    return 0;
}