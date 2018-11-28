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
	string pc;
	int k;
	cin >> pc >> k;
	int l = pc.length();
	
	int flips = 0;
	for (int i = 0; i < l - k + 1; i++) {
		if (pc[i] == '+')
			continue;
		
		flips++;
		for (int j = 0; j < k; j++)
			pc[i+j] = (pc[i+j] == '+') ? '-' : '+';
	}
	
	for (int i = 0; i < l; i++) {
		if (pc[i] == '-') {
			cout << "IMPOSSIBLE";
			return;
		}
	}
	
	cout << flips;
}

bool loadFile(int argc, char *argv[]) {
	bool result = false;
	string filename = argv[1];
	if (!strcmp(argv[2], "-s")) {
		filename += "-small-attempt";
		filename += argv[3];
	}
	else if (!strcmp(argv[2], "-l"))
		filename += "-large";
	else if (!strcmp(argv[2], "-t")) {
		result = true;
		filename += "-test";
	}
	else 
		filename += argv[2];
	
	freopen((path + filename + ".in").c_str(), "r", stdin);
	if (!result)
		freopen((filename + "-out.out").c_str(), "w", stdout);
	
	return result;
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