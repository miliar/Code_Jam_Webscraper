#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

const string path = "C:\\Users\\Max\\Downloads\\";

void runCase() {
	int D,N;
	cin >> D >> N;
	double longestTime = 0;
	for (int i = 0; i < N; i++) {
		int Ki, Si; 
		cin >> Ki >> Si;
		double time = (D-Ki) / (double)Si;
		
		if (time > longestTime) 
			longestTime = time;
	}
	
	double speed = D/longestTime;
	//cout << speed;
	printf("%f", speed);
}

bool loadFile(int argc, char *argv[]) {
	bool isTest = argc == 3 && !strcmp(argv[2], "-t");
	string filename = argv[1];
	
	freopen((path + filename + ".in").c_str(), "r", stdin);
	if (!isTest)
		freopen((filename + "-out.out").c_str(), "w", stdout);
	
	return isTest;
}

int main(int argc, char *argv[]) {
	bool isTest = loadFile(argc, argv);
	int tc;
	cin >> tc;
	for (int i = 1; i <= tc; i++) {
		cout << "Case #" << i << ": ";
		runCase();
		cout << "\n";
	}
	
	fclose(stdin);
	if (!isTest)
		fclose(stdout);
}