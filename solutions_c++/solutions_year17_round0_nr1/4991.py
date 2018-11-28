#include <utility>
#include <cassert>
#include <string>
#include <iostream>
using namespace std;

char flip(char c) {
    return c == '-' ? '+' : '-';
}

bool all_face_up(string s, int start, int end) {
    for (; start < end; start++) {
	if (s[start] == '-') return false;
    }
    return true;
}

pair<bool,int> pancake(string s, int i, int k) {
    int flips = 0;
    while (i < (int)s.size() && s[i] == '+') i++;
    if (i == (int)s.size()) return make_pair(true, flips);
    if (i + k > (int)s.size()) {
	if (all_face_up(s, i, s.size())) {
	    return make_pair(true,flips);
	}else {
	    return make_pair(false,flips);
	}
    }
    for (int j = 0; j < k; j++) {
	s[i+j] = flip(s[i+j]);
	flips = 1;
    }
    if (i + k > (int)s.size()) {
	if (all_face_up(s, i, s.size())) {
	    return make_pair(true,flips);
	}else {
	    return make_pair(false,flips);
	}
    }
    auto res = pancake(s,i,k);
    return make_pair(res.first, flips + res.second);
}

void test() {
    assert(pancake("-+-+-", 0, 4).first == false);
    assert(pancake("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", 0, 4).first == true);
    assert(pancake("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-", 0, 2).first == true);
    assert(pancake("+++++", 0, 4).second == 0);
    assert(pancake("---+-++-", 0, 3).second == 3);
    assert(pancake("---+-++-", 0, 3).first == true);
    assert(pancake("-", 0, 1).first == true);
    assert(pancake("-", 0, 1).second == 1);
    assert(pancake("-", 0, 2).first == false);
    assert(pancake("-", 0, 1).first == true);
    assert(pancake("-------", 0, 3).first == false);
}

int main() {
    // test();
    int t, k;
    string s;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
	cin >> s >> k;
	auto res = pancake(s, 0, k);
	cout << "Case #" << i << ": " << (res.first == true ? to_string(res.second) : "IMPOSSIBLE") << endl;
    }
}
