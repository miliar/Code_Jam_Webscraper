#include <iostream>
#include <sstream>
#include <math.h>

using namespace std;

void int_to_arr(unsigned long input, unsigned long length, unsigned long* output) {
	unsigned long tmp;

	for (int i=length-1;i>=0;i--) {
		output[i] = input % 10;
		input /= 10;
	}
}

unsigned long arr_to_int(unsigned long* input, int length) {
	unsigned long output = 0;
	unsigned long pow = 1;
	for (int i=length-1;i>=0;i--) {
		output += input[i]*pow;
		pow *= 10;
	}
	return output;
}

unsigned long pow10(int pow) {
	unsigned long output = 1;
	for (int j=pow;j>0;j--) output *= 10;
	return output;
}

int main() {
	unsigned long number, tmp_num, pow;
	int result, case_num, flag, curr, last, digit_num, correct;
	int* equal;
	string tmp;

	getline(cin,tmp);
	case_num = stoi(tmp);

#ifdef DEBUG
	cout << "case_num : " << case_num << endl;	//TODO Delete
#endif
	
	for (int count=1; count<=case_num; count++) {
		getline(cin,tmp);
		number = stol(tmp);
		tmp_num = number;
		digit_num = 0;
		while (tmp_num > 0) {
			tmp_num /= 10;
			digit_num++;
		}

#ifdef DEBUG
		cout << "input : " << number << ", # of digits : " << digit_num << endl;	//TODO Delete
#endif

#ifndef DEBUG_FN
		if (digit_num == 1) {				// number < 10
			cout << "Case #" << count << ": " << number << endl;
			continue;
		}
		else if (digit_num == 2) {			// number < 100
			if (number / 10 > number % 10) {
				number = (number / 10 - 1) * 10 + 9;
			}
			cout << "Case #" << count << ": " << number << endl;
			continue;
		}
		else {								// number >= 100
			equal = new int[digit_num+1]();
			pow = pow10(digit_num-2);
			last = number / pow10(digit_num-1);
#ifdef DEBUG
			printf("initial last : %d\n", last);
#endif
			correct = 1;
			for (int i=digit_num-1;i>0;i--) {
#ifdef DEBUG
				printf("pointing at digit : %d, pow : %lu\n", i,pow);
#endif
				curr = (number / pow) % 10;
#ifdef DEBUG
				printf("last : %d, curr : %d\n",last,curr);
#endif

				if (last > curr) {
					correct = 0;
					flag = 1;
					while (flag) {
						number += (9-curr) * pow10(i-1);	// curr <- 9
#ifdef DEBUG
						printf(">>>> %lu\n", number);
#endif
						number -= pow10(i);					// last -= 1
#ifdef DEBUG
						printf(">>>> %lu\n", number);
#endif
						flag = equal[++i];
						curr = (number / pow10(i-1)) % 10;
					}
					number = (number / pow + 1) * pow - 1;	// set remaining digits to 9
					cout << "Case #" << count << ": " << number << endl;
					break;
				}
				else if (last == curr) equal[i] = 1;	// check equal vector

				pow /= 10;
				last = curr;
			}
			if (correct) cout << "Case #" << count << ": " << number << endl;
		}	// end if
#ifdef DEBUG
		printf("end loop\n");
#endif
#endif
	}	// end for

#ifdef DEBUG_FN
	unsigned long test[5] = {1,3,5,4,2};
	unsigned long* output = NULL;
	printf("arr_to_int test result : %d\n", arr_to_int(test,5));

	output = new unsigned long[5]();
	int_to_arr(13542,5,output);
	printf("int_to_arr done\n");
	for (int k=0;k<5;k++) printf("%d ",output[k]);
	printf("\n");

	printf("power : %d\n",pow10(1));
#endif

#ifdef DEBUG
	printf("end program\n");
#endif
	return 0;
}
