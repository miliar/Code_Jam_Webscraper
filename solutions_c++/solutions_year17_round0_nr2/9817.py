#include <iostream>
#include <string>
using namespace std;

string n;

void decrstr(int j) {
    if (n[j] == '0') {
        n[j] = '9';
        decrstr(j - 1);
    }
    else
        n[j] -= 1;
    if (n[0] == '0')
        n.erase(0, 1);
}

int main() {
    int t;

    cin >> t;
    for (int i = 0; i < t; ++i) {
        cin >> n;
        int l = n.length();
        bool flag = false;
	    int c = -1;
        for (int j = 1; j <l; j++) {
            if (!flag)
                if (n[j] < n[j - 1]) {
                    flag = true;
	                c = 0;
	                for (int k = j - 1; k > 0; --k) {
		                if (n[k] > n[k-1]) {
			                c = k;
			                j = k + 1;
			                break;
		                }
	                }
	                if (c == 0)
		                j = 1;
                }

            if (flag)
                n[j] = '9';
        }
	    decrstr(c);
        cout << "Case #" << i + 1 << ": " << n << endl;
    }
    return 0;
}