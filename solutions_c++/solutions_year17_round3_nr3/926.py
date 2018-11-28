#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define make0(a) memset(a,0,sizeof(a))
#define make1(a) memset(a,-1,sizeof(a))
#define all(v) begin(v),end(v)
#define pi pair <int,int>
#define fast_cin() ios_base::sync_with_stdio(0) 

const int mod = 1e9+7;

int main()
{
	int T;
	cin >> T;
	for(int f=1;f<=T;f++)
	{
		cerr << f << endl;
		int N,K;
		cin >> N >> K;
		long double A[N];
		long double X;
		cin >> X;
		priority_queue <long double, vector <long double>, greater<long double> > pq;
		for(int i=0;i<N;i++)
		{
			cin >> A[i];
			pq.push(A[i]);
		}
		int num = X*500000;
		while(num and !pq.empty())
		{
			num --;
			// printf("%lf\n",pq.top());
			long double p = pq.top();
			pq.pop();
			p += 0.000002;
			pq.push(p);
		}
		long double ans = 1;
		while(!pq.empty())
		{
			long double p = pq.top();
			pq.pop();
			// printf("%lf\n",p);
			ans *= (p);
		}
		// cout << ans << endl;
		assert(ans <= 1.00001);
		if(ans >= 1)
			ans = 1;
		// ans = 1 - ans;
		printf("Case #%d: %.6Lf\n",f,ans);
	}	
	return 0;
}