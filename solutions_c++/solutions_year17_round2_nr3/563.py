#include <iostream>
#include <fstream>
#include <iomanip>
#define DN 1005
#define LL long long
using namespace std;

int T,n,q,td[DN],sp[DN];
LL dm[DN][DN];
double rz[DN][DN];

void cdm() {
	for(int i=1; i<=n; i++) for(int j=1; j<=n; j++) for(int k=1; k<=n; k++)
        if (j==k) dm[j][k]=0;
        else dm[j][k]=min(dm[j][k],dm[j][i]+dm[i][k]);
}

void crz() {
	for(int _=1; _<=n; ++_)
	for(int i=1; i<=n; i++) for(int j=1; j<=n; j++) for(int k=1; k<=n; k++)
        if (j==k) dm[j][k]=0;
    	else if(dm[j][i]<=td[j]) {
    		rz[j][k]=min(rz[j][k],(double)dm[j][i]/sp[j]+rz[i][k]);
    	}
}

int main() {
	ifstream f("c.txt");
	ofstream g("c.out");
	f>>T;
	for(int t=1; t<=T; ++t) {
		cerr<<t<<'\n';
		f>>n>>q;
		for(int i=1; i<=n; ++i) f>>td[i]>>sp[i];
		for(int i=1; i<=n; ++i)
			for(int j=1; j<=n; ++j) {
				f>>dm[i][j];
				if(dm[i][j]==-1) dm[i][j]=(1LL<<60);
			}
		cdm();
		for(int i=1; i<=n; ++i) for(int j=1; j<=n; ++j)
			if(dm[i][j]<=td[i])
				rz[i][j]=(double)dm[i][j]/sp[i];
			else rz[i][j]=1e18;
		crz();
		// for(int i=1; i<=n; ++i) {
		// 	for(int j=1; j<=n; ++j) {
		// 		cout<<rz[i][j]<<' ';
		// 	}
		// 	cout<<'\n';
		// }

		g<<"Case #"<<t<<": ";
		while(q--) {
			int a,b; f>>a>>b;
			g<<fixed<<setprecision(9)<<rz[a][b]<<' ';
		}
		g<<'\n';
	}
}