#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <iomanip>
using namespace std;

struct Stu {
	int K, S;
};

bool cmp(const Stu& a,const Stu& b){
	return a.K > a.K;
}

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("outlarge111.txt");

	int t;
	fin >> t;
	for (int ti = 1; ti <= t; ti++)
	{
		int D, N;
		fin >> D >> N;
		Stu arr[10000];
		for (int i = 0; i < N; i++) {
			fin >> arr[i].K >> arr[i].S;
		}
		sort(arr, arr + N, cmp);

		double fastest = 0;
		for (int i = 0; i < N; i++) {
			double curFastest = (D - arr[i].K) / (double)arr[i].S;
			if (curFastest > fastest) {
				fastest = curFastest;
			}
		}
		fout << "Case #" << ti << ": " << setprecision(6) << setiosflags(ios::fixed | ios::showpoint) << (double)D / fastest << endl;
		//printf("Case #%d: %.6lf\n",ti, D / fastest);
	}
}