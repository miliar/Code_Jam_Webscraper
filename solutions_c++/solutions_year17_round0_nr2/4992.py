#include <iostream>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>    // std::reverse
using namespace std;

bool trynum(int n) {
	stack<int> S;
	while( n > 0) {
		S.push( n%10 );
		n /= 10;
	}

	int p = S.top();
	S.pop();
	
	bool f = true;
	while(!S.empty()) {
		int t = S.top();
		S.pop();
		
		if(t < p) {
			f = false;
			break;
		}
		p = t;
	}
	return f;
}


int main() {
	ios_base::sync_with_stdio(0);

	int T;
	cin>>T;

	for(int tt=1; tt<=T; tt++) {

		long long N;
		cin>>N;

		vector<int> d;

		long long NN = N;
		stack<int> S;
		int p = 0;
		while(NN > 0) {
			d.push_back( NN % 10);
			NN /= 10;
		}
		d.push_back(0);
		reverse(d.begin(), d.end());

		

		for(int i=1; i<d.size(); i++) {
			if(d[i] < d[i-1]) {
				if(d[i-1] > 0)
					d[i-1]--;
				else {
					d[i-2]--;
					d[i-1] = 9;
				}
				for(int j=i; j<d.size(); j++)
					d[j] = 9;
				i = 0;
			}
		}

		long long res = 0;
		long long mng = 1;
		for(int i=d.size()-1; i >= 0; i--) {
			res += mng * d[i];
			mng *= 10;
		}
		//cout<<endl;
		d.clear();

		cout<<"Case #"<<tt<<": "<<res<<endl;

	}
	return 0;
}