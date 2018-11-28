#include <iostream>
#include <iomanip>

using namespace std;

int main(){
	int q;
	cin >> q;
	for(int i=1;i<=q;i++){
		int d;
		cin >> d;
		int n;
		cin >> n;

		double maximum = -1;
		for(int j=0;j<n;j++){
			int at, speed;
			cin >> at >> speed;

			if(1.0*(d-at)/speed > maximum){
				maximum = 1.0*(d-at)/speed;
			}
		}

		cout << "Case #" << i << ": " << setprecision(10) << d*1.0/maximum << endl;
	}
	return 0;
}