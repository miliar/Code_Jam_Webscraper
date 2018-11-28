#include <iostream>
#include <cstring>
#include <cmath>
#include <fstream>
using namespace std;
int T, N, P, R[52], A[52][52];
int work[52];
double L[52], H[52];
double NL[52], NH[52];
int main() {
    ifstream cin("s2in.txt");
    ofstream cout("s2out.txt");
	cin>>T;
	for (int t=1; t<=T; t++) {
		cin>>N>>P;
		memset(R, 0, sizeof R);
		memset(L, 0, sizeof L);
		memset(H, 0, sizeof H);
		for (int i=0; i<52; i++) memset(A[i], 0, sizeof A[i]);
		for (int i=0; i<N; i++) {
			cin>>R[i];
			L[i]=0.9*R[i];
			H[i]=1.1*R[i];
		}
		for (int i=0; i<N; i++) {
			for (int j=0; j<P; j++) {
				cin>>A[i][j];
			}
		}
		int ans=0;
		for (int i=1; i<1111111; i++) {
			if (ans>=P) break;
			bool b=0;
			for (int j=0; j<N; j++) {
				NL[j]=i*L[j];
				NH[j]=i*H[j];
				if (NL[j]>1111111) {b=1; break;}
			}
			if (b) break;
			for (int j=0; j<N; j++) {
				work[j]=-1;
			}
			while (1) {
				if (ans>=P) break;
				for (int j=0; j<N; j++) {
					for (int k=0; k<P; k++) {
						if (NL[j]<=A[j][k]&&A[j][k]<=NH[j]) {
							work[j]=k;
						}
					}
					if (work[j]==-1) b=1;
				}
				if (b) break;
				else {
					for (int j=0; j<N; j++) {
						A[j][work[j]]=-1;
						work[j]=-1;
					}
					ans++;
				}
			}
		}
		cout<<"Case #"<<t<<": "<<ans<<"\n";
		printf("Case #%d: %d\n", t, ans);
	}
}
