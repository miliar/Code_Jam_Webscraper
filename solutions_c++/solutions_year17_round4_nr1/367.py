#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
#define F first
#define S second

const int lim=100;
int gc[5];
int ans3[101][101];
int ans4[101][101][101];

void precomp() {
	for (int i=0;i<=lim;i++) {
		for (int j=0;j<=lim;j++) {
			ans3[i][j]=1;
			for (int k=0;k<=lim;k++) ans4[i][j][k]=1;
		}
	}
	ans3[0][0]=0;
	ans4[0][0][0]=0;
	for (int i=0;i<=lim;i++) {
		for (int j=0;j<=lim;j++) {
			if (i+1<=lim && j+1<=lim) {
				ans3[i+1][j+1]=max(ans3[i][j]+1,ans3[i+1][j+1]);
			}
			if (i+3<=lim) {
				ans3[i+3][j]=max(ans3[i][j]+1,ans3[i+3][j]);
			}
			if (j+3<=lim) {
				ans3[i][j+3]=max(ans3[i][j]+1,ans3[i][j+3]);
			}
		}
	}
	for (int i=0;i<=lim;i++) {
		for (int j=0;j<=lim;j++) {
			for (int k=0;k<=lim;k++) {
				if (i+4<=lim) {
					ans4[i+4][j][k]=max(ans4[i][j][k]+1,ans4[i+4][j][k]);
				}
				if (j+2<=lim) {
					ans4[i][j+2][k]=max(ans4[i][j][k]+1,ans4[i][j+2][k]);
				}
				if (k+4<=lim) {
					ans4[i][j][k+4]=max(ans4[i][j][k]+1,ans4[i][j][k+4]);
				}
				if (i+2<=lim && j+1<=lim) {
					ans4[i+2][j+1][k]=max(ans4[i][j][k]+1,ans4[i+2][j+1][k]);
				}
				if (j+1<=lim && k+2<=lim) {
					ans4[i][j+1][k+2]=max(ans4[i][j][k]+1,ans4[i][j+1][k+2]);
				}
				if (i+1<=lim && k+1<=lim) {
					ans4[i+1][j][k+1]=max(ans4[i][j][k]+1,ans4[i+1][j][k+1]);
				}
			}
		}
	}
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	precomp();
	int tcs;
	cin>>tcs;
	for (int tc=1;tc<=tcs;tc++) {
		int n,p;
		cin>>n>>p;
		for (int i=0;i<p;i++) gc[i]=0;
		for (int i=0;i<n;i++) {
			int g;
			cin>>g;
			gc[g%p]++;
		}
		cout<<"Case #"<<tc<<": ";
		if (p==2) cout<<gc[0]+(gc[1]+1)/2;
		else if (p==3) cout<<gc[0]+ans3[gc[1]][gc[2]];
		else if (p==4) cout<<gc[0]+ans4[gc[1]][gc[2]][gc[3]];
		cout<<"\n";
	}
}
