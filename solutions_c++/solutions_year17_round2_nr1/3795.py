#include "stdafx.h"

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>

using namespace std;

//#define	MAX	1000

vector<int> k, s, o;

int main()
{
	int i;
	int ncase, d, n;
	double a;
	cin>>ncase;
	for (int icase=1;icase<=ncase;icase++) {
		cin>>d>>n;
		k.resize(n); s.resize(n); o.resize(n);
		for (i=0;i<n;i++) {
			o[i]=i;
			cin>>k[i]>>s[i];
		}
		sort(o.begin(), o.end(), [](const int &a, const int &b){return k[a]>k[b];});
		//for (auto i: o) cout<<i<<"("<<k[i]<<","<<s[i]<<") "; cout<<endl;

		a = (double)(d-k[o[0]]) / s[o[0]];
		for (i=1;i<n;i++) 
			if ((double)(d-k[o[i]]) / s[o[i]] > a)
				a = (double)(d-k[o[i]]) / s[o[i]];
		
		cout << fixed << std::setprecision(6);
		//cout << "d=" << d << ", a=" << a << endl;
		cout << "Case #" << icase << ": " << d/a << endl;
	}
}