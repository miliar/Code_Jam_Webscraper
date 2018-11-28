#include <iostream> 
#include <stdlib.h>
#include <algorithm>
#include <vector>

void printAnswer(int caseNum, unsigned long long int solution, unsigned long long int);
using namespace std;
unsigned long long findMaxEmptyStalls(unsigned long long stalls, unsigned long long people);
unsigned long long secondAttempt(unsigned long long stalls, unsigned long long people);
void main() {

	unsigned long long n, stalls, people;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> stalls >> people;
		unsigned long long answer = findMaxEmptyStalls(stalls, people);
		printAnswer(i + 1, answer - answer / 2, answer / 2);
	}
}

unsigned long long secondAttempt(unsigned long long stalls, unsigned long long people) {
	vector<unsigned long long> stallsArr;
	unsigned long long num;
	stallsArr.push_back(stalls);
	make_heap(stallsArr.begin(), stallsArr.end());
	while (people > 1) {
		pop_heap(stallsArr.begin(), stallsArr.end());
		num = *(stallsArr.end() - 1);
		stallsArr.pop_back();
		num -= 1;
		stallsArr.push_back(num - num / 2);
		push_heap(stallsArr.begin(), stallsArr.end());
		stallsArr.push_back(num / 2);
		push_heap(stallsArr.begin(), stallsArr.end());
		people--;
	}
	pop_heap(stallsArr.begin(), stallsArr.end());
	return *(stallsArr.end() - 1) - 1;
}


unsigned long long findMaxEmptyStalls(unsigned long long stalls, unsigned long long people) {
	stalls -= 1;
	people -= 1;
	if (people == 0) {
		return stalls;
	}
	auto res2 = findMaxEmptyStalls(stalls - stalls / 2, people - people / 2);
	if (people / 2 > 0) {
		auto res1 = findMaxEmptyStalls(stalls / 2, people / 2);
		return (res1 > res2 ? res2 : res1);
	}
	return res2;

}



void printAnswer(int caseNum, unsigned long long int solutiona, unsigned long long int solutionb) {
	printf("Case #%d: %I64d %I64d\n", caseNum, solutiona, solutionb);
}