#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
int main()
{
	ios::sync_with_stdio(0);
	int T;
	cin>>T;
	for (int t = 1; t <= T; ++t)
	{
		int N, K;
		cin>>N>>K;
		long long R[N], H[N];
		for (int i = 0; i < N; ++i)
		{
			cin>>R[i]>>H[i];
		}
		pair<long long, long long> C[N], A[N];
		for (int i = 0; i < N; ++i)
		 {
		 	A[i].first = R[i]*R[i];
		 	A[i].second = i;
		 	C[i].first = 2*R[i]*H[i];
		 	C[i].second = i;
		 } 
		 sort(A, A+N, greater<pair<long long, long long>>());
		 sort(C, C+N, greater<pair<long long, long long>>());
		 long long ans = 0, temp = 0;
		 for (int i = 0; i < N; ++i)
		 {
		 	temp = A[i].first;
		 	int index = A[i].second;
		 	temp += 2*R[index]*H[index];
		 	int count = 1, pos = 0;
		 	while (count < K)
		 	{
		 		if (C[pos].second == index)
		 		{
		 			++pos;
		 			continue;
		 		}
		 		temp += C[pos].first;
		 		++count;
		 		++pos;
		 	}
		 	ans = max(ans, temp);
		 }
		 long double ansx = M_PI * ans;
		cout<<"Case #"<<t<<": "<<fixed<<setprecision(9)<<ansx<<'\n';
	}
}