#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;

const int MX = 10000;

struct H {
	int k;
	int s;

	vector<double> kL; //later
	vector<int> sL; //later
};

int d, n;
vector<H> h(MX);


bool compare(H a, H b){
	return a.k > b.k;
}

double getPos(double cK, int cS, double fK, int fS){
	int rS = cS - fS;
	double rD = fK - cK;
	if(rS <= 0) return d;
	
	double t = rD/rS;
	if(fS*t + fK >= d) return d;
	return cK + cS * t;
}

void compute(int current){
	int front = current - 1;
	for(int i=0;i<h[front].sL.size();i++){
		double p =getPos(h[current].kL.back(), h[current].sL.back(), h[front].kL[i], h[front].sL[i]);
		h[current].kL.push_back(p);
		h[current].sL.push_back(h[front].sL[i]);
	}
}

void solve(){
	cin>>d>>n;
	for(int i=0;i<n;i++) {
		H tmp;
		cin>>tmp.k>>tmp.s;

		tmp.kL.push_back(tmp.k);
		tmp.sL.push_back(tmp.s);
		h.push_back(tmp);
	}
	sort(h.begin(), h.end(), compare);

	for(int i=1;i<n;i++) compute(i);

	H last = h[n-1];

	double t = 0;
	for(int i=0;i<last.sL.size()-1;i++){
		t += (last.kL[i+1] - last.kL[i]) / last.sL[i];
	}
	t+= (d - last.kL[last.kL.size()-1]) / last.sL[last.kL.size()-1];
	printf("%0.6f\n", (d/t));
}

int main(){
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		printf("Case #%d: ", i+1);
		solve();
		h.clear();
	}
	return 0;
}