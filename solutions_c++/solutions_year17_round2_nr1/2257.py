#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <iomanip>
using namespace std;
int main() {
	ifstream fin;
	ofstream fout;
	vector < pair<int, int> > a;
	fin.open("sample.txt");
	fout.open("answers.txt");
	int t, i, T, d, n, x, y;
	double j;
	char ch;
	fin>>t;
	for(T=1;T<=t;T++) {
		fin>>d>>n;
		int min=INT_MAX, mini=-1;
		for(i=0;i<n;i++) {
			fin>>x>>y;
			a.push_back(make_pair(x,y));
		}
		sort(a.begin(), a.end());
		i=n-1;
		j=(d-(a[i].first))*1.0/a[i].second;
		for(i=n-2;i>=0;i--) {
			double temp=(d-(a[i].first))*1.0/a[i].second;
			if(temp>j)
				j=temp;
		}
		fout<<"Case #"<<T<<": "<<setprecision(9)<<fixed<<d/j<<endl;
		a.clear();
	}
	return 0;
}