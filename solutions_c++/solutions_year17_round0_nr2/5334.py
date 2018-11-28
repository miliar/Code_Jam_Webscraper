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
	string num;
	cin >> num;
	int l = num.length();
	
	for (int i = l-2; i >= 0; i--) {
		char first = num[i];
		char second = num[i+1];
		if (first <= second)
			continue;
		
		num[i] = first - 1;
		for (int j = i+1; j < l; j++)
			num[j] = '9';
	}
	
	cout << atol(num.c_str());
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