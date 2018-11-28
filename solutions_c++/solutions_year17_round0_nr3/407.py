#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>

using namespace std;

//#define ifs cin
//#define ofs cout
//ifstream ifs("C-small-1-attempt0.in");ofstream ofs("1.out");
//ifstream ifs("C-small-2-attempt0.in");ofstream ofs("2.out");
ifstream ifs("C-large.in");ofstream ofs("3.out");

struct vq{
	vector<pair<long long,long long> > vp;

	void add(int i,long long p,long long n){
		for(int j = i;j <= vp.size();j++){
			if(j == vp.size()){
				vp.push_back(make_pair(p,n));
				break;
			}
			if(vp[j].first == p){
				vp[j].second += n;
				break;
			}
		}
	}
};
void solve(int time){
	long long ansmax,ansmin;
	long long n,k;
	ifs >> n >> k;
	long long a,b,c,d;
	vq v;
	a = 0;b = n;
	v.add(0,n,1);
	for(int i = 0;i < v.vp.size();i++){
		b = v.vp[i].first;
		a += v.vp[i].second;
		ansmin = (b-1)/2;
		if((b-1)%2) ansmax = ansmin+1;
		else ansmax = ansmin;
		if(a >= k) break;
		v.add(i,ansmax,v.vp[i].second);
		v.add(i,ansmin,v.vp[i].second);
	}
	ofs << "Case #" << time << ": " << ansmax << ' ' << ansmin << endl;
}

int main() {
	int t;
	ifs >> t;
	cout << "start" << endl;
	for(int i = 1;i <= t;i++){
		solve(i);
	}
	cout << "fin" << endl;
	return 0;
}
