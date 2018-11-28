//Irvin Gonzalez
//a


#include <iostream>
#include <string>
#include <vector>
#include <limits>
#include <algorithm>
#include <cmath>

using namespace std;


const double PI  = 3.14159265358979323846264338327950;
double solve2(int k, int pos, vector<long> rad, vector<long> hei) {
	double radi = rad[pos];
	double height = hei[pos];
	rad.erase(rad.begin() + pos);
	hei.erase(hei.begin() + pos);
	--k;
	double tot = PI * 2 * radi * height;
	for(int i = 0; i < hei.size(); ++i) {
		if(rad[i] > radi) {
			rad.erase(rad.begin() + i);
			hei.erase(hei.begin() + i); } }

	vector<double> sa;
	for(int i = 0; i < hei.size(); ++i){
		double cur = PI * 2 * (double)hei[i] * (double)rad[i]; 
		sa.push_back(cur);}
	sort(sa.begin(), sa.end());
	while(k != 0) {
		tot += sa.back();
		sa.pop_back();
		--k; }
	//cout << radi << endl;
	//cout << height << endl;	
	return tot + (PI*pow(radi, 2)); }

void solve() {
	int n;
	int k;
	cin >> n >> k;
	vector<long> rad;
	vector<long> hei;
	for(int i = 0; i < n; ++i) {
		long r;
		cin >> r;
		rad.push_back(r);
		long h;
		cin >> h;
		hei.push_back(h); }
	vector<long> radcpy (rad);
	long smallr = numeric_limits<long>::max();
	for(int i = 0; i < k; ++i) {
		smallr = numeric_limits<long>::max();
		int pos = 0;
		for(int i = 0; i < radcpy.size(); ++i){
			if(radcpy[i] < smallr){
				smallr = radcpy[i];
				pos = i; } }
		radcpy.erase (radcpy.begin() + pos); }
	double tot = 0;
	for(int i = 0; i < n; ++i) {
		double cur = 0;
		if(rad[i] >= smallr) {
		//	cout << "here" << endl;
			cur = solve2(k, i, rad, hei);
			if(cur > tot)
				tot = cur; } }
	cout << fixed << tot;
}
int main() {

	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl; }
	return 0;
}
