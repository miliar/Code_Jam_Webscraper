#include<bits/stdc++.h>

using namespace std;

string s;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("a.txt","w",stdout);
	
	int t;
	
	cin >> t;
	
	for(int tt=0;tt<t;tt++)
	{
		cin >> s;
		
		for(int i=0;i<s.size()-1;i++)
			if(s[i]>s[i+1])
			{
				for(int j=i-1;;j--)
					if(j==-1 || s[j]!=s[i])
					{
						s[j+1]--;
						i=j+1;
						break;
					}
				
				for(int j=i+1;j<s.size();j++)
					s[j]=57;
					
				break;
			}
			
		cout << "Case #" << tt+1 << ": ";
		
		int flag=0;
		
		for(int i=0;i<s.size();i++)
			if(!flag && s[i]!='0')
			{
				flag=1;
				cout << s[i];
			}
			else if(flag)
				cout << s[i];
				
		cout << endl;
	}
	
	return 0;
}
