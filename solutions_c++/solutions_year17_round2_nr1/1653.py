#include <bits/stdc++.h>
using namespace std;
int main(int argc, char *argv[])
{
	int T;
	while(cin>>T){
		for(int Case = 1; Case<=T; Case++){
			double D, N, k[1000], d[1000];
			cin>>D>>N;
			for(int i=0; i<N; i++){
				cin>>k[i]>>d[i];
			}
			double x = (D-k[0])/d[0], y = D/x;
			for(int i=0; i<N; i++){
				double tmp = (D-k[i])/d[i];
				if(tmp > x){
					x = tmp;
					y = D/x;
				}
			}
			printf("Case #%d: %.6lf\n", Case, y);
		}
	}
    return 0;
}
