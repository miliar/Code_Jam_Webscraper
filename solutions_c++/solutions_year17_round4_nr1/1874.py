#include <bits/stdc++.h>
using namespace std;
#define rep(a,b,c) for(int a=b;a<c;++a)
#define repeq(a,b,c) for(int a=b;a<=c;++a)
#define debug(x) cerr<<(#x)<<": "<<x<<endl
typedef long long ll;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int T;
	cin >> T;
	repeq(testcase,1,T)
	{
		int N, P;
		cin >> N >> P;
	    int g;
		int count[5];
		rep(i,0,P)
			count[i]=0;
		rep(i,0,N)
		{
			cin >> g;
			count[g%P]++;
		}
		// rep(i,0,P)
		// 	cout << count[i] << " ";
		// cout << endl;
		int ans;
		if(P==2)
		{
			ans = count[0]+(count[1]+1)/2;
		}
		else if(P==3)
		{
			ans = count[0];
			int a = min(count[1],count[2]), b=max(count[1],count[2]);
			ans += a + (b-a+2)/3;
		}
		
		printf("Case #%d: %d\n",testcase,ans);
	}
}
