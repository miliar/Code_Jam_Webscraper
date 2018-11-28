#include <vector>
#include <map>
#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>

using namespace std;

const string path = "/Users/mac/Documents/cpp/Code Jam/";

const string IMPOSSIBLE = "IMPOSSIBLE";

string digits(long long a) {
    string r = "";
    while (a) {
        r = char((a % 10) + '0') + r;
        a /= 10;
    }
    return r;
}

long long num(string d) {
    long long r = 0;
    for (int i = 0; i < d.size(); i ++)
        r = r * 10 + (d[i] - '0');
    return r;
}

string tidy(string a) {
    for (int i = 1; i < a.size(); i ++)
        if (a[i - 1] > a[i]) {
            string first = a.substr(0, i);
            long long f = num(first);
            f --;
            first = tidy(digits(f));
            for (int j = i; j < a.size(); j ++)
                first = first + '9';
            return first;
        }
    
    return a;
}

int main() {
    freopen("/Users/mac/Documents/cpp/Code Jam/in", "r", stdin);
    freopen("/Users/mac/Documents/cpp/Code Jam/out", "w", stdout);
    
    int T;
    scanf("%d", &T);
    for (int CT = 1;  CT <= T; CT ++) {
        long long n;
        scanf("%lld", &n);
        printf("Case #%d: ", CT);
        
        string d = digits(n);
        
        printf("%s\n", tidy(d).c_str());
    }
    
    
    return 0;
}
