#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>

using namespace std;

int main(){
	cout<<"launching function main"<<endl;
	ifstream file("A-large.in");
	ofstream outputfile("myoutput.txt");
	cout.precision(10);
	int T, S;
	long int D, N, K;
	long double max_speed, time;
	file>>T;
	for(int t=0;t<T;t++){
		time=0;
		//read input
		file>>D>>N;
		for(int i=0; i<N; i++){
			file>>K>>S;
			time=max(time,((long double)(D-K))/((long double)(S)));
		}
		//write output
		outputfile<<"Case #"<<(t+1)<<": "<<setprecision(10) <<(((long double)(D))/(time))<<endl;
	}
	file.close();
	outputfile.close();
}

