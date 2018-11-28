#include <iostream>
#include <set>
#include <functional>

using namespace std;



struct Answer {
	long int max;
	long int min;
};
/*
bool isOdd(long int num) {
	return num %2;
}

Answer solve(Answer inputConfig, long int numPeople) {
	Answer currentAnswer = inputConfig;
	for (long int i = 0; i < numPeople; ++i) {
		Answer newAnswer;
		long int newPosition = currentAnswer.max / 2 + currentAnswer % 2;

	}
}
*/

Answer solve(long int numStalls, long int numPeople) {
	multiset<long int, greater<long int> > stalls;
	stalls.insert(numStalls);

	Answer currentAnswer;
	for (int i = 0; i < numPeople; ++i) {
		long int currentMax = *stalls.begin();
		stalls.erase(stalls.begin());

		currentAnswer.max = (currentMax-1)/2 + (currentMax-1)%2;
		currentAnswer.min = (currentMax-1)/2;
		stalls.insert(currentAnswer.max);
		stalls.insert(currentAnswer.min);

		/*
		multiset<long int, greater<long int> >::iterator it = stalls.begin();
		for (;it != stalls.end(); ++it) {
			cout << *it << " ";
		}
		cout << 	endl;	*/
	}

	return currentAnswer;

}



int main() {
	int T;
	cin >> T;

	for (int i = 0; i < T; ++i) {
		long int numStalls, total;
		cin >> numStalls >> total;
		Answer caseAnswer = solve(numStalls, total);
		cout << "Case #" << i+1 << ": " << caseAnswer.max << " " << caseAnswer.min << endl;

	}
}