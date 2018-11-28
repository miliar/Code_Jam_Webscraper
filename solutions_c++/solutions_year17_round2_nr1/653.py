#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <list>
#include <cctype>
using namespace std;

int N;
double D;
list<pair<double, double> > q[2];

struct Horse {
	double K;
	double S;
} h[2000];

bool cmp(const Horse& h1, const Horse& h2) {
	return (h1.K < h2.K);
}

void work() {
	scanf("%lf%d", &D, &N);
	for (int i = 0; i < N; ++i) {
		scanf("%lf%lf", &h[i].K, &h[i].S);
	}
	sort(h, h + N, cmp);
	q[0].clear();
	q[1].clear();
	int cur = 0;
	for (int i = N - 1; i >= 0; --i, cur ^= 1) {
		q[cur].clear();
		q[cur].insert(q[cur].begin(), make_pair(h[i].K, h[i].S));
		if (i == N - 1) {
			q[cur].push_back(make_pair(D, h[i].S));
			continue;
		}

		list<pair<double, double> >::iterator it = q[cur^1].begin();
		double curK = q[cur^1].begin()->first, curS = q[cur^1].begin()->second;
		double curT = 0;
		for (++it; it != q[cur^1].end(); ++it) {
			double t1 = (double)(it->first - curK) / (double)(curS);
			double t2 = (double)(it->first - h[i].K) / (double)(h[i].S);
			if (curT + t1 > t2) {
				double dis = curK - (h[i].K + h[i].S * curT);
				double ds = h[i].S - curS;
				double t = dis / ds;
				double newK = curK + curS * t;
				q[cur].push_back(make_pair(newK, curS));
				break;
			}
			curT += t1;
			curK = it->first; curS = it->second;
		}
		for (; it != q[cur^1].end(); ++it) {
			q[cur].push_back(*it);
		}
		if (q[cur].size() == 1) {
			q[cur].push_back(make_pair(D, h[i].S));
		}

		/*
		cerr << i << endl;
		for (it = q[cur].begin(); it != q[cur].end(); ++it) {
			cerr << it->first << "," << it->second << "    ";
		}
		cerr << endl;
		*/
	}
	cur ^= 1;
	double t = 0;
	double curK = q[cur].begin()->first, curS = q[cur].begin()->second;
	list<pair<double, double> >::iterator it = q[cur].begin();
	for (++it; it != q[cur].end(); ++it) {
		t += (double)(it->first - curK) / curS;
		curK = it->first; curS = it->second;
	}
	if (curK < D) t += (D - curK) / curS;

	printf("%.8f\n", D / t);
}

int main() {
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		printf("Case #%d: ", i + 1);
		work();
	}
	return 0;
}
