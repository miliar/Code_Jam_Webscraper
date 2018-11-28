#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <cstdlib>
#include <time.h>
#include <bits/stdc++.h>


using namespace std;

int check(double mid, int *s , int * k , int n , int d){
	double t = (double)d/mid;
	//cout << "t" << t<< endl;
	int i;
	for(i=0;i<n;i++){
		double temp = (double)k[i] + (double)s[i]*t;
		if(temp < (double)d)return 0;
	}
	return 1;
}

int main(){
	cout.precision(6);
	int t;
	cin >> t;
	int i;
	int d,n,j;
	for(i=0;i<t;i++){
		cin >> d >> n;
		int k[n],s[n];
		for(j=0;j<n;j++){
			cin >> k[j] >> s[j];
		}
		double high,low,mid;
		high = (double)(d)* 10000, low = 0;
		while(abs(high - low) >= 0.000001){
			mid = (high + low)/2;
			//cout << high << " " << low << " " << mid << endl;
			if(check(mid,s,k,n,d))low = mid;
			else high = mid;
		}
		printf("Case #%d: %.6lf\n",i+1, low);
		//cout << "Case #" << i+1 << ": " << low << endl;
	}
}