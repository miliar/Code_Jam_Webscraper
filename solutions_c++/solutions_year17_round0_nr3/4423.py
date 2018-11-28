#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    int T;
    cin >> T;
    int counter = 0;
    while (T--) {
        int N, K;
        cin >> N >> K;
        int smin = 0, smax = 0;

        std::vector<int> v;
        v.push_back(N);

        std::make_heap(v.begin(), v.end());
        K--;
        while (K--) {
            int cur_max = v.front(); 
            std::pop_heap(v.begin(),v.end()); v.pop_back();
            v.push_back(cur_max/2); std::push_heap (v.begin(),v.end());
            v.push_back(cur_max - cur_max/2 - 1); std::push_heap (v.begin(),v.end());
        }
        int cur_max = v.front();
        smax = cur_max/2;
        smin = cur_max - 1 - smax;

        cout << "Case #" << ++counter << ": " << smax << " " << smin << "\n";
    }
    return 0;
}
