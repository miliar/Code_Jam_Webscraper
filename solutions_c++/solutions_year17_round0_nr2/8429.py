#include <iostream>
#include <string>

using namespace std;

int main() {
    int T = 0;

    cin >> T;

    for (int i = 1; i <= T; i++) {
        string N = "";
        char biggest;
        unsigned int pos = 0;

        cout << "Case #" << i << ": ";

        cin >> N;

        biggest = N.at(0);

        for (; pos < N.size(); pos++) {
        	if (N.at(pos) > biggest) {
        		biggest = N.at(pos);
        	}
        	else if (N.at(pos) < biggest) {
        		N.at(pos-1) = biggest - 1;

        		break;
        	}
        }

        int j = pos - 1;

        for (; pos < N.size(); pos++) {
        	N.at(pos) = '9';
        }

        for (; j > 0; j--) {
        	if (N.at(j-1) > N.at(j)) {
        		N.at(j-1) = N.at(j-1) - 1;
        		N.at(j) = '9';
        	}
        	else {
        		break;
        	}
        }

        if (N.at(0) == '0') {
        	N.erase(0, 1);
        }

        cout << N << endl;
    }

    return 0;
}
