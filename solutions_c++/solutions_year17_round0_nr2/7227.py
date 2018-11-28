#include <bits/stdc++.h>
using namespace std;
#define ll long long
vector < long long > vi;
int ptr[11];
int eend;


int main() {
	//freopen("input.txt" , "r" , stdin);
	//freopen("output.txt" , "w" , stdout);
	for(int i=1;i<=9;i++) {
		vi.push_back(i);
		ptr[i] = i - 1;
	}
	eend = 9;

	long long max1 = (ll)(1e+17);

	string s , tmp;
	ll bound;
	while(vi[eend -1] <= max1) {
		for(int i=1;i<=9;i++) {
			s = to_string(i);
			int k = ptr[i];
			for(int j=k;j<eend;j++) {
				tmp = s + to_string(vi[j]);
				bound = stoll(tmp);
				//if(bound > max1)
				vi.push_back(bound);
			}
			ptr[i] = vi.size() - (eend - k);
			//cout << i << " " << ptr[i] << endl;
		}
		eend = vi.size();
	}
	//cerr << "DONE !" << endl;
	int t;
	cin >> t;
	for(int i=1;i<=t;i++) {
		ll num;
		cin >> num;
		int pos = upper_bound(vi.begin() , vi.end() , num) - vi.begin() - 1;
		cout << "Case #" << i << ": " << vi[pos] << endl;
	}

	return 0;
}
