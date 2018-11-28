#include <iostream>
#include <iomanip>
#include <stdio.h>

using namespace std;

int main(){

	double number;
	cin >> number;

	for (int i = 0; i < number; ++i){
		
		double dis;
		cin >> dis;

		double n;
		cin >> n;

		double max = 0;
		for(int j = 0; j < n; j++){

			double a, b;
			cin >> a >> b;
			if((dis - a)/b > max)
				max = (dis - a)/b;
		}
		double re = dis/max;
		cout << "Case #" << i+1 << ": " ;// setprecision(6) << re << endl;
		printf("%.6f", re);
		cout << endl;

	}

}