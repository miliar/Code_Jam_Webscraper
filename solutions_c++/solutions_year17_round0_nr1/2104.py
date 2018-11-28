#include <bits/stdc++.h>

int T;

void test(int t) {
    std::string s;
    int k;
    std::cin >> s >> k;
    
    int a = 0;
    for(int i=0; i<s.size(); ++i) {
        if(s[i] == '-') {
            if(i+k > s.size()) {
                std::cout << "Case #" << t << ": IMPOSSIBLE" << std::endl;
                return;
            }
            
            for(int j=i; j<i+k; ++j){
                if(s[j] == '-') s[j] = '+';
                else s[j] = '-';
            }
            ++a;
        }
    }
    
    std::cout << "Case #" << t << ": " << a << std::endl;
}

int main() {
    std::cin >> T;
    for(int i=0; i<T; ++i) test(i+1);
}
