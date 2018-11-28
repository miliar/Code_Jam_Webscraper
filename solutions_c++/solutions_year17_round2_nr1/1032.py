#include<iostream>
#include <fstream>
#include <cstdlib>
#include <stdint.h>
#include <iomanip>

using namespace std;

int main(){
	int n; 
	ifstream fp("A-large.in");
	ofstream outfile;
	outfile.open("A-large.out"); 
	if (fp){
		fp >> n;
		for (int i = 0; i < n; i++){
			int64_t des;
			int N; 
			fp >> des;
			fp >> N;
			long double max = 0;
			for (int j = 0; j < N; j++){
				int64_t pos;
				fp >> pos;
				int speed;
				fp >> speed;
				long double time = (long double)(des - pos)/((long double)speed);
				if (max < time) max = time;
			}
			outfile << "Case #" << i+1 << ": ";
			long double ans = (long double)des/max;
			outfile << fixed << setprecision(6) << ans << endl;
		}
	}
	return 0;
}
