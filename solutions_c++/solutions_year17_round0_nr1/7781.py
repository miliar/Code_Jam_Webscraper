#include <algorithm>
#include <cstdio>
#include <cmath>
#include <iterator>
#include <bitset>
#include <iostream>
#include <list>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <queue>
#include <deque>
#include <cassert>
#include <string>
#include <cstring>
#include <climits>

using namespace std;

#define ll long long
#define pii pair<int, int>
#define vi vector<int>
#define mp make_pair
#define pb push_back
#define fs first
#define sc second
#define sz(x) (int)x.size()
#define fill(x,a) memset(x, a, sizeof(x))
#define sortall(x) sort(x.begin(), x.end())


int main() {

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);


	int T;
	cin>>T;
	for(int t=1; t<=T; t++) {

		string s;
		int k, n;
		cin>>s>>k;
		int steps = 0;
		n = s.length();
		while(1) {

			int cnt = 0;
			for(int i=0; i<n; i++) {
				if(s[i] == '+') {
					cnt++;
				}
			}
			if(cnt == n) {
				cout<<"Case #"<<t<<": "<<steps<<"\n";
				break;
			}

			if(steps>1e6) {
				cout<<"Case #"<<t<<": IMPOSSIBLE\n";
				break;
			}

			int i;
			bool flag = false;
			for(i=0; i<n; i++) {
				if(s[i] == '-') {
					int j = i;
					while(s[j] == '-' && j<n) {
						j++;
					}
					int temp = j-i;
					if(temp%k == 0) {
						for(int l = i; l<j; l++) {
							s[l] = '+';
						}
						steps+=(temp/k);
					} else {

						if(temp>k) {
							steps+=(temp/k);
							for(int l=i; l< i+ (temp/k)*k; l++) {
								s[l] = '+';
							}
							temp-=(temp/k)*k;
						}
						i= j-temp;
						if(i+k>n) {
							for(int l = n-1 ; l>=(n-k); l--) {
								s[l] = (s[l]=='+'? '-' : '+');
							}
							steps++;
						} else {
							for(int l = i; l<i+k; l++) {
								s[l] = (s[l]=='+'? '-' : '+');	
							}
							steps++;
						}

					}
					
					break;
				}
			}

		}


	}


	return 0;
}





















