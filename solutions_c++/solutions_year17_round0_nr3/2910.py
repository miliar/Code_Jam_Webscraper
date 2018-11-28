#include <iostream>
#include <map>

void Work(long long n, long long k, long long &y, long long &z) {
    std::map<long long, long long> m;
    m[n] = 1;
    while (k > 0) {
        auto it = m.end();
        --it;
        long long a = it->first, b = it->second;
        m.erase(it);
        z = (a - 1) / 2;
        y = z;
        if (a % 2 == 0)
            ++y;
        m[y] += b;
        m[z] += b;
        k -= b;
    }
}

void Output(int test, long long y, long long z) {
    std::cout << "Case #" << test << ": " << y << " " << z << std::endl;
}

int main() {
    int t;
    std::cin >> t;
    for (int i = 1; i <= t; ++i) {
        long long n, k, y, z;
        std::cin >> n >> k;
        Work(n, k, y, z);
        Output(i, y, z);
    }
    return 0;
}

