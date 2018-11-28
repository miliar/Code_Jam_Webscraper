#include <cstdio>
#include <iostream>
#include <cstring>
#include <map>

using namespace std;

typedef long long LL;

string testfile = "C-large";

map<LL,LL,greater<LL> > Q;

LL N,K;

void add(LL x,LL cnt) {
	if (x<=0) return;
	//cout<<"Add "<<x<<' '<<cnt<<endl;
	if (Q.find(x)!=Q.end()) {
		Q[x] += cnt;
	}
	else Q[x] = cnt;
}

void run() {
	Q.clear();

	cin>>N>>K;

	Q[N] = 1;

	while (true) {
		LL L = Q.begin()->first;
		LL cnt = Q.begin()->second;

		//cout<<"Split"<<' '<<L<<' '<<cnt<<endl;

		Q.erase(Q.begin());

		LL l,r;

		r = L/2;
		l = L-r-1;

		if (K<=cnt) {
			cout<<r<<' '<<l<<endl;
			return;
		}

		K -= cnt;
		add(l,cnt);
		add(r,cnt);
	}
}

int main() {
	freopen((testfile+".in").c_str(),"r",stdin);
	freopen((testfile+".out").c_str(),"w",stdout);
	int testn;
	cin>>testn;
	for (int loop = 1; loop<=testn; ++loop) {
		cout<<"Case #"<<loop<<": ";

		run();
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
