#include <iostream>
#include <istream>
#include <fstream>
#include <string>
#include <cstdio>
#include <limits>
using namespace std;

double calc(long Dist,long N, long *position, long *speed){
	double maxTime=0;
	for(int i=0; i<N;i++){
		double curTime = (double)(Dist-position[i])/(double)speed[i];
		if(maxTime<curTime){
			maxTime = curTime;
		}
	}
	cerr<<maxTime;
	return Dist/maxTime;
}
int main(int argc,char *argv[]) {
	freopen(argv[1],"r",stdin);
	freopen(argv[2],"w",stdout);
	int tests;
	cin >> tests;
	for(int i=0; i<tests; i++){
		long Dist, N;
		cin>>Dist>>N;
		long *position=new long[N];
		long *speed=new long[N];
		for(int j=0;j<N;j++){
			cin>>position[j]>>speed[j];

		}
		double result = calc(Dist, N, position, speed);
		cerr<<" "<<result<<endl;
		cout << "Case #"<< (i+1)<<": ";
		cout.precision(15);
		cout<<result<< endl;
		delete[]position;
		delete[]speed;
	}
	cerr<<std::numeric_limits<int>::max()<<" ";
	cerr<<std::numeric_limits<long>::max()<<" ";
	cerr<<std::numeric_limits<double>::digits<<" ";
	return 0;
}

