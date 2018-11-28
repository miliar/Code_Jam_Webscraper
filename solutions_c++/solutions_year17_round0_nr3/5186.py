#include <iostream>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>    // std::reverse
using namespace std;

struct range{
	int d;
	int p;
	int q;
};

bool operator<(range a, range b) {
	return a.d > b.d;
}

struct level{
	vector<range> ranges;
};

level levels[30];

void divide(range r, int l) {
	range a, b;

	a.p = r.p;
	a.q = (r.p+r.q)/2 - 1;//(r.d % 2 == 0 ? 0 : 1);
	a.d = a.q - a.p + 1;
	
	b.p = (r.p+r.q)/2 + 1;
	b.q = r.q;
	b.d = b.q - b.p + 1;
	levels[l+1].ranges.push_back(a);
	levels[l+1].ranges.push_back(b);
}



int main() {
	ios_base::sync_with_stdio(0);

	int T;
	cin>>T;

	for(int tt=1; tt<=T; tt++) {
		int K, N;
		cin>>N>>K;

		int p=0;
		int t=1;
		while(t<=K) {
			t *= 2;
			p++;
		}

		//cout<<p<<endl;
		range r;
		r.p = 1;
		r.q = N;
		r.d = (r.q - r.p + 1);
		levels[0].ranges.push_back(r);

		vector<range> V;

		for(int i=0; i<p; i++)
			for(int j=0; j<levels[i].ranges.size(); j++) {
				divide(levels[i].ranges[j], i);
				V.push_back(levels[i].ranges[j]);
			}

		sort(V.begin(), V.end());

		//for(int i=0; i<V.size(); i++)
			// cout<<V[i].p<<" "<<V[i].q<<" "<<V[i].d<<endl;

		int x = V[K-1].d/2 ;
		int y = V[K-1].d/2 - (V[K-1].d % 2 == 0 ? 1 : 0);
		
		for(int i=0; i<30; i++)
			levels[i].ranges.clear();
		V.clear();
		cout<<"Case #"<<tt<<": "<<x<<" "<<y<<endl;

	}
	return 0;
}