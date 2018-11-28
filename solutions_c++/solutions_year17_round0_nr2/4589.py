#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;
int T; string s; int d[20], ans[20];
int main() {
    ifstream cin("cjam2017p2in.txt");
    ofstream cout("cjam2017p2out.txt");
	cin>>T;
	for (int t=1; t<=T; t++) {
		cin>>s;
		int S=s.size();
		for (int i=0; i<S; i++) {
			d[i]=s[i]-'0';
		}
		memset(ans, 0, sizeof ans);
		bool b=0;
		for (int i=0; i<S; i++) {
			if (i<S-1&&d[i]>d[i+1]) {
				for (int j=i+1; j<S; j++) ans[j]=9;
				while (i>=0) {
					ans[i]=d[i]-1;
					if (i==0||ans[i]>=ans[i-1]) break;
					ans[i]=9;
					i--;
				}
				b=1;
			} else {
				ans[i]=d[i];
			}
			if (b) break;
		}
		b=0;
		cout<<"Case #"<<t<<": ";
		for (int i=0; i<S; i++) {
			if (ans[i]!=0) b=1;
			if (b) cout<<ans[i];
		}
		cout<<"\n";
	}
}
