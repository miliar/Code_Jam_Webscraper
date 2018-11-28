#include <cstdint>
#include <iostream>
#include <string>

using namespace std;

int findError (string input) {
    for (int i = 1; i < input.length(); i++) {
	if (input[i] < input[i-1]) {
	    return i-1;
	}
    }
    return -1;
    
}

string tidy (string input) {
    if (input.length() ==1)
	return input;
    while (true) {
	int firsterror = findError(input);
	if (firsterror == -1) {
	    return input;
	}
	else {
	    input[firsterror]--;
	    for (int i = firsterror + 1; i < input.length(); i ++) {
		input[i] = '9';
	    }
	}
    }
    return input;
}

int main()
{
    int numCases = 0;
    cin >> numCases;

    for (int q = 0; q < numCases; q++)
    {
	string n;
	cin >> n;

	int64_t highest = 0;
	highest = strtoll(tidy(n).c_str(), NULL, 10);
	cout << "Case #" << q+1 << ": " << highest << endl;
    }
    return 0;
}
