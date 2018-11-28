#include<bits/stdc++.h>

using namespace std;

string s;
int a[2005];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.txt","w",stdout);
	
	int t;
	
	cin >> t;
	
	for(int tt=0;tt<t;tt++)
	{
		int cnt=0,k,ans=0,flag=0;
		
		cin >> s >> k;
		
		for(int i=0;i<s.size();i++)
			a[i]=0;
		
		for(int i=0;i<s.size();i++)
		{
			cnt-=a[i];
			
			if((s[i]=='-' && !(cnt&1)) || (s[i]=='+' && cnt&1))
			{
				if(i+k>s.size())
				{
					flag=1;
					break;
				}
				
				cnt++;
				a[i+k]++;
				ans++;
			}
		}
		
		cout << "Case #" << tt+1 << ": ";
		
		if(flag)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << ans << endl;
	}
	
	return 0;
}
