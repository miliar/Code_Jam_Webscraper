#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int t, T, i, j, R, C;
	
	cin>>T;
	
	for(t = 1; t <= T; t++)
	{
		vector<vector<char> > cake;
		char last = '?', done;
		
		cin>>R>>C;
		cout<<"Case #"<<t<<": "<<endl;
		
		cake.resize(R);
		
		for(i = 0; i < R; i++)
		{
			cake[i].resize(C);
			
			for(j = 0; j < C; j++)
			{
				cin>>cake[i][j];
			}
		}
		
		for(i = 0; i < R; i++)
		{
			last = '?';
			for(j = 0; j < C; j++)
			{
				if(cake[i][j] != '?')
					last = cake[i][j];
				else
				{
					cake[i][j] = last;
					
					if(last == '?')
					{
						for(int s = j - 1; s >= 0; s--)
						{
							cake[i][s] = last;
						}
					}
				}
			}
			
			for(j = C - 1; j >= 0; j--)
			{
				if(cake[i][j] != '?')
					last = cake[i][j];
				else
				{
					cake[i][j] = last;
					
					if(last == '?')
					{
						for(int s = j - 1; s >= 0; s--)
						{
							cake[i][s] = last;
						}
					}
				}
			}
			
			if(last == '?')
			{
				if(i > 0 && !cake[i-1].empty())
				{
					cake[i] = cake[i-1];
				}
				else
				{
					cake[i].resize(0);
				}
			}
		}
		
		for(i = 0; i < R; i++)
		{
			if(!cake[i].empty())
			{
				for(j = i - 1; j >= 0; j--)
				{
					cake[j] = cake[i];
				}
				
				break;
			}
		}
		
		
		for(i = 0; i < R; i++)
		{
			for(j = 0; j < C; j++)
			{
				cout<<cake[i][j];
			}
			cout<<endl;
		}
	}
	
	return 0;
}
