#include<stdio.h>
#include<stdlib.h>
#include<vector>

using namespace std;


int main () {
	vector <int> number;
	int t, case_counter, block_index, update;
	char c;
	
	
	scanf("%d ", &t);
	
	case_counter = 0;
	
	while (t--) {
		case_counter++;
		number.clear();
		block_index = 0;
		
		while (true) {
			scanf("%c", &c);
			if (c >= '0' && c <= '9') {
				number.push_back(c - '0');
			} else break;
//printf("***");			
		}
		
		for (int i=0; i<number.size()-1; i++) {
//printf("@");
			if (number[i] > number[i+1]) {
				if (number[block_index] == 1 ) {
//printf("#");
					number.pop_back();
					for (int j=0; j< number.size(); j++) {
						number[j] = 9;
					}
					break;
				} else {
					number[block_index] --;
					for (int j = block_index+1; j < number.size(); j++) {
						number[j] = 9;
					}
					break;
				}
			} else if (number[i] < number[i+1]) {
				block_index = i+1;
//printf("$");
			}
		}
		
		printf("Case #%d: ", case_counter);
		
		for(int i=0; i< number.size(); i++ ) {
			printf("%d", number[i]);
		}
		
		printf("\n");
		
	}
	
	return 0;
}
