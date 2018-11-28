#include <iostream>
#include <stack>
using namespace std;
unsigned long long calc (unsigned long long n) {
    unsigned long long nc = n;
    stack<int> s;
    while (nc) {
        s.push(nc % 10);
        nc /= 10;
    }
    int dnc = s.top();
    unsigned long long ret = dnc;
    s.pop();
    while(!s.empty() && dnc <= s.top()) {
        ret = ret * 10 + s.top();
        dnc = s.top();
        s.pop();
    }
    int i =0;
    while (i < s.size()) {
        ret *= 10;
        i += 1;
    }
    if (!s.empty()) {
        ret -= 1;
    }
    nc = ret;
    int d = nc % 10;
    nc = nc / 10;
    unsigned long long m = 1;
    while (nc) {
        int dp = nc % 10;
        if (dp > d) {
            ret -= m * (d + 1);
            d = dp - 1;
        }
        else {
            d = dp;
        }
        m *= 10;
        nc = nc / 10;
    }
    return ret;
}

int main()
{
    int T;
    cin >> T;
    for (int i=0; i<T; ++i) {
        unsigned long long N;
        cin >> N;
        cout << "Case #" << i + 1 << ": " << calc(N) << endl;
    }
}
