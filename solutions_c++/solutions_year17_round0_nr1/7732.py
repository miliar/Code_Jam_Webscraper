#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("inputlarge.txt","r",stdin);
	freopen("outputlarge.txt","w",stdout);
	int t;
	cin >> t;
	int count=1;
	while(count<=t)
	{
		cout << "Case #" << count << ": ";
		string s;
		cin >> s;
		int k;
		cin >> k;
		int len=s.size();
		int cnt=0;
		for(int i=0;i<=len-k;i++)
		{
			if(s[i]=='+')
				continue;
			else
			{
				cnt++;
				for(int j=i;j<i+k;j++)
				{
					if(s[j]=='+')
						s[j]='-';
					else if(s[j]=='-')
						s[j]='+';
				}
			}
		}
		bool flag=false;
		for(int i=0;i<len;i++)
		{
			if(s[i]=='-')
			{
				flag=true;
				break;
			}
		}
		if(flag==true)
			cout << "IMPOSSIBLE\n";
		else
			cout << cnt << "\n";
		cerr << "Test Case " << count << " Solved in " << double(clock())/double(CLOCKS_PER_SEC) << endl;
		count++;
	}
	return 0;
}