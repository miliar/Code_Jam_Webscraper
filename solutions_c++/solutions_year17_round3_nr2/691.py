#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>

using namespace std;

#define INF 1000000000
#define ll long long
#define endl '\n'

struct Interval
{
	int p;
	int L,R;
	int len(){return R-L;};
	Interval(){};
	Interval(int l, int r, int _p){ L=l; R=r; p=_p;};
};
inline bool operator < (const Interval &A, const Interval &B) { return A.L < B.L; }


#define PA 0
#define PB 1
	
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	int T;
	cin >> T;
	for(int t=1; t<=T; t++)
	{
		vector<Interval> interval;
	
		int N;
		int n,m;
		cin >> n >> m;
		N = n+m;
		
		int L,R;
		for(int i=0; i<n; i++)
		{
			cin >> L >> R;
			interval.push_back(Interval(L,R,PA));
		}
		for(int i=0; i<m; i++)
		{
			cin >> L >> R;
			interval.push_back(Interval(L,R,PB));
		}
		
		sort(interval.begin(), interval.end());
		
		
		int ans = 0;
		for(int i=0; i<N; i++)
		{
			int j = (i+1)%N;
			if(interval[i].p != interval[j].p)
				ans++;
		}
		
//		cout << "ans_0 = " << ans <<endl;
		
		int A_inter = 0;
		int B_inter = 0;
		int free_inter = 1440-A_inter-B_inter;
		// sum static
		for(int i=0; i<N; i++)
		{
			if(interval[i].p == PA)
				A_inter += interval[i].len();
			else
				B_inter += interval[i].len();
		}
		// sum linked
		for(int i=1; i<N; i++)
		{
			if(interval[i-1].p == interval[i].p)
			{
				if(interval[i].p == PA)
					A_inter += interval[i].L-interval[i-1].R;
				else
					B_inter += interval[i].L-interval[i-1].R;
			}
		}
		if(interval[0].p==interval[N-1].p)
		{
			if(interval[0].p==PA)
				A_inter += (1440-interval[N-1].R) + interval[0].L;
			else
				B_inter += (1440-interval[N-1].R) + interval[0].L;
		}
		
//		cout << "A_inter = " << A_inter << endl;
//		cout << "B_inter = " << B_inter << endl;
		
		// Manage
		if( A_inter>720 || B_inter>720 )
		{
			int dec,inc;
			int over;
			if(A_inter>720)
				dec=PA, inc=PB, over = A_inter-720;
			else// B>720
				dec=PB, inc=PA, over = B_inter-720;
			
			
			vector<int> dec_space;
			for(int i=1; i<N; i++)
			{
				if(interval[i].p==dec && interval[i].p == interval[i-1].p)
					dec_space.push_back( interval[i].L-interval[i-1].R );
			}
			if(interval[0].p==dec && interval[0].p == interval[N-1].p)
				dec_space.push_back( 1440-interval[N-1].R + interval[0].L );
		
		
			sort(dec_space.begin(), dec_space.end(), greater<int>());
			
			
			for(int i=0; i<dec_space.size(); i++)
			{
//				cout << "dec : " << dec_space[i] <<endl;
				over -= dec_space[i];
				ans += 2;
				if(over <= 0)
					break;
			}
		}
		
		
		cout << "Case #" << t << ": " << ans << endl;
//		cout <<endl;
	}
	
	return 0;
}


