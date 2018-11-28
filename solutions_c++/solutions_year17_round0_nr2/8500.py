#include <string>
#include <iostream>

using namespace std ;

string max_tidy (string input) {
	bool need_to_change = false ;
	string::iterator main ;
	string::iterator start_identical ;
	start_identical = input.begin() ;
	for (main = input.begin() ; main != input.end()-1 ; main ++) {
		if (*start_identical != *main) start_identical = main ;
		if (*(main+1) < *main) {
			need_to_change = true ; 
			break ;
		}
	}
	if (need_to_change == true) {
		input.replace(start_identical+1, input.end(), input.end()-(start_identical+1), '9') ;
		input.replace(start_identical, start_identical+1, 1, *(start_identical)-1) ;
	}
	if (*(input.begin()) == '0') input.erase(0, 1) ;
	return input ;
}

int main(void) {
	int nb_test ; string pres ; string line_input ;
	cin >> nb_test ;
	for (int i=0 ; i<nb_test ; i++) {
		pres = "Case #" + to_string(i+1) + ": " ;
		cin >> line_input ;
		cout << pres << max_tidy(line_input) << endl ;
	}
	return 0 ;
}