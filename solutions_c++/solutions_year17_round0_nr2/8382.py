#include<cstdio>
#include<cmath>
#include<iostream>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<cassert>
#include<string>
#include<stack>
#include<unordered_set>

using namespace std;

int main( int argc,char **argv)
{
	int cases;
	cin >> cases;
	for(int iter = 1; iter <= cases; iter++) {
		unsigned long n;
		cin >> n;
		queue<unsigned long> q;
		unordered_set<unsigned long> S;
		for(int i=1;i<=9;i++) {
			q.push((unsigned long)i);
			S.insert((unsigned long)i);
		}
		unsigned long res = 1;
		while(!q.empty()) {
			unsigned long t = q.front(); q.pop();
			if( t > res && t <= n ) {
				res = t;
			}
			unsigned long rem = t%10;
			for(int i=rem;i<=9;i++) {
				unsigned long t1 = t * 10 + (unsigned long)i;
				if(t1 > t && S.find(t1) == S.end() && t1 <= n) {
					q.push(t1);
					S.insert(t1);
				}
			}
		}
		cout << "Case #" << iter << ": " << res << endl;
	}
	return 0;
}
