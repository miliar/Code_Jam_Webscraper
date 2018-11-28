/*
 * codejam.cpp
 *
 *  Created on: 09-Apr-2017
 *      Author: naivehobo
 */
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	int t;
	cin>>t;
	vector<int> num;
	int n, k, l, r;
	for(int i=1;i<=t;i++){
		cin>>n>>k;
		while(k>0){
			if(n%2==1){
				l = n/2;
				r = n/2;
				num.push_back(l);
				num.push_back(r);
			}
			else{
				l = n/2-1;
				r = n/2;
				num.push_back(r);
				num.push_back(l);
			}
			k--;
			sort(num.begin(),num.end(),greater<int>());
			n = num[0];
			num.erase(num.begin());
		}
		cout<<"Case #"<<i<<": "<<r<<' '<<l<<endl;
		num.clear();
	}
	return 0;
}
