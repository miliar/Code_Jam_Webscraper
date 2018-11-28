#include <iostream>
using namespace std;

int main() {
	int T;

	cin >> T;

	int r, c, sz[30];
	string str[30];
	for (int t=1 ; t<=T ; ++t) {

		cin >> r >> c;

		for (int i=0 ; i<r ; ++i)
			cin >> str[i];
	
		char first[30];
		for (int i=0 ; i<r ; ++i) {
			sz[i] = 0;
			char first = 0;
			for (int j=0 ; j<c ; ++j) {
				if (str[i][j] != '?') {
					sz[i]++;
					if (!first)
						first = str[i][j];
				}
			}
			str[i][0] = first;
		}

		bool started = 0;
		for (int i=0 ; i<r ; ++i) {
			if (sz[i] == 0 && started)
				for (int j=0 ; j<c ; ++j)
					str[i][j] = str[i-1][j];

			else if (sz[i]) {
				for (int j=1 ; j<c ; ++j)
					if (str[i][j] == '?')
						str[i][j] = str[i][j-1];
				
				if (started == 0) {
					for (int x=i-1 ; x>=0 ; --x)
						for (int j=0 ; j<c ; ++j)
							str[x][j] = str[i][j];				
				}
				started = 1;
			}
		}

		cout << "Case #" << t << ":\n";
		for (int i=0 ; i<r ; ++i)
			cout << str[i] << endl;
	}

	return 0;
}