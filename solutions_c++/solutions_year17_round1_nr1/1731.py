#include<bits/stdc++.h>

using namespace std;

string s[105];

int r,c;

void dfs(int x,int y)
{
	
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
		{
			x=i;
			y=j;
		if(s[x][y]!='?')
	{
		for(int j=y-1;j>=0;j--)
			if(s[x][j]=='?')
				s[x][j]=s[x][y];
			else
				break;
				
		for(int j=y+1;j<c;j++)
			if(s[x][j]=='?')
				s[x][j]=s[x][y];
			else
				break;
	}	
	}
}
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.txt","w",stdout);
	
	int t;
	
	cin >> t;
	
	for(int tt=0;tt<t;tt++)
	{
		cin >> r >> c;
		
		for(int i=0;i<r;i++)
			cin >> s[i];
			
		dfs(0,0);
	
	cout << "Case #" << tt+1 << ":" << endl;
	
	for(int i=0;i<r;i++)
	{
		//cout << s[i][0] << endl;
		if(s[i][0]=='?')
		{
			if(i)
			{
				s[i]=s[i-1];
				cout << s[i] << endl;
			}
			else
			{
				for(int j=i+1;j<r;j++)
					if(s[j][0]!='?')
					{
						s[0]=s[j];
						break;
					}
					
				cout << s[0] << endl;
			}
		}
		else
			cout << s[i] << endl;
	}
	}
	
	return 0;
}
