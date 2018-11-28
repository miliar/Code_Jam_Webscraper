#include <iostream>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <iomanip>
#include <algorithm>
using namespace std;


struct pancake{
	int r, h;
	long double pp, pb;
	bool d;
	int n;
};

struct pancake2{
	int r, h;
	long double pp, pb;
	bool d;
	int n;
};

pancake2 pan2(pancake a) {
	pancake2 h;
	h.r = a.r;
	h.h = a.h;
	h.n = a.n;
	h.pp = a.pp;
	h.pb = a.pb;
	h.d = a.d;
	return h;
}

bool operator<(pancake2 a, pancake2 b) {
	return a.pb > b.pb;
}

bool operator<(pancake a, pancake b) {
	return a.r > b.r;
}

long double brut(vector<pancake> V, int p, int k, int K) {
	if(p >= V.size() && k != K)
		return 0;
	if(K == k) {
		// for(int i=0; i<V.size(); i++)
		// 	cout<<V[i].d<<" ";
		// cout<<endl;
		long double m = 0;
		for(int i=0; i<V.size(); i++)
			if(!V[i].d) {
				m+=V[i].pp;
				break;
			}
		for(int i=0; i<V.size(); i++)
			if(!V[i].d)
				m+=V[i].pb;
		//cout<< setprecision (9) << fixed <<m<<endl;
		return m;
	}
	V[p].d = true;
	long double m1 = brut(V, p+1, k-1, K);
	V[p].d = false;
	long double m2 = brut(V, p+1, k, K);
	return fmax(m1, m2);
}


int main() {
	ios_base::sync_with_stdio(0);

	int T;
	cin>>T;

	for(int tt=1; tt<=T; tt++) {

		int N, K;
		cin>>N>>K;

		vector<pancake> V;
		int r, h;
		for(int i=0; i<N; i++) {
			pancake p;
			cin>>r>>h;
			p.r = r;
			p.h = h;
			p.pp = M_PI*r*r;
			p.pb = 2*M_PI*r*h;
			p.d = false;
			p.n = i;
			V.push_back(p);
		}
		sort(V.begin(), V.end());

		//for(int i=0; i<V.size(); i++)
		//	cout<<V[i].n<<" "<<V[i].pp<<" "<<V[i].pb<<endl;

		if(N == K) {
			long double r = 0;
			r += V[0].pp;
			for(int p = 0; p<V.size(); p++) {
				r += V[p].pb;
			}
			cout<<"Case #"<<tt<< setprecision (9) << fixed <<": "<<r<<endl;
			continue;
		}

		long double tab[1017];
		bool B[1017];
		for(int i=0; i<N+7; i++)
			tab[i] = B[i] = 0;

		priority_queue<pancake2> Q;
		//cout<<"hi"<<endl;
		long double m = 0;
		int k = K-1;
		if(k != 0)
		for(int i=V.size()-1; i>0; i--) {
			pancake2 p2 = pan2(V[i]);
			if(Q.size() < k) {
				
				Q.push(p2);
				m += p2.pb;
			} else {
				pancake2 tmp = Q.top();
				
				if(p2.pb > tmp.pb) {
					m -= tmp.pb;
					Q.pop();
					
					m += p2.pb;
					Q.push(p2);
					
					B[i] = true;
				}
			}
			if(Q.size() == k)
				tab[i] = m;
			else
				tab[i] = 0;
		}
		//cout<<tab[1]<<endl;
		//cout<<"hi"<<endl;
		while(!Q.empty()) {
			// if(tt == 7)
				
			Q.pop();
		}
	

		long double res = 0;
		for(int p = 0; p<V.size()-k; p++) {
			long double tmp = V[p].pp + V[p].pb;
			if(k == 0)
				res = fmax(res, tmp);
			for(int i=p+1; i<V.size(); i++) {
				if(tab[i] != -1)
					res = fmax(res, tmp+tab[i]);
				//cout<<tmp+tab[i]<<endl;
			}
		}
	
		// for(int i=0; i<V.size(); i++)
		// 	cout<<V[i].r<<endl;
		//long double res = brut(V, 0, N, K);
		cout<<"Case #"<<tt<< setprecision (9) << fixed <<": "<<res<<endl;
	}
	return 0;
}