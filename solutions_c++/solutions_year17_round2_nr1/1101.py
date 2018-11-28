#include <cstdlib>
#include <iostream>
#include <cstring>
#include <fstream>
#include <iomanip>
using namespace std;
int T;
int D;
int N;

int main(){
	fstream in;
	fstream out;
	out.open("output.txt",ios::out);
	in.open("input.txt",ios::in);
	in >> T;
	int P, K;
	for(int tc = 1; tc <= T; ++tc){
		in >> D >> N;
		double time = 0;
		for(int i = 0; i < N; ++i){
			in >> P >> K;
			time = max( 1.0*(D - P)/K,time);
		}
		
		double velocity = D/time;
		out <<  setprecision(6) << fixed << "Case #" << tc << ": " << velocity << endl;
	}
	
}
