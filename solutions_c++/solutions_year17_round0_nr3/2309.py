#include<bits/stdc++.h>

using namespace std;

string s;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("a.txt","w",stdout);
	
	int t;
	
	cin >> t;
	
	for(int tt=0;tt<t;tt++)
	{
		long long n,ans,k;
		
		cin >> n >> k;
		
		long long var1=n,var2,cnt1=1,cnt2=0;
		
		while(var1)
		{
			if(k<=cnt1)
			{
				ans=var1;
				break;
			}
			else if(k<=cnt1+cnt2)
			{
				ans=var2;
				break;
			}
			
			k-=(cnt1+cnt2);
			
			if(var1&1)
			{
				var1/=2;
				
				if(var2)
				{
					var2/=2;
					var2--;
				}
				
				cnt1=2*cnt1+cnt2;
			}
			else
			{
				var1/=2;
				var2=var1;
				var2--;
				
				cnt2=2*cnt2+cnt1;
			}	
		//	cout << var1 << " " << cnt1 << endl;	
		}
		
		//cout << ans << endl;		
			
		cout << "Case #" << tt+1 << ": " << ans/2 << " " << (ans-1)/2 << endl;
	}
	
	return 0;
}
