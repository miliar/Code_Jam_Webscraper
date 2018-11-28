#include <bits/stdc++.h>
using namespace std;

#define maxsiz 1000000
#define mod 1000000007
#define F first
#define S second
#define si(a) scanf("%d",&a)
#define sl(a) scanf("%llu",&a)
#define pi(a) printf("%d",a)
#define pl(a) printf("%llu",a)
#define fr(i,k,n) for(int i = k ; i < n ; i++ )
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define printvect(a,n) fr(i,0,n) cout << fixed << a[i] << " " ;
typedef unsigned long long int ull;

bool myfunction (int i,int j) { return (i>j); }

int main()
{
	ull test;
	cin >> test;
	fr(t,0,test)
	{	
		int n,k,ls,rs;
		cin >> n >> k ;

		vector<int> q;
		q.pb(n);
		for(int i=0 ;i < k;i++)
		{
			sort(q.begin(),q.end(),myfunction);
			
			int ele = q[0]; //Largest element
			
			q.pb(ele/2);
			rs = ele/2;
			// cout << ele/2 << " ";
			if(ele%2==0)
			{
				ls = ele/2-1;
				q.pb(ele/2-1);
				// cout << ele/2 -1<< endl;
			}
			else
			{
				ls = ele/2 ;
				q.pb(ele/2);
				// cout << ele/2 << endl;
			}
			q.erase(q.begin());
		}
		cout << "Case #" << t+1 << ": " <<  max(0,max(ls,rs)) << " " << max(0,min(ls,rs)) << endl ;
	}
	return 0;
}