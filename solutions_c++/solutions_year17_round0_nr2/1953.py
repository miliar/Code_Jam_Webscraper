#include <bits/stdc++.h>

#define icin(x) scanf("%d",&x)
#define lcin(x) scanf("%lld",&x)
#define pb push_back
#define LL long long
#define F first
#define S second
#define VPI vector< pair<int,int> >
#define VVI vector< vector<int> > 
#define BC(x) __builtin_popcount(x)

using namespace std;

int main()
{
	int t;
	icin(t);
	for(int tc=1; tc<=t; tc++)
	{
		LL n;
		LL ans = 0;
		cin >> n;
		vector< int > ar;
		LL temp = n;
		while(temp != 0)
		{
			ar.pb(temp%10);
			temp /= 10;
		}		
		int cur = -1;
		for(int i=1; i<ar.size(); i++)
		{
			if(ar[i] > ar[i-1])
				cur = i-1;
		}
		if(cur == -1)
			ans = n;
		else
		{
			bool tight = false;
			for(int i=0; i<=cur; i++)
				ar[i] = 9;
			for(int i=cur+1; i<ar.size(); i++)
			{
				if(tight == true)
					break;
				if(i == ar.size() - 1)
				 	ar[i]--;
				 else
				 {
				 	if(ar[i] > ar[i+1])
				 	{
				 		ar[i]--;
				 		tight = true;
				 	}
				 	else
				 		ar[i] = 9;
				 }
			}
			for(int i = ar.size() - 1 ;i >=0; i--)
			{
				ans = 10*ans + ar[i];
			}
		}
		printf("Case #%d: %lld\n",tc,ans);
	}
	return 0;
}