/*
	CodeJam 2017 - Qualification Round
	Problem A. Oversized Pancake Flipper
	Author: Youssef ElGhareeb
*/	

#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <queue>
#include <functional>
#include <cstring>
#include <string>
using namespace std;

#define pii pair<int, int>
#define mp make_pair
#define loop(i,n) for (int i=0; i<n; i++)
#define pb push_back
#define ll long long
#define vi vector<int>

int main () {
	ios_base::sync_with_stdio(false);
	int tests;
	cin>>tests;
	for(int test=1; test<=tests; test++) {
		string s;
		int k, n, res = 0;
		cin>>s>>k;
		n = s.length();
		for (int i=n-k; i>=0; i--) {
			if (s[i + k - 1] == '-') {
				res++;
				for (int j=i; j <= i + k - 1; j++) {
					if (s[j] == '+') s[j] = '-';
					else s[j] = '+';
				}
			}
		}
		/* Consistency check */
		bool flag = true;
		for (int i=0; i<n; i++) {
			if (s[i] == '-') {
				flag = false;
				break;
			}
		}
		cout<<"Case #"<<test<<": ";
		if (flag) {
			cout<<res<<endl;
		/*	cout<<"\t";
			for (int j=0; j<vres.size(); j++) cout<<vres[j]<<" ";
			cout<<endl; */
		}
		else cout<<"IMPOSSIBLE\n";
	}
	return 0;
}