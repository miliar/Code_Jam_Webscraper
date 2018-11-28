#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <cmath>
#include <climits>
#include <iomanip>
using namespace std;

struct Horse {
	double pos;
	double speed;
};

bool cmp(Horse h, Horse t) {
	return h.pos < t.pos;
}

vector<Horse> horses;
int N;
double D;

double timeTaken(int i) {
	if(i >= horses.size()) return 0;
	
	Horse h = horses[i];
	return max((D-h.pos) / (double)h.speed, timeTaken(i+1));
}

void oneRun(){
	horses.clear();
	
	cin >> D >> N;
	
	for(int i=0; i<N; i++) {
		double p, s;
		cin >> p >> s;
		Horse h = {p, s};
		horses.push_back(h);
	}
	sort(horses.begin(), horses.end(), cmp);
	double time = timeTaken(0);
	
	cout << fixed << setprecision(7) << D / time;
}

int main(){
	int nums;
	cin >> nums;
	for(int i=1; i <= nums; i++) {
		cout << "Case #" << i << ": ";
		oneRun();
		cout << endl;
	}
		
	return 0;
}