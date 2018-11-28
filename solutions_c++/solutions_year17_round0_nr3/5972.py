#include "bits/stdc++.h"

using namespace std;

const int N = 7e3 + 5;
const int M = 1e5 + 5;
const int LN = 17;
const int SQRTN = 325;
const double PI = acos(-1.0);
const double EPS = 1e-7;
const int INF = 1e9;

typedef long long ll;
typedef long double ld;

int main(){
	int t;
	cin >> t;
	for(int tc = 1; tc <= t; tc++){
		int n, k;
		cin >> n >> k;
		
		multiset<int> s;
		s.insert(n);
		for(int i = 0; i < k; i++){
			int x = *s.rbegin();
			s.erase(s.find(x));
			int minn = (x - 1)/2, maxx = x/2;
			if(i == k - 1){
				cout << "Case #" << tc << ": " << maxx << " " << minn << endl;
			}
			s.insert(minn);
			s.insert(maxx);
		}
	}
  return 0;
}