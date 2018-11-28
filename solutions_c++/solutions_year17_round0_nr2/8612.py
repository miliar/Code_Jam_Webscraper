#include <iostream>
#include <string>

using namespace std;

int main() {
  unsigned num_cases;
  cin >> num_cases;

	string input;

  for (unsigned case_num = 1; case_num <= num_cases; case_num++) {
    cin >> input;

    //cout << "input for Case #" << case_num << ": " << input << endl;

		if (input.length() == 1) {
			// the input is already the largest tidy number
			cout << "Case #" << case_num << ": " << input << endl;
			continue;
		}

		// we can now assume the input has at least two digits

		uint8_t *digits = new uint8_t[input.length()];

		// load the decimal digits into an array
		for (unsigned i = 0; i < input.length(); i++) {
			digits[i] = input.at(i) - '0';
		}

		// temporary holder for the index of the digit 
		// we must decrement to get a tidy number
		unsigned a = input.length();

		for (unsigned i = 0; i+1 < input.length(); i++) {
			// check if the digits are nondecreasing
			if (digits[i+1] < digits[i]) {
				a = i;
				break;
			}
		}
		
		if (a < input.length()) {
			// decrement the digit before the limiting digit 
			// to allow a carry
			// If the digit to be decremented forms the end of a 
			// repeat sequence, every position in the sequence 
			// must be decremented.
			
			for (int i = static_cast<int>(a) - 1; i >= 0; i--) {
				if (digits[i] == digits[a]) {
					a--; // move a back toward the start
				} else {
					break;
				}
			}

			// now find the tidy number
			
			// the digit to decrement will be > 0, so no carry needed
			digits[a]--;

			// the largest tidy number will have all following digits = 9
			for (unsigned i = a + 1; i < input.length(); i++) {
				digits[i] = 9;
			}
		} // end if: handling a limiting digit
		

		// now output the tidy number

		unsigned i = 0;

		// skip leading zeros
		for (; i+1 < input.length(); i++) {
			if (digits[i] != 0) {
				break;
			}
		}

		cout << "Case #" << case_num << ": ";

		// print the digits
		for (; i < input.length(); i++) {
			cout << static_cast<char>('0' + digits[i]);
		}
		cout << endl;
	
  } // end for: cases
}


