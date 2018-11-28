#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <list>
#include <map>
#include <deque>
#include <string>

using namespace std;

int t,T;

#define ULL unsigned long long

void runtestcase()
{	
	ULL N, Q;
	cin >> N >> Q;
	vector<ULL> E(N+1), S(N+1);
	for (ULL n=1; n<=N; n++)
	{
		cin >> E[n] >> S[n];
	}
	ULL D[101][101];
	for (ULL i=1; i<=N; i++)
		for (ULL j=1; j<=N; j++)
			cin >> D[i][j];
	vector<ULL> U(Q), V(Q);
	for (ULL k=0; k<Q; k++)
		cin >> U[k] >> V[k];

	// small dataset
	vector<double> r(N+1, 0);
	for (ULL n=N-1; n>=1; n--)
	{
		double d = 0;
		double mint;
		for (ULL m=n+1; m<=N; m++)
		{
			d += D[m-1][m];
			if (d > E[n])
				break;
			double t = d/double(S[n]) + r[m];
			if  (m == n+1 || t < mint)
				mint = t;
		}
		r[n] = mint;
	}
	printf("%.9f", r[1]);
}

void main()
{	
	cin >> T;
	for (t = 1; t <= T; t++)
	{
		cerr << t;
		cout << "Case #" << t << ": ";
		runtestcase();
		cout << endl;
	}	
}