#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

#define ifs cin
#define ofs cout
//ifstream ifs("A-small-practice.in");ofstream ofs("1.out");
//ifstream ifs("A-large.in");ofstream ofs("2.out");
//ifstream ifs("C-large.in");ofstream ofs("3.out");

void solve(int time){
	int n;
	double d;
	ifs >> d >> n;
	double maxi = 0;
	for(int i = 0;i < n;i++){
		double k,s;
		ifs >> k >> s;
		k = (d-k)/s;
		if(k > maxi) maxi = k;
	}
	//ofs << "Case #" << time << ":" << endl;
	printf("Case #%d: %9f\n",time,d/maxi);
}

int main() {
	int t;
	ifs >> t;
	//cout << "start" << endl;
	for(int i = 1;i <= t;i++){
		solve(i);
	}
	//cout << "fin" << endl;
	return 0;
}
