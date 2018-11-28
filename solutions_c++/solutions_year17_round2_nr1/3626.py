#include <iostream>
#include <iomanip>
using namespace std;

const int MAX_N = 1000+10;

double s[MAX_N];
double k[MAX_N];

int main(){
	int T;
	cin >> T;
	for (int t=1; t<=T; t++){
		double D;
		int n;
		cin >> D >> n;
		for (int i=0;i<n;i++){
			cin >> k[i] >> s[i];
		}
		int mn = n-1;
		for (int i=n-2;i>=0;i--){
			double a = s[mn] * (1 + (k[mn] - k[i]) / (D - k[mn]));
			if (a > s[i])
				mn = i;
		}
		double ans = s[mn] * (1 + (k[mn]) / (D - k[mn]));


		cout << "Case #" << t << ": ";
		cout << fixed << setprecision(6) << ans << endl;


	}

	return 0;
}

//double ans = 10e10;
		/*
		for (int i=0;i<n;i++){
			double k, s;
			cin >> k >> s;
			//double a = (D * s)/(D-k);
			double a = s * (1 + k) / (D - k);
			if (a < ans)
				ans = a;
		}
		*/
