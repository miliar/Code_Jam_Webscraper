#include <iostream> 
#include <stdlib.h>
#include <algorithm>
#include <queue>

using namespace std;

struct horse {
	int start;
	int speed;
	friend bool operator <(const horse &a, const horse &b) {
		return a.start < b.start;
	}
	horse() {}
	horse(int _start, int _speed) {
		start = _start;
		speed = _speed;
	}
	double finish(int finish) {
		return (double)(finish - start) / (double)speed;
	}
};

void printAnswer(int , double );
void findAndPrintSpeed(priority_queue<horse> horses, int start, int casenum);


void main() {

	int numCases, hspeed, hstart;
	cin >> numCases;
	priority_queue<horse> horses;
	horse temp;
	int trackLength, numHorses;
	for (int j = 0; j < numCases; ++j) {
		cin >> trackLength >> numHorses;
		for (int i = 0; i < numHorses; ++i) {
			cin >> temp.start >> temp.speed;
			horses.push(temp);
		}
		findAndPrintSpeed(horses, trackLength, j);
		horses = priority_queue<horse>();
	}

}
void findAndPrintSpeed(priority_queue<horse> horses, int start, int casenum) {
	horse slowest;
	slowest = horses.top();
	horse one, two;
	while (horses.size() > 1) {
		one = horses.top();
		horses.pop();
		two = horses.top();
		if (one.finish(start) < two.finish(start)) {
			if (slowest.finish(start) < two.finish(start)) {
				slowest = two;
			}
		}
	}
	printAnswer(casenum, start / slowest.finish(start));
}

void printAnswer(int caseNum, double solutiona) {
	printf("Case #%d: %f\n", caseNum + 1, solutiona);
}