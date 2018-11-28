// pb-1-1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	cin>>T;
	for(int t=1; t<=T; t++) {
		int n;
		double d;
		cin>>d;
		cin>>n;
		double m = 0.0; 
		for(int i=0; i<n; i++) {
			double k, s;
			cin>>k>>s;
			m = max(m, (d-k)/s);
		}
		if(m==0.0) m = 1.0;
		double res = d / m;
		cout<<"Case #"<<t<<": "<<fixed<<setprecision(6)<<res<<endl;
	}
	return 0;
}

