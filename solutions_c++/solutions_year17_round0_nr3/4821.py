#include <iostream>
#include <string>
#include <vector>
#include <set>
using namespace std;

int main() {
    int t; cin >> t;
    for (int i = 1; i <= t; i++) {
        int n, k; cin >> n >> k;
        multiset <int, std::greater<int> > vec;
        vec.insert(n);
        for (int j = 0; j < k - 1; j++) {
            int num = *(vec.begin());
            vec.insert(num / 2);
            vec.insert((num - 1) / 2);
            vec.erase(vec.begin());
        }
        int num = *(vec.begin());
        cout << "Case #" << i << ": " << num / 2 << " " << (num - 1) / 2<< endl;
    }
}

