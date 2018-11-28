#include <iostream>
#include <map>

using namespace std;

void test_example(int i) {
    long long int n, k;
    cin >> n >> k;
    auto compare = [](const long long & a, const long long & b) {return a > b;};
    map<long long , long long , decltype(compare)> przedzialy(compare); // dlugosc, ilosc
    przedzialy.emplace(n+2, 1);
    while(k > 0) {
        auto biggest = przedzialy.begin();
        k -= biggest->second;
        auto s = (biggest->first - 1) / 2;
        if (k <= 0) {
            cout << "Case #" << i << ": " << max((s - 1), (biggest->first - s - 2)) << " "
                 << min((s - 1), (biggest->first - s - 2)) << endl;
            return;
        }

        przedzialy[s + 1] += biggest->second;
        przedzialy[s + (biggest->first - 1) % 2 + 1] += biggest->second;
        przedzialy.erase(przedzialy.begin());
    }
};

int main() {
    int t;
    cin >> t;
    for(auto i = 0; i < t; i++) {
        test_example(i+1);
    }
}