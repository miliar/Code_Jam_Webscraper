#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

typedef struct {
	double speed;
	double position;
}HorseData;

HorseData horses[1000];
void solve () {
	double distance;
	int qtdHorses;
	cin >> distance;
	cin >> qtdHorses;
	double minSpeed = 10000 * distance;
	for (int i = 0; i< qtdHorses; i++) {
		double currentPosition;
		double currentSpeed;		
		cin >> currentPosition;
		cin >> currentSpeed;
		double time = (distance - currentPosition)/currentSpeed;
		double myCurrentSpeed = distance/time;
		if (myCurrentSpeed < minSpeed) minSpeed = myCurrentSpeed;
	}
	printf("%lf",minSpeed);
	cout << endl;
}

int main() {
    int tests;
    cin >> tests;
    for (int i = 1; i <= tests; i++) {
    	cout << "case #" << i << ": ";
    	solve();
	}
	return 0; 
}

