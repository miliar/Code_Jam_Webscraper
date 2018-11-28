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

#define PI 3.141592653

struct cylinder {
	double R,H;
	double SA;
	double area;
	int idx;
};

bool compare(cylinder a, cylinder b)
{
	return a.SA > b.SA;
}

int main()
{
	int T;
	cin >> T;
	for(int f=1;f<=T;f++)
	{
		int N,K;
		cin >> N >> K;
		struct cylinder A[N],copy[N];
		for(int i=0;i<N;i++)
			cin >> A[i].R >> A[i].H;
		for(int i=0;i<N;i++)
		{
			A[i].SA = A[i].R*2*PI*A[i].H;
			A[i].idx = i;
			A[i].area = A[i].R*A[i].R*PI;
		}
		for(int i=0;i<N;i++)
		{
			copy[i].R = A[i].R;
			copy[i].H = A[i].H;
			copy[i].SA = A[i].SA;
			copy[i].idx = A[i].idx;
			copy[i].area = A[i].area;
		}
		double ans=0;
		double mans=0;
		for(int i=0;i<N;i++)
		{
			ans = A[i].SA + A[i].area;
			int ct=1;
			sort(copy,copy+N,compare);
			// cout << ans << endl;
			for(int j=0;j<N;j++)
			{
				if(ct == K)
					break;
				// cout << ans << endl;
				// cout << A[i].idx << ' ' << copy[j].idx << ' ' <<  A[i].R << ' ' << copy[j].R << endl;
				if(A[i].idx == copy[j].idx)
					continue;
				if(A[i].R < copy[j].R)
					continue;
				ans += copy[j].SA;
				ct++;
			}
			// cout << ct << endl;
			mans = max(ans,mans);
		}
		printf("Case #%d: %.6lf\n",f,mans);
	}	
	return 0;
}