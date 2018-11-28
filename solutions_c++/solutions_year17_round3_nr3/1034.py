#include <iostream>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <iomanip>
#include <algorithm>
using namespace std;


struct core{
	double p;
};

bool operator<(core a, core b) {
	return a.p > b.p;
}

int main() {
	ios_base::sync_with_stdio(0);

	int T;
	cin>>T;

	for(int tt=1; tt<=T; tt++) {

		int N, K;
		cin>>N>>K;
		double U;
		cin>>U;
		
		priority_queue<core> Q;
		vector<core> V;
		core c;
		for(int i=0; i<N; i++){
			cin>>c.p;
			V.push_back(c);
		}
		c.p = 1;
		V.push_back(c);
		sort(V.begin(), V.end());

		// for(int i=0; i<V.size(); i++)
		// 	cout<<V[i].p<<" ";

		int l = 1;
		double lvl = V[V.size()-1].p;
		int r = V.size() - 1;
		for(int i=V.size()-1; i>0; i--) {
			if(U <= 0)
				break;
			r = i;
			double diff = (V[i-1].p-V[i].p)*(l);
			if(U > diff) {
				U -= diff;
				lvl = V[i-1].p;
			}
			else {
				lvl = lvl + U/l;
				break;
			}
			l++;
		}

		// while(!Q.empty() && U > 0) {
		// 	core a = Q.top();
		// 	Q.pop();
		// 	core b;
		// 	b.p = 1;
		// 	if(!Q.empty()) {
		// 		b = Q.top();
		// 		Q.pop();
		// 	}
		// 	double diff = fmin(b.p - a.p, U);
		// 	if(diff == 0 && U != 0)
		// 		diff = 0.000001;
		// 	U -= diff;
		// 	a.p += diff;
		// 	if(a.p < 1)
		// 		Q.push(a);
		// 	if(b.p < 1)
		// 		Q.push(b);
		// 	//cout<<Q.top().p<<" "<<U<<" "<<diff<<endl;

		// }
	 
		// double res = 1;
		// while(!Q.empty()) {
		// 	res *= Q.top().p;
		// 	Q.pop();
		// }
		long double res = 1;

		for(int i=0; i<V.size(); i++) {
			if(i < r) {
				res *= V[i].p;
				// cout<<V[i].p<<" ";
			}
			else {
				res *= lvl;
				//cout<<lvl<<" ";
			}

		}
		//cout<<endl;
		cout<<"Case #"<<tt<< setprecision (6) << fixed <<": "<<res<<endl;

	}
	return 0;
}