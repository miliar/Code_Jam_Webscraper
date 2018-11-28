#include <iostream>
#include <string>

using namespace std;

bool is_tidy(long long input);

int main() {
	int testnum, test = 0;
	long long input;
	long long i;

	FILE *fp = fopen("output.txt", "w");
	freopen("B-small-attempt0.in", "r", stdin);

	cin >> testnum;
	while (test < testnum) {
		test++;
		cin >> input;
		for (i = input; i >= 0; i--) {
			//printf("here at least\n");
			if (is_tidy(i) == true)
				break;
		}
		fprintf(fp,"Case #%d: %lld\n", test,i);
	}

	fclose(fp);
	return 0;
}

bool is_tidy(long long input) {
	long long test_input = input;
	long long comp1, comp2;
	if (input / 10 == 0) {
		printf("one digit\n");
		return true;
	}
	else{
		while (1) {
			comp1 = test_input % 10;
			test_input = test_input / 10;
			comp2 = test_input % 10;
			//printf("comp1 : %d, comp2: %d\n", comp1, comp2);
			if (comp1 >= comp2) {
				if (test_input / 10 == 0) {
					//printf("last digits compared\n");
					return true;
				}
				else {
					printf("m\n");
					continue;
				}
			}
			else {
				return false;
			}
		}
	}
}