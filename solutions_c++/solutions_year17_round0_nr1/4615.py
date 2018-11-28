#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;
int T; string s; int K; bool ar[1005];
int main() {
    ifstream cin("cjam2017in.txt");
    ofstream cout("cjam2017out.txt");
	cin>>T;
	for (int t=1; t<=T; t++) {
		cin>>s>>K;
		memset (ar, 0, sizeof ar);
		int S = s.size();
		for (int i=0; i<S; i++) {
			ar[i]=s[i]=='+'?1:0;
		}
		int n=0;
		for (int i=0; i<=S-K; i++) {

			if (!ar[i]) {
				n++;
				for (int j=i; j<i+K; j++)
					ar[j]^=1;
			}
		}
		bool suc=1;
		for (int i=0; i<S; i++)
			if (ar[i]==0) {suc=0; break;}
		if (suc) cout<<"Case #"<<t<<": "<<n<<"\n";
		else cout<<"Case #"<<t<<": IMPOSSIBLE\n";
	}
}
