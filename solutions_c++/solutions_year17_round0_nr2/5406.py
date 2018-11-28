#include <iostream>
#include <stdio.h>
#include <string>
#include <set>

using namespace std;

int is_tidy(const string &n) {
    int q = n.length();
    if (q == 1) return 1;
    for (int i = 1; i < q ; i++) {
        if (n[i] < n[i-1]) return 0;
    }
    return 1;
}

void make_tidy(string &n) {
    const int q = n.length();
	//cout << n << " " << q;
	if (q == 1) return;
	set<char> digits;
	digits.insert(n[0]);
	int i = 1;
	for (; i < q; i++) {
		if (n[i] >= n[i-1]) {
			digits.insert(n[i]);
		}
		else break;
	}
	//cout << "st at pos " << i << endl;
	if (i == q) return;
	if ((digits.size() == 1) && ((*(digits.begin())) == '1')) {
		n = string("");
		for (int z = 0; z < q-1; z++) n += string("9");
	} else {
		n[i-1]--;
		for (int z = i; z < q; z++) n[z] = '9';
        if (is_tidy(n) == 0) make_tidy(n);
	}
}

int main(int argc, char* argv[]) {
    int T; cin >> T;
    for (int t = 0; t < T; t++) {
        string N; cin >> N;
        make_tidy(N);
        cout << "Case #" << (t+1) << ": " << N << endl;
    }
    return 0;
}
