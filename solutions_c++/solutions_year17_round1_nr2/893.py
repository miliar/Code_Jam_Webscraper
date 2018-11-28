#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int>vi;
typedef pair<int,int>ii;
double A[55];
int B[55][55][2];
int main(){
	int test;
	cin>>test;
	for(int te=1;te<=test;te++){
		int n,m;
		double x;
		cin>>n>>m;
		for(int i=0;i<n;i++)
			cin>>A[i];
		int b=0;
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				cin>>x;
				B[i][j][0]=ceil(x/(1.1*A[i]));
				B[i][j][1]=floor(x/(0.9*A[i]));
				if(B[i][j][0]>B[i][j][1])B[i][j][0]=B[i][j][1]=-1;
				b=max(b,B[i][j][1]);
				//cout<<B[i][j][0]<<" - "<<B[i][j][1]<<"  ;  ";
			}//cout<<endl;
		}//cout<<endl;
		int r=0;
		for(int k=1;k<=b;){
			vector<int>P(n,-1);
			for(int i=0;i<n;i++){
				for(int j=0;j<m;j++){
					if(k>=B[i][j][0] and k<=B[i][j][1]){
						if(P[i]==-1)P[i]=j;
						else {
							if(B[i][j][1]<=B[i][P[i]][1])
								P[i]=j;
						}

					}
				}
			}
			bool sw=1;
			for(int i=0;i<n;i++){
				if(P[i]==-1)sw=0;
			}
			if(sw){
				for(int i=0;i<n;i++)					
					B[i][P[i]][0]=B[i][P[i]][1]=-1;
				r++;
			}else k++;
		}
		printf("Case #%d: %d\n",te,r );
	}	
	return 0;
}