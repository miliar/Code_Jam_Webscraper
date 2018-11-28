#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

#define ifs cin
#define ofs cout
//ifstream ifs("B-small-attempt2.in");ofstream ofs("1.out");
//ifstream ifs("B-large.in");ofstream ofs("2.out");
//ifstream ifs("C-large.in");ofstream ofs("3.out");
vector<double> e,s;
vector<pair<int,int> > path[100];

void solve(int time){
	int n,k;
	cin >> n >> k;
	vector<int> r(n),h(n);
	for(int i = 0;i < n;i++) cin >> r[i] >> h[i];
	vector<pair<double,double> > yoko(n);
	for(int i = 0;i < n;i++){
		yoko[i] = make_pair(2*M_PI*r[i]*h[i],M_PI*r[i]*r[i]);
	}
	sort(yoko.begin(),yoko.end());
	double ans = 0;
	for(int i = 0;i < n;i++){
		double s = yoko[i].first+yoko[i].second;
		for(int j = 1,t = n-1;j < k;j++,t--){
			if(t == i){
				j--;
				continue;
			}
			s += yoko[t].first;
		}
		if(ans < s) ans = s;
	}
	//ofs << "Case #" << time << ": " << ans << endl;
	printf("Case #%d: %20f\n",time,ans);
}

int main() {
	int t;
	ifs >> t;
	//cout << "start" << endl;
	for(int i = 1;i <= t;i++){
		solve(i);
	}
	//cout << "fin" << endl;
	return 0;
}
