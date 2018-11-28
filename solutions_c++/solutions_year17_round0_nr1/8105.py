#include <iostream>
#include <string> 
#include <fstream>

using namespace std;

// just... send output to stdout
// and then from the cmd pass it to a file. 
void calculate_answer
(string pancakes, unsigned int spatula_size) {

	// get the index of the last part... 
	unsigned int num_flips = 0;
	unsigned int end = pancakes.size() - spatula_size;
	for(unsigned int i = 0; i <= end; i++) {
		if(pancakes[i] == '-') {
			//cout << "detected ";
			for(unsigned int j = i; j < spatula_size + i; j++) {
				if(pancakes[j] == '-') {
			//		cout << "flippingto plus" << endl;
					pancakes[j] = '+';
				} else {

			//		cout << "flipping to minus" << endl;
			//		cout << "before flip: " << pancakes << " " << i << " " << j << endl;
					pancakes[j] = '-';
			//		cout << "after flip: " << pancakes << endl;
				}
			}
			num_flips++;
		}
		//cout << i << " " << pancakes << endl;
		
	}

	// check if the entire thing is all positives now. 
	bool all_flipped = true;
	for(unsigned int i = 0; i < pancakes.size(); i++) {
		if(pancakes[i] == '-') {
			all_flipped = false;
		}
	}

	if(all_flipped) {
		cout << num_flips << endl;
	} else {
		cout << "IMPOSSIBLE" << endl;
	}
}

int main(int argc, char *argv[]) {

	fstream input(argv[1]);	

	unsigned int trials;
	input >> trials;

	unsigned int current_trial = 0;
	
	while(current_trial < trials) {

		string pancake_row;
		input >> pancake_row;

		unsigned int k = 0;
		input >> k;

		cout << "Case #" << current_trial + 1 << ": ";
		calculate_answer(pancake_row, k);
		current_trial++;
	}
}
