#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void flip(int j, int s, string &in) {
	while(s>0) {
		if(in[j]=='+') in[j]='-';
		else in[j]='+';
		++j; --s;
	}
}

int main() {
	freopen("171a.in.txt", "r", stdin);
	freopen("171a.out.txt", "w", stdout);
	int tt; cin>>tt;
	for(int i=1;i<=tt; ++i)  {
		int s, c=0;
		bool imp=false;
		string in;
		cin>>in>>s;
		for(int j=0;j<in.size();++j) {
			if(in[j]=='-') {
				// cout<<in.size()<<endl;
				if(s>in.size()-j) {
					imp=true;
					break;
				} 
				flip(j, s, in);
				++c;
			}
		}
		if(imp) printf("Case #%d: IMPOSSIBLE\n", i);
		else printf("Case #%d: %d\n", i,c);
		fflush(stdout);
	}
}