#include<map> 
#include<set>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<iomanip>
#include<algorithm>

using namespace std;

int main(){

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	double d,p,s,f;
	int n;

	int ntc;
	cin >> ntc;
	for (int tc=1;tc<=ntc;tc++){
		cin >> d >> n;
		double r = 0;
		for (int i=0;i<n;i++){
			cin >> p >> s;
			double k = (d-p)/s;
			if (k>r)
				r = k;
		}	
		cout << "Case #" << tc << ": ";
		cout << fixed <<setprecision(8)<< d/r << endl;
	}

	return 0;
}