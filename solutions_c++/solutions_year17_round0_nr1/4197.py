#include <iostream>
#include <string>
#include <list>
#include <set>


using namespace std;

string flip(string s, int i, int k) {
	string ss(s);
	for (int j = i; j < i + k; j++) {
		if (ss[j] == '+') {
			ss[j] = '-';
		} else {
			ss[j] = '+';
		}
	}
	return ss;
}

bool isvalid(string s) {
	for (int i = 0; i < s.size(); i++) {
		if (s[i] != '+') {
			return false;
		}
	}
	return true;
}

bool isvalidflip(string s, int i, int k) {
	for (int j  = i; j < i + k; j++) {
		if (s[j] == '-') {
			return true;
		}	
	}
	return false;
}

// int main() {
// 	int T;
// 	cin >> T;

// 	for (int iT = 0; iT < T; iT++) {
// 		cout << "Case #" << iT+1 << ": ";

// 		string input;
// 		cin >> input;
// 		int length = input.size();
// 		int K;
// 		cin >> K;

// 		int i = 0;

// 		while (!isvalid(input)) {
// 			s
// 		}

// 		if (!worked) {
// 			cout << "IMPOSSIBLE" << endl;
// 		}
// 	}
// }


int main() {
	int T;
	cin >> T;

	for (int iT = 0; iT < T; iT++) {
		cout << "Case #" << iT+1 << ": ";

		string input;
		cin >> input;
		int length = input.size();
		int K;
		cin >> K;

		list<pair<string, int> > q;

		q.push_back(make_pair(input, 0));

		set<string> visited;
		visited.insert(input);

		bool worked = false;
		while (q.size() != 0) {
			pair<string, int> s = q.front();
			q.pop_front();
			visited.insert(s.first);

			// cout << visited.size() << endl;
			
			if (isvalid(s.first)) {
				cout << s.second << endl;
				worked = true;
				break;
			} else {
				for (int i = 0; i <= length - K; i++) {
					// if (!isvalidflip(s.first, i, K)) {
					// 	continue;
					// }
					 
					if (s.first[i] == '-') {

						string ss = flip(s.first, i, K);

						if (visited.count(ss) == 0) {
							q.push_back(make_pair(ss, 
										s.second + 1));
						}
						break;
					}

				}
			}
		}

		if (!worked) {
			cout << "IMPOSSIBLE" << endl;
		}
	}
}