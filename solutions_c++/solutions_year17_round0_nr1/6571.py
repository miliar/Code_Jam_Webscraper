#include <iostream>
#include <string>
using namespace std;

void flip(string *s, int i) {
	if ((*s)[i] == '-') {
		(*s)[i] = '+';
	} else if ((*s)[i] == '+') {
		(*s)[i] = '-';
	}
}

void flip_k(string *s, int i, int k) {
	int it1;
	for(it1 = 0; it1 < k; it1++) {
		flip(s, i + it1);
	}
}

int main() {
	int t,k,i,n_flips,j;
	bool b1;
	string s;
	cin >> t;
	int len_s;
	for(j = 0; j < t; j++) { // test_cases
		cin >> s >> k;
		n_flips = 0;
		b1 = false;
		len_s = s.size();
		//cout << "STRING "<< s << endl;
		//cout << "K "<< k << endl;

		for(i = 0; i < len_s-(k-1); i++) {
			if (s[i] == '-') {
				flip_k(&s,i,k);
				n_flips ++;
				//cout << i+1 <<" "<< s << endl;
			}
		}
		for(i= len_s - (k-1); i < len_s; i++) {
			if (s[i] == '-') {
				b1 = true;
				break;
			}
		}
		// output
		cout << "CASE #" << j + 1 <<": ";
		if (b1 == false) {
			cout << n_flips;
		} else {
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}
	return 0;
}
