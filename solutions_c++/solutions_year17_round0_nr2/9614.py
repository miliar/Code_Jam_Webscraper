#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void sub(vector<int> &v) {
	for(int i=v.size() - 1; i >= 0; --i) {
		if(v[i]==0) {
			v[i]=9;
		} else {
			--v[i];
			break;
		}
	}
}

bool zero(vector<int> const&v) {
	for(int i=0;i<v.size();++i) {
		if(v[i]!=0) return false;
	}
	return true;
}

bool equ(vector<int> const&v, vector<int> const&y) {
	for(int i=0;i<v.size();++i) {
		if(v[i]!=y[i]) return false;
	}
	return true;	
}

int main() {
	freopen("171b.in", "r", stdin);
	freopen("171b.out", "w", stdout);
	int tt; cin>>tt;
	for(int i=1;i<=tt; ++i)  {
		string in; cin>>in;
		vector<int> v;
		v.reserve(in.size());
		transform(begin(in), end(in), back_inserter(v), [](char c) {return c - '0';});
		while(!zero(v)) {
			vector<int> vv = v;
			sort(vv.begin(), vv.end());
			if(equ(v, vv) ) {
				break;
			}
			sub(v);
		}
		printf("Case #%d: ", i);
		for(auto const& i:v) if(i!=0) cout << i;
		cout<<endl;
		fflush(stdout);
	}
}