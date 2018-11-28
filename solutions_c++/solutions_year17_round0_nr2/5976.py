#include <iostream>
#include <string>
#include <algorithm>

inline bool isTidy(std::string s) {
    int n = s.size();
    for (int i = 1; i < n; ++i)
        if (s[i] < s[i-1]) return false;
    return true;
}

long long f(long long s) {
    long long ret;
    if (isTidy(std::to_string(s))) return s;

    ret = s;
    ret /= 10;
    ret--;
    if (!isTidy(std::to_string(ret)))
        ret = f(ret);    
    ret = ret * 10 + 9;
    return ret;

    
}

int main() {
    int n;
    std::cin >> n;
    std::vector<long long> v(n);
    long long s;
    for (int i = 0; i < n; ++i) {        
        std::cin >> s;
        std::cout << "Case #" << i+1 << ": " << f(s) << std::endl;
    }

} 