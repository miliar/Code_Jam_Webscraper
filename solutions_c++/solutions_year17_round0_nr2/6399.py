#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {

        int P;
        cin >> P;
        for (int p = 1; p <= P; p++) {
                cout << "Case #" << p << ": ";
		string x;
		cin >> x;
		if (x.size() <= 1) {
			cout << x << endl;
		} else {
			x = "000" + x;
			start:
			for (int i = 0; i < x.size()-1; i++) {
				if (x[i] > x[i+1]) {
					for (int j = i+1 ; j < x.size() ; j++) {x[j] = '9';}
					x[i]--;
					goto start;
					// while (i > 0) { x[i]-- ; if (x[i] >= x[i-1]) { goto done; } } 
				}
			}
			done:
			x = x.substr(x.find_first_not_of("0"),9999);
			cout << x << endl;
		}
        }

}

