#include <bits/stdc++.h>
using namespace std;

int T;
double P[51];

double espo(float a, int b) {
	if (b==0) return 1;
	return a*espo(a, b-1);
}

int main() {
	cin>>T;
	for (int t=0; t<T; t++) {
		int N, K;
		double U;
		cin>>N>>K>>U;
		for(int i=0; i<N; ++i) cin>>P[i];
		int j=1;
		double m, d;
		if (N==K) {
			sort(P, P+N);
			P[N]=1;
			m=P[0];
			while(U>0.00000001 && j<=N) {
				d = P[j] - m;
				//~ cout<<"d="<<d<<"\n";
				if (U/j > d) {
					U -= (double)(j)*d;
					m=P[j];
					++j;
				}
				else {
					m += U/j;
					break;
				}
			}
		}
		//~ cout<<"m= "<<m<<"\n";
		double ans=espo(m,j);
		for(int i=j; i<N; ++i) ans*=P[i];
		cout<<"Case #"<<t+1<<": "<< ans <<"\n";
	}
	return 0;
}
