#include <iostream>

void ans(unsigned long long int n, unsigned long long int k, int i) {
        unsigned long long int l=n, r=n;
        while (k>0) {
                if (n%2 == 0) {
                        n /= 2;
                        l = n;
                        r = n-1;
                        if (k%2 != 0 && n>1) {
                                n--;
                        }
                        k /= 2;
                } else{
                        n /= 2;
                        k /= 2;
                        l = n;
                        r = n;
                }
        }
        std::cout << "Case #" << i << ": " << l << " " <<  r << '\n';
}

int main() {

        int t;
        unsigned long long int n, k;
        std::cin >> t;

        for (int i = 0; i < t; i++) {
                std::cin >> n >> k;
                ans(n,k,i+1);
        }

        return 0;
}
