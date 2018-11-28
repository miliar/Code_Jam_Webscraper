#include <iostream>
#include <string>

using namespace std;


int where_minus(char arr[], int string_size);
bool check_plus(char arr[], int string_size);
void flip(int minus_loc, int flip_num, char arr[]);

int main() {
	int testnum = 0,test=0;
	int i;
	int string_size=0,length=10000;
	char input;
	int flip_num,flip_count=0;
	char* input_arr;

	FILE *fp = fopen("output.txt", "w");
	freopen("A-large.in", "r", stdin);

	cin >> testnum;
	while (test < testnum) {
		test++;
		string_size = 0;
		flip_count = 0;
		input_arr = (char*)malloc(sizeof(char)*length);

		cin >> input_arr;

		for (int i = 0; i < length; i++) {
			if (input_arr[i] != NULL)
				string_size++;
			else
				break;
		}
		cin >> flip_num;

		if (check_plus(input_arr,string_size) == true) {
			fprintf(fp, "Case #%d: 0\n", test);
			free(input_arr);
		}
		else
			while (1) {
				int minus_loc = where_minus(input_arr, string_size);
				if (string_size - minus_loc < flip_num && check_plus(input_arr,string_size)==false) {
					fprintf(fp, "Case #%d: IMPOSSIBLE\n",test);
					free(input_arr);
					break;
				}
				else {
					flip(minus_loc, flip_num, input_arr);
					flip_count++;

					if (check_plus(input_arr,string_size)==true) {
						fprintf(fp, "Case #%d: %d\n", test, flip_count);
						free(input_arr);
						break;
					}
				}
			}
	}
	fclose(fp);
	return 0;

}

bool check_plus(char arr[], int string_size) {
	for (int i = 0; i < string_size; i++) {
		if (arr[i] == '-') {
			return false;
		}
	}
	return true;
}

int where_minus(char arr[], int string_size) {
	int i;
	for (i = 0; i < string_size; i++) {
		if (arr[i] == '-') {
			break;
		}
	}
	return i;
}

void flip(int minus_loc, int flip_num, char arr[]) {
	for (int i = minus_loc; i < minus_loc + flip_num; i++) {
		if (arr[i] == '-')
			arr[i] = '+';
		else
			arr[i] = '-';
	}
}