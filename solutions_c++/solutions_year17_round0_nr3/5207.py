#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>

int main() {
    int t;
    std::cin >> t;
    for (int i = 1; i <= t; i++) {
        int n, k;
        std::cin >> n >> k;
        int log2k= int(log2(k)); 
        int hk = log2k + 1; // the layer that k-th person will be at
        int nk = int(exp2(hk - 1)); // the number of nodes at hk layer
        int sk = n - int(exp2(log2k)) + 1;
        int n_large = sk % nk;
        int n_small = nk - n_large;
        int small = sk / nk;
        int large = small + 1;
        int k_shunwei = k - int(exp2(log2k)) + 1;
        int gap = k_shunwei > n_large ? small : large;
        int ls = gap / 2 - (gap % 2 == 0 ? 1 : 0);
        int rs = gap / 2;
        
        std::cout << "Case #" << i << ": " << std::max(ls, rs) << " " << std::min(ls, rs) << std::endl;
    }
    return 0;
}

