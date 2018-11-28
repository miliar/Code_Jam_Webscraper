#include <utility>
#include <cassert>
#include <string>
#include <stack>
#include <iostream>
#include <deque>
using namespace std;

void set_to_nine(string& s, int i) {
    for (; i < (int)s.size(); ++i) {
	s[i] = '9';
    }
}

int to_int(char c) {
    return c -'0';
}

long tidy(string s) {
    if ((int)s.size() <= 1) return stol(s);
    for (int i = (int)s.size()-2; i >= 0; --i) {
	if (to_int(s[i]) > to_int(s[i+1])) {
	    set_to_nine(s, i+1);
	    s[i] = (to_int(s[i]) - 1) + '0';
	}
    }
    return stol(s);
}

void test() {
    assert(to_int('9') == 9);
    assert(tidy("1100") == 999);
    assert(tidy("111111111111111110") == 99999999999999999);
    assert(tidy("7") == 7);
    assert(tidy("132") == 129);
    assert(tidy("1000") == 999);
}

int main() {
    // test();
    int t;
    string k;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> k;
        auto res = tidy(k);
        cout << "Case #" << i << ": " <<  res << endl;
    }
}
