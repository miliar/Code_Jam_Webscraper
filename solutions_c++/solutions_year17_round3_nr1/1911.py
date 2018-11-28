#include <bits/stdc++.h>
using namespace std;
typedef pair <double,double> pi;

const int MAX=1010;
pi A[MAX];
multiset <double> S;
double mpi=2*acos(0);

int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		S.clear();
		int n,k;
		double res=0;
		scanf("%d %d",&n,&k);
		for(int i=0;i<n;i++){
			scanf("%lf %lf",&A[i].first,&A[i].second);
		}
		sort(A,A+n);
		for(int i=0;i<n;i++){
			double sum=A[i].first*A[i].first+A[i].first*A[i].second*2;
			int q=k-1;
			auto it =S.end();
			while(q-- && it!=S.begin()){
				it--;
				sum+=*it;
			}
			S.insert(A[i].first*A[i].second*2);
			res=max(res,sum);
		}
		printf("Case #%d: %f\n",t,res*mpi);
	}
}