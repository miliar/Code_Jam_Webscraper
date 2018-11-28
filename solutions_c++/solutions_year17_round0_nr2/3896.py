#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#define pb push_back

using namespace std;

int main() {
	int t;
	string a;
	scanf("%d",&t);
	for (int ctr=1;ctr<=t;ctr++) {
		cin >> a;
		printf("Case #%d: ",ctr);
		if (a.size()==1) cout << a << endl;
		else {
			for (int i=0;i<a.size()-1;i++) {
				if (a[i]>a[i+1]) {
					int pos = i;
					char val = a[i];
					for (int j=i-1;j>=0;j--) {
						if (val==a[j]) pos = j;
						else break;
					}
					a[pos] = a[pos]-1;
					for (int j=pos+1;j<a.size();j++) a[j] = '9';
					break;
				}
			}
			bool toggle = true;
			for (int i=0;i<a.size();i++) {
				if (toggle && a[i]=='0') continue;
				else {
					toggle = false;
					cout << a[i];
				}
			}
			cout << endl;
		}
	}
}