#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>
#include <map>

#define IN_FILE "C-large.in"
#define OUT_FILE "outL.txt"

using namespace std;

typedef long long ll;
typedef long double ld;

map< ll, ll > m1;

int main() {
	ios::sync_with_stdio(0);
	ifstream xin(IN_FILE);
	ofstream xout(OUT_FILE);
	cin.rdbuf(xin.rdbuf());
	cout.rdbuf(xout.rdbuf());
	ll i, j, t1, t2, t3, t4, n, ans,cnt=0,k,t;	
	cin >> t;
	while (t--) {
		cin >> n >> k;
		m1.clear();
		m1[n]++;
		for (i = 0; i < k; ) {
			auto it = m1.rbegin();
			t1 = it->first;
			if (t1 % 2 == 0) {
				t2 = t1 / 2 - 1;
				t3 = t1 / 2;
			}
			else {
				t2 = t3 = (t1-1) / 2;
			}
			t2 = max(t2, 0ll);
			m1[t2]+=m1[t1];
			m1[t3]+=m1[t1];
			//cout <<"y= "<< m1[t1] << " "<< t1 << endl;
			if (i + m1[t1] >= k) {
				ans = t1;
				break;
			}
			else {
				i += m1[t1];
				m1.erase(t1);
			}
		}
		if (ans % 2 == 0) {
			t2 = (ans-1) / 2 ;
			t3 = ans / 2;
		}
		else {
			t2 = t3 = (ans - 1) / 2;
		}
		cnt++;
		cout << "Case #" << cnt << ": " << t3 <<" "<< t2 << "\n";
	}
	system("pause");
	return 0;
}
