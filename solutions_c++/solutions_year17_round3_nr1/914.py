#include <iostream>
#include <iomanip>


using namespace std;

#define MAXN 1050
#define PI           3.14159265358979323846

int main(){
	int t;
	cin >> t;
	int c=1;
	while (c<=t){
		cout << "Case #" << c++ << ": ";
		int n,k;
		cin >> n >> k;
		pair<double,double> rh[MAXN];
		double MaxR = 0;
		double MaxRLocal = 0;
		int index;
		for (int i=0;i<n;i++){
			double R,H;
			cin >> R >> H;
			if (R>MaxR){
				MaxR=R;
			}
			rh[i].first = 2*PI*R*H;
			rh[i].second = R;
		}
		sort(rh,rh+n);

		for (int i=0;i<n;i++){
			if (rh[i].second==MaxR)
				index = i;
		}

		double ans = 0;

		for (int i=0;i<k;i++){
			ans+=(rh[(n-1)-i].first);
			if (rh[(n-1)-i].second>MaxRLocal){
				MaxRLocal=rh[(n-1)-i].second;
			}
		}
		ans += PI*(MaxRLocal*MaxRLocal);	// Potential answer
		double diff = 0;
		if (MaxRLocal!=MaxR)
			diff = (PI*(MaxR*MaxR-MaxRLocal*MaxRLocal))-(rh[(n-1)-(k-1)].first - rh[index].first); // Replace least height one with max radius one
		if (diff>0)ans+=diff;
		cout << setprecision(30) << ans;
		cout << '\n';
	}
}