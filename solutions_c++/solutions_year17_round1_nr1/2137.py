#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;


int main() {
	int numTests;

	cin >> numTests;
	

	for(int i = 0; i < numTests; ++i) {
		vector< vector <char> > initials;
		int R,C;
		cin >> R >> C;

		for(int r = 0; r < R; ++r) {
			vector <char> row;
			char filler = '?';
			int start = 0;
			for(int c = 0; c < C; ++c) {
				char name;
				cin >> name;
				if(name != '?') {
					//notGood.push_back(c);
					filler = name;

				}

				row.push_back(filler);


			}

			for(int c = C-2; c >= 0; --c) {
				char name = row[c];
				if(name == '?') {
					//notGood.push_back(c);
					row[c] = row[c+1];
				}


			}

			initials.push_back(row);
		}



		//cout << "what?" << endl;
		for(int r = 0; r < R; ++r) {
			
			for(int c = 0; c < C; ++c) {
				
				if(initials[r][c] == '?') {
					int r_ = r;
					while(initials[r_][c] == '?') {
						r_ = r_-1;
						if(r_ == -1) {
							break;
						}
					}

					if(r_ == -1) {
						r_ = r;
						while(initials[r_][c] == '?') {
							r_ = r_+1;
							if(r_ == R) {
								break;
							}
						}

						initials[r][c] = initials[r_][c];
					} else {
						initials[r][c] = initials[r_][c];
					}
				}
			}

		}

		cout << "Case #" << i+1 << ":" << endl;
		for(int r = 0; r < R; ++r) {
			
			for(int c = 0; c < C; ++c) {
				
				cout << initials[r][c];
			}
			cout << endl;

		}
	}

}