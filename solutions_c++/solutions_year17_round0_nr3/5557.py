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

struct stall {
	bool occ;
	int ls;
	int rs;
	int min() { return (ls < rs) ? ls : rs; }
	int max() { return (ls > rs) ? ls : rs; }
};

void runCase() {
	int N;
	int k;
	cin >> N >> k;
	vector<stall> stalls(N);
	for (int i = 0; i<N; i++) {
		stalls[i].ls = i;
		stalls[i].rs = N-i-1;
		stalls[i].occ = false;
	}
	
	int sel = 0;
	for (int i = 0; i < k; i++) {
		sel = -1;
		for (int j = 0; j < N; j++) {
			if (stalls[j].occ)
				continue;
			
			if (sel < 0) {
				sel = j;
				continue;
			}
			
			int min1 = stalls[j].min();
			int min2 = stalls[sel].min();
			if (min1 > min2 || (min1 == min2 && stalls[j].max() > stalls[sel].max()))
				sel = j;
		}
		
		stalls[sel].occ = true;
		for (int j = sel+1; j < N && !stalls[j].occ; j++)
			stalls[j].ls = j-sel-1;
		for (int j = sel-1; j >= 0 && !stalls[j].occ; j--)
			stalls[j].rs = sel-j-1;
	}
	cout << stalls[sel].max() << " " << stalls[sel].min();
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