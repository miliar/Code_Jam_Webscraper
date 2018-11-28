#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>

using namespace std;

int to_int(char c){
	return c - '0';
}

char to_char(int i){
	return i + '0';
}

string solve(string number_string){
	int target;
	int reduced_index = -1;

	for (int i = 0; i < (number_string.size() - 1); ++i){
		if (number_string[i] > number_string[i+1]){

			for (int j = i; j >= 0; --j){
				if ((j == 0) || ((number_string[j] - 1) >= number_string[j-1])){
					number_string[j] -= 1;
					reduced_index = j;
					break;
				}

				// if (number_string[j] >= number_string[j-1]){
				// 	number_string[j] = number_string[j-1];
				// 	reduced_index = j;
				// 	break;
				// }
			}

			break;			
		}
	}

	if (reduced_index != -1){
		for (int j = (reduced_index + 1); j < number_string.size(); ++j){
			number_string[j] = to_char(9);
		}
	}

	if (to_int(number_string[0]) == 0){
		number_string.erase(0, 1);
	}

	return number_string;
}

int main(int argc, char* argv[]){
	int t = 0, T;
	string str, number_string, ans;

	getline (cin, str);
	T = stoi(str);

	while (t++ < T){
		getline (cin, number_string);

		ans = solve(number_string);

		cout << "Case #" << t << ": " << ans << endl;
	}
}