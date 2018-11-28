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
	int ac,aj;
	cin >> ac >> aj;
	int cc = ac;
	vector<int> v(1440);
	vector<int> c(ac),d(ac),e(aj),f(aj);
	for(int i = 0;i < ac;i++){
		cin >> c[i] >> d[i];
		for(int j = c[i];j < d[i];j++){
			v[j] = 1;
		}
	}
	for(int i = 0;i < aj;i++){
		cin >> e[i] >> f[i];
		for(int j = e[i];j < f[i];j++){
			v[j] = -1;
		}
	}
	vector<int> most,lest;
	int inter = 0;
	if(ac+aj == 0){
		ofs << "Case #" << time << ": " << 2 << endl;
		return;
	}
	int before,len;
	for(int i = v.size()-1;i >= 0;i--){
		if(v[i] != 0){
			before = v[i];
			len = i-v.size()+1;
			break;
		}
	}
	int ans = ac*2;
	sort(c.begin(),c.end());
	sort(d.begin(),d.end());
	if(c.size() > 0){
	if(c[0] == 0 && d[d.size()-1] == 1440) ans -= 2;
	for(int i = 1;i < d.size();i++){
		if(c[i] == d[i-1]) ans -= 2;
	}
	}
	//cout << ans << endl;
	int al = 0;
	int status = v[v.size()-1];
	for(int i = 0;i < v.size();i++){
		if(v[i] == 1) al++;
		if(status == 0 && v[i] != 0){
			if(before == 1 && v[i] == 1){
				most.push_back(i-len);
			}
			else if(before != v[i]){
				inter += i-len;
			}
			else{
				lest.push_back(i-len);
			}
		}
		if(status != 0 && v[i] == 0){
			len = i;
		}
		if(v[i] != 0) before = v[i];
		status = v[i];
	}
	sort(most.begin(),most.end());
	sort(lest.begin(),lest.end());
	for(int i = 0;i < most.size();i++){
		if(720-al >= most[i]){
			al += most[i];
			ans -= 2;
		}
		else{
			al = 720;
			break;
		}
	}
	//cout << ans << endl;
	al += inter;
	for(int i = lest.size()-1;i >= 0;i--){
		if(al >= 720) break;
		al += lest[i];
		ans += 2;
	}
	ofs << "Case #" << time << ": " << ans << endl;
	//printf("Case #%d: %20f\n",time,ans);
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
