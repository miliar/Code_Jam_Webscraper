#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

#define MAX_CHAR 32

int istidy(char *num) {
	char last = '0';
	for (int i = 0; i < MAX_CHAR; i++) {
		if (num[i] == 0) {
			return 0;
		}
		if (num[i] < last) {
			return i;
		}
		last = num[i];
	}
	return 0;
}

char substract(char *num, int pos) {
	const int len = strlen(num);
	num[pos - 1]--;
	for (int i = pos; i < len; i++) {
		
		num[i] = '9';
	}

	return 0;
}

int getSmallest(char *num, char *target) {
	
	strcpy((char*)target, num);
	int istidyresult = 1;
	while (istidyresult > 0) {
		istidyresult = istidy(target);
		if (istidyresult == 0) {
			break;
		}
		substract(target, istidyresult);
	}

	int i = 0;

	while (target[i] == '0') {
		i++;
	}

	return i;
}

void main() {
	int t, pad;
	
	char x[MAX_CHAR];

	char *result = (char*)malloc(32);

	cin >> t; 
	for (int i = 1; i <= t; ++i) {
		cin >> x;  
		pad = getSmallest(x, result);
		result += pad;
		cout << "Case #" << i << ": " << result << endl;
		result -= pad;
	}
}