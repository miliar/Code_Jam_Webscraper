#include<bits/stdc++.h>
#define ll long long 

using namespace std;

int main()
{

	FILE *fp = fopen("output.txt" , "w+");
	int T;cin >> T;
	for(int I = 1;I <= T;I++)
	{
		//ll int n;
		//cin >> n;
		
		int r , c;
		cin >> r >> c;
		string s[r + 1];
		for(int i = 1;i <= r;i++)
		{
			cin >> s[i];
			s[i] = ' ' + s[i];
			//cout << s[i] << "\n";
		}
		for(int i = 1;i <= r;i++)
		{
			int fl = 0;
			for(int j = 1;j <= c - 1;j++)
			{
				if(s[i][j] != '?' && s[i][j + 1] == '?')	
				{
					s[i][j + 1] = s[i][j];fl = 1;cout << s[i][j];
				}
			}
			for(int j = c;j > 1;j--)
			{
				if(s[i][j] != '?' && s[i][j - 1] == '?')	
				{
					s[i][j - 1] = s[i][j];fl = 1;cout << s[i][j];
				}
			}
		}
		for(int i = 1;i <= r - 1;i++)
		{
			for(int j = 1;j <= c;j++)
			{
				if(s[i][j] == '?' && s[i + 1][j] != '?')
				{
					s[i][j] = s[i + 1][j];cout << s[i][j];
				}
			}
		}
		for(int i = r;i > 1;i--)
		{
			for(int j = 1;j <= c;j++)
			{
				if(s[i][j] == '?' && s[i - 1][j] != '?')
				{
					s[i][j] = s[i - 1][j];cout << s[i][j];
				}
			}
		}
		for(int i = 1;i <= r - 1;i++)
		{
			for(int j = 1;j <= c;j++)
			{
				if(s[i][j] == '?' && s[i + 1][j] != '?')
				{
					s[i][j] = s[i + 1][j];cout << s[i][j];
				}
			}
		}
		for(int i = r;i > 1;i--)
		{
			for(int j = 1;j <= c;j++)
			{
				if(s[i][j] == '?' && s[i - 1][j] != '?')
				{
					s[i][j] = s[i - 1][j];cout << s[i][j];
				}
			}
		}
		//print
		fprintf(fp , "Case #%d:\n" , I);
		char x;
		//cout << "Case #<<I<<:"<<endl;
		for(int i = 1;i <= r;i++)
		{
			for(int j = 1;j <= c;j++)
			{
				x = s[i][j];
				fprintf(fp , "%c" , x);
				cout << s[i][j] ;
			}
			fprintf(fp , "\n");
			cout << "\n";
		}
	}
}
