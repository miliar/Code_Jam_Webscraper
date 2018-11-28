#include <cstdio>
#include <vector>
#include <algorithm>
#include <utility>

#define mp make_pair
#define pb push_back

using namespace std;

typedef long long LL;

const long double pi = 3.14159265358;
int n,K;
vector <int> V;

LL A[1111],H[1111];

bool comp(int ca,int cb)
{
	return H[ca] < H[cb];
}

long double TC()
{
	int i,j;
	LL k, ret=0;

	scanf("%d%d",&n,&K);

	for(i=0;i<n;i++){
		scanf("%lld%lld",A+i,H+i);
		H[i] *= A[i] * 2;
	}

	for(i=0;i<n;i++){
		V.clear();
		for(j=0;j<n;j++){
			if(A[i] >= A[j] && i!=j) V.push_back(j);
		}
		sort(V.begin(),V.end(),comp);

		if(V.size() < K-1) continue;

		k = A[i] * A[i] + H[i];
		for(j=K;j>1;j--){
			k += H[V.back()];
			V.pop_back();
		}
		if(k>ret) ret=k;
	}

	return ret*pi;
}

int main()
{
	freopen("output.txt","w",stdout);

	int t,i;

	scanf("%d",&t);

	for(i=1;i<=t;i++){
		printf("Case #%d: %.9Lf\n",i,TC());
	}

	return 0;
}