#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void
compute_fn
(string s) {

	// start at the end. 
	// if the number is 0, turn it into a 9. 

	bool must_decrement = false;

	int i = s.size() - 1;
	while(i > 0) {

		// cases: 
		// must_decrement is true: 
		// 	s[i] == 0:
		// 		set to 9, leave must_decrement on.  
		// 	s[i] != 0:
		// 		decrement s[i]. 
		// 		now, if s[i] == 0, set it to 9, and set must_decrement to on. 
		// 	s[i] > 1:
		// 		decrement s[i].
		// 		now, compare with previous digit. if s[i] > s[i-1], do nothing. 
		// 		otherwise, set s[i] to 9 and set must_decrememt to on.
		//
		// must_decrement is not true: 
		// 	s[i] == 0:
		// 		set to 9, set must_decrement on. 
		// 	s[i] != 0:
		// 		check if s[i] > s[i-1]. If yes, set must_decrement to on, set to 9.  
		// 		otherwise, do nothing. 
	
		if(must_decrement && s[i] == '0') {
			s[i] = '9';
		} else if(must_decrement && s[i] == '1') {
			s[i] = '9';
		} else if(must_decrement && s[i] > '1') {
			s[i] = s[i] - 1;
			if(s[i] < s[i - 1]) {
				s[i] = '9';
			} else {
				must_decrement = false;
			}
		} else if(!must_decrement && s[i] == '0') {
			s[i] = '9';
			must_decrement = true;
		} else if(!must_decrement) {
			
			if(s[i] < s[i - 1]) {
			//	cout << "setting to true because of comparison: " << s[i-1] << ">" << s[i] << endl;
				s[i] = '9';
				must_decrement = true;
			}
		}
		i--;

	}

	// we're at the front now... 
	if(s[0] == '1' && must_decrement) {
		s[0] = '0';
	} else if(s[0] > '1' && must_decrement) {
		s[0] = s[0]-1;
	}

	// now reverse the string, 
	// get rid of leading zerios
	// and the reverse it back. 
	string reversed;
	for(auto it = s.rbegin(); it != s.rend(); it++) {
		reversed.push_back(*it);
	}

	while(reversed.back() == '0') {
		reversed.pop_back();
	}

	string answer;
	for(auto it = reversed.rbegin(); it != reversed.rend(); it++) {
		answer.push_back(*it);
	}

	bool found_nine = false;
	// now, we need to go through, and set 9's. 
	for(int i = 1; i < answer.size(); i++) {
		if(found_nine) {
			answer[i] = '9';
		} else {
			if(answer[i] < answer[i-1]) {
				answer[i] = '9';
				found_nine = true;
			}
		}
	}

	cout << answer << endl;
}

int main(int argc, char *argv[]) {

	fstream input(argv[1]);


	unsigned int t;
	input >> t;

	for(unsigned int i = 1; i <= t; i++) {

		cout << "Case #" << i << ": ";
		string s;
		input >> s;

		compute_fn(s);
	}
}
