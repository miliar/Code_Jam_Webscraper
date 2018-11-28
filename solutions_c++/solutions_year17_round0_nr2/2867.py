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
#include <sstream>
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
		cout<<"Case #"<<test<<": ";
		long long n;
		cin>>n;
		ostringstream os;
		os<<n;
		string s = os.str();
		for (int k=0; k<20; k++) {
			for (int i=0; i<s.length() - 1; i++) {
				if (s[i] > s[i + 1]) {
					s[i]--;
					for (int j=i+1; j<s.length(); j++) {
						s[j] = '9';
					}
					break;
				}
			}
		}
		int ptr = 0;
		while (s[ptr] == '0') ptr++;
		cout<<s.substr(ptr, s.length() - ptr)<<endl;
	}
	return 0;
}