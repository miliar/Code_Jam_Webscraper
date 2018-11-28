#include "iostream"
#include "vector"
#include "string"
#include "algorithm"
#include "string.h"
#include "stdio.h"
#include "map"

using namespace std;

int main() {
	int T;
	cin>>T;
	for(int tc=0;tc<T;tc++) {
		map<long long, long long> g;
		int n,k;
		cin>>n>>k;
		g[-n]=1;
		while(1) {
			int x=-(g.begin()->first);
			int c=g.begin()->second;
			//cout<<"# "<<x<<" "<<c<<" "<<k<<endl;
			if(k<=c) break;
			k-=c;
			g.erase(-x);
			x--;
			g[-(x/2)]+=c;
			g[-(x-x/2)]+=c;
		}
		int s=-(g.begin()->first)-1;
		cout<<"Case #"<<tc+1<<": "<<s-s/2<<" "<<s/2<<endl;
	}
	return 0;
}