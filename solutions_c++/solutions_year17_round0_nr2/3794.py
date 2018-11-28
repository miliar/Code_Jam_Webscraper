#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <unordered_map>
#include <string>
#include <utility>
#include <unordered_set>
using namespace std;


long long getLastTidy(vector  <int> & v) {
	long long ret=0;
	bool first=true;
	for (int i=0; i < v.size()-1; i++) {
		if (v[i] > v[i+1]) {
			if (first)
				v[i]--;
			first=false;
			v[i+1] = 9;
		}

	}
	reverse(v.begin(),v.end());
	for (int i=0; i < v.size()-1; i++) {
		if (v[i] < v[i+1]) {
			v[i]=9;
			first=false;
			v[i+1]--;
		}

	}
	reverse(v.begin(),v.end());
	return ret;
}

long long intify(vector  <int> & v) {
	long long ret=0;
	while (v[0] == 0) {
		v.erase (v.begin(),v.begin()+1);
	}
	string str="";
	for (int i=0; i < v.size(); i++) {
		str+= v[i] + '0';
	}
	return stoll(str);
}

int main() {
	int t;
	cin >> t;
	for (int i=0; i < t; i++) {
		long long n;
		cin >> n;
		vector<int> v;
		for(; n; n/=10)
  			v.push_back( n%10 );
  		reverse(v.begin(),v.end());
  		getLastTidy(v);	
  		cout << "Case #" << i+1 << ": " << intify(v) << endl;
	}

	return 0;
}
