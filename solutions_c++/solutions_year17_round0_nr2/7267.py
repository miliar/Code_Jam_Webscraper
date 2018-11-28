#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <map>
#include <set>

#define pii pair <int, int>
#define pb push_back
#define ll long long
#define ss second
#define ff first
#define N 500010

using namespace std;

int t;
string s;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> t;
	int now = 0;
	while(t--) {
		cin >> s, now++;
		int l = 0;
		int l2 = -1;
		
		for(int i=0; i < s.length(); i++) {
			if(s[i] > s[i+1] && i != s.length()-1) {
				l2 = l;
				break;
			}
			if(s[i] != s[i+1])
				l = i+1;
		}
		int j = 0;
		
		if((s[0]-48)-1 == 0 && l2 == 0)
			j++;
		
		cout << "Case #" << now << ": ";
		if(l2 == -1) {
			cout << s << "\n";
			continue;
		}
		
		for(int i=j; i < s.length(); i++) {
			if(i < l2)
				cout << s[i];
			if(i == l2)
				cout << (s[i]-48)-1;
			if(i > l2)
				cout << '9';
		}
		cout << "\n";
	}
}

