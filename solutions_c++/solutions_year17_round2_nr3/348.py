#include <bits/stdc++.h>
#define f(a, n) for (int a=0; a<n; a++)
#define F(a, n) for (int a=1; a<=n; a++)
using namespace std;
int Q, n, T;
long long D0[105][105];
double D1[105][105];
long long E[105];
double S[105];
int x, y;
int main(){
	cin.tie(NULL);
	ios::sync_with_stdio(0);
	ifstream inp;
	ofstream oup;
	inp.open("c.in");
	oup.open("c.out");
	oup<<setprecision(9)<<fixed;
	inp>>T;
	
	F(t, T){
		oup<<"Case #"<<t<<": ";
		inp>>n>>Q;
		f(i, n) D0[i][i]=0;
		f(i, n) inp>>E[i]>>S[i];
		f(i, n) f(j, n) {
			inp>>D0[i][j];
			if (D0[i][j]==-1) D0[i][j]=INT_MAX;
			D1[i][j]=1e18;
		}
		f(k, n) f(i, n) f(j, n){
			D0[i][j] = min(D0[i][j], D0[i][k]+D0[k][j]);
		}
		f(i, n) f(j, n) if (D0[i][j]<=E[i]) {
			D1[i][j] = D0[i][j]/S[i];
		}
		f(k, n) f(i, n) f(j, n){
			D1[i][j] = min(D1[i][j], D1[i][k]+D1[k][j]);
		}
		f(q, Q){
			inp>>x>>y;
			oup<<D1[x-1][y-1]<<" ";
		}
		oup<<endl;
	}
}

