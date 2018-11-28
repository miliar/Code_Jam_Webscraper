#include <iostream>
int isTidy (unsigned long int num) {
//std::cout << "In isTidy "<<num<<std::endl;
	if (num < 10) {
		return 1;
	}
	  
	int last = num % 10;
	int second_last;
	for (unsigned long int rest = num/10; rest > 0; rest = rest /10) {
		second_last = rest%10;
		if (second_last > last ) {
			return -1;
		} 
		last = second_last;
	}
	return 1;
}
unsigned long int prune (unsigned long int num) {
//std::cout << "In prune "<<num<<std::endl;
	if (num < 10) {
		return 0;
	} 
	unsigned long int rest = num /10;
	unsigned long int pruned = 0;
	int last = num % 10;
	int second_last = rest % 10;
	if (second_last > last ) {
		rest = rest -1;
	}
	pruned = prune (rest);
	if (pruned == 0 ) {
		if (second_last > last) {
			return rest * 10 + 9;
		}
		else {
			return 0;
		} 
	}
	else {
		return pruned * 10 + 9;
	}
}
int main () {
	int T =0;
	unsigned long int num =0 ;
	int i;
	unsigned long int j, pruned;
	std::cin >> T;
//std::cout << T<<std::endl;
	for (i = 0; i < T; i++) {
		std::cin >> num;
//std::cout <<num <<std::endl;
/*		for (j = num; j > 0; j--) {
			if (isTidy(j) > -1) {
				std::cout << "Case #"<<i+1<<": "<<j<<std::endl;
				break;
			}
		}
*/
		if (num < 10) {
				std::cout << "Case #"<<i+1<<": "<<num<<std::endl;
		}
		else {
				pruned = prune (num);
			if (pruned !=0) {
				std::cout << "Case #"<<i+1<<": "<<pruned<<std::endl;
			}
			else {
				std::cout << "Case #"<<i+1<<": "<<num<<std::endl;
			}
		}	
	}
}
