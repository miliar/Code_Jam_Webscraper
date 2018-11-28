#include<map> 
#include<set>
#include<cmath>
#include<string>
#include<vector>
#include<sstream>
#include<iomanip>
#include<iostream>
#include<algorithm>

using namespace std;

#define	MAX	1010

#define	pi (2*acos(0.0))

pair<double,double> p[MAX];
double res[MAX][MAX];

inline double eval(double r,double h){
	return pi*r*r+2*pi*r*h;
}

int main(){

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int n,k;


	int ntc;
	cin >> ntc;
	for (int tc=1;tc<=ntc;tc++){
		cin >> n >> k;
		for (int i=0;i<n;i++)
			cin >> p[i].first >> p[i].second;
		sort(p,p+n);
		memset(res,0,sizeof(res));
		for (int i=0;i<n;i++){
			res[i][0] = 0;
			res[i][1] = eval(p[i].first,p[i].second);
			double a = eval(p[i].first,p[i].second);
			for (int j=2;j<=min(i+1,k);j++)
				for (int m=j-2;m<i;m++){
					double &r = res[i][j];
					r = max(r,res[m][j-1]+a-pi*p[m].first*p[m].first);
				}
		}
		double r = 0;
		for (int i=k-1;i<n;i++)
			if (res[i][k]>r) r = res[i][k];

		cout << "Case #" << tc << ": " << fixed << setprecision(10) << r << endl;
	}

	return 0;
}