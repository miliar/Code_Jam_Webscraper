#include <iostream>
#include <fstream>
#include <string>
#include <map>
#define x first
#define y second
#define LL long long
using namespace std;

map<LL, LL> fr;
LL T,n,k;

int main() {
	ifstream f("c.txt");
	ofstream g("c.out");
	f>>T;
	for(int t=1; t<=T; ++t) {
		g<<"Case #"<<t<<": ";
		f>>n>>k;
		fr[-n]=1;
		while(true) {
			pair<LL, LL> _=*fr.begin();
			_.x=-_.x;
			//cout<<_.x<<' '<<_.y<<'\n';
			fr.erase(fr.begin());
			LL a=(_.x-1)/2,b=_.x/2;
			if(k>_.y) {
				k-=_.y;
				fr[-a]+=_.y;
				fr[-b]+=_.y;
			}else {
				g<<b<<' '<<a;
				break;
			}
		}
		fr.clear();
		g<<'\n';
	}
}