#include <iostream>
#include <iomanip>

using namespace std;

int main(){
	int t;
	cin >> t;
	int c=1;
	while (c<=t){
		int d,n;
		cin >> d >> n;
		double MAX = 0;
		for (int i=0;i<n;i++){
			double k,s;
			cin >> k >> s;
			double Time = (d-k)/s;
			MAX = max(Time,MAX);
		}
		cout << "Case #" << c << ": ";
		cout << setprecision(30) << d/MAX << endl;
		c++;
	}
}