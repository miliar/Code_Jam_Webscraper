#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main(){
	int n;
	cin>>n;
	for(int i = 0; i<n; i++){
		long long dist = 0;
		int num = 0;
		cin>>dist>>num;
		double max = 0;
		for(int t = 0; t<num; t++){
			long long pos = 0;
			int speed = 1;
			cin>>pos>>speed;
			double temp = double(dist-pos)/speed;
			max = max>temp?max:temp;
		}

		cout<<"Case #"<<i+1<<": "<<fixed<<setprecision(7)<<dist/max<<endl;
	}
	return 0;
}