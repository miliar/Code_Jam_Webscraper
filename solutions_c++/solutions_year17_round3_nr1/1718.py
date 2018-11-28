#include "stdafx.h"

#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>

const double PI = 3.141592653589793238463;

using namespace std;

vector<int> r, h, nr, nh;
vector<double> hh;

int main()
{
	int i, j;
	int ncase, n, k;
	cin>>ncase;
	double ans, best;
	for (int icase=1;icase<=ncase;icase++) {
		cin>>n>>k;
		r.resize(n); nr.resize(n);
		h.resize(n); hh.resize(n);
		for (i=0;i<n;i++) {
			cin>>r[i]>>h[i];
			nr[i]=i;
			hh[i]=2*PI*r[i]*h[i];
		}
		sort(nr.begin(), nr.end(), [](const int &a, const int &b){return r[a]>r[b];});

		best=0;
		for (i=0;i<n;i++) {
			nh.clear();
			for (j=i+1;j<n;j++)
				nh.push_back(nr[j]);				
			sort(nh.begin(), nh.end(), [](const int &a, const int &b){return hh[a]>hh[b];});

			ans = PI * r[nr[i]] * r[nr[i]];
			ans += 2 * PI * r[nr[i]] * h[nr[i]];
			for (j=0;j<k-1&&j<nh.size();j++) 
				ans += hh[nh[j]];
			if (ans>best) best=ans;
		}

		cout << fixed << std::setprecision(9);
		cout << "Case #" << icase << ": " << best << endl;
	}
}