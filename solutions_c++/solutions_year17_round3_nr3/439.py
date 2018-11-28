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
vector<pair<int,int> > path[100];

void solve(int time){
	int n,k;
	cin >> n >> k;
	vector<double> p(n);
	double u;
	cin >> u;
	double s;
	for(int i = 0;i < n;i++){
		cin >> p[i];
	}
	sort(p.begin(),p.end());
	p.push_back(1);
	for(int i = 0;i < n;i++){
		if(u > (p[i+1]-p[i])*(i+1)){
			u -= (p[i+1]-p[i])*(i+1);
			for(int j = 0;j <= i;j++){
				p[j] = p[i+1];
			}
		}
		else{
			for(int j = 0;j <= i;j++){
				p[j] += u/(i+1);
			}
			break;
		}
	}
	double ans = 1;
	for(int i = 0;i < n;i++){
		ans *= p[i];
	}
	//ofs << "Case #" << time << ": " << ans << endl;
	printf("Case #%d: %.20f\n",time,ans);
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
