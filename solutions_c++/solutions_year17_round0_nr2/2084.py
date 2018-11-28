#include <bits/stdc++.h>

void test(int t) {
    long long k;
    std::string sk;
    std::cin >> sk;
    k = std::stoll(sk);
    
    for(size_t i=1; i<sk.size(); ++i) {
        if(sk[i] < sk[i-1]) {
            int j=i-1;
            while(j >= 1 && sk[j] == sk[j-1]) --j;
            k -= std::stoll(sk.substr(j+1))+1ll;
            break;
        }
    }
    std::cout << "Case #" << t << ": " << k << std::endl;
}

int main() {
    int T;
    std::cin >> T;
    for(int i=0; i<T; ++i) test(i+1);
}
