#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int T;
    cin >> T; 
    int n, k;
    for (int I = 1; I <= T; ++I)
    {
        cin >> n >> k;
        k--;
        int level_count = 1, range;
        while (level_count-1 < k) level_count <<= 1;
        if (level_count - 1 == k)
            range = ceil((n - (level_count-1)) * 1.0 / level_count);
        else
        {
            level_count >>= 1;
            range = floor((n - (level_count-1)) * 1.0 / level_count);
            int num_bigger_range = (n-level_count+1) - range * level_count;
            int more_people = k - (level_count-1);
            if (more_people < num_bigger_range) range++;
        }
        range--;
        int mi = floor(range / 2.0), ma = ceil(range / 2.0);
        cout << "Case #" << I << ": "<< ma << " " << mi << endl;
    }
}
