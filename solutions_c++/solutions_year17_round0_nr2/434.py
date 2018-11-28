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
	repeq(t,1,T)
	{
		ll N;
		cin >> N;
		int di[30];
		int i = 0;
		for(ll n=N; n>0 ;++i, n/=10)
			di[i] = n%10;
	    for(int j=i-2;j>=0;--j)
			if(di[j]<di[j+1])
			{
				++j;
				while(j+1<i && di[j+1]==di[j])
					++j;
				--di[j];
				--j;
				while(j>=0)
				{
					di[j]=9;
					--j;
				}
			}
		ll m=0;
		for(int j=i-1;j>=0;--j)
			m*=10, m+=di[j];
				
		cout << "Case #" << t << ": " << m << endl;
	}
	
	return 0;
}
