#include <bits/stdc++.h>

using namespace std;
typedef long long int lli;

int main()
{
	ios_base::sync_with_stdio();
	int T;
	char arr[25*25+1];	
	string str;
	cin >> T;
	int R, C;
	for(int aa=1;aa<=T;++aa)
	{
		cin >> R >> C;
		for(int i=0;i<R;++i)
		{
			cin >> str;
			for(int j=0;j<C;++j)
				arr[j+i*C] = str.at(j);
		}
		arr[R*C] = '\0';
		int empty = 0;
		for(int i=R-1;i>=0;--i)
		{
			empty = 1;
			for(int j=0;j<C;++j)
			{
				// check for empty
				if(arr[j+i*C] != '?')
				{
					empty = 0; break;
				}
			}
			if(!empty)
			{
				char prev = '?';
				for(int j=0;j<C;++j)
				{
					if(arr[j+i*C] == '?')
						arr[j+i*C] = prev;
					else
						prev = arr[j+i*C];
				}
				//get first
				for(int j=C-1;j>=0;--j)
				{
					if(arr[j+i*C] != '?')
					{
						prev = arr[j+i*C];
					}
					else
						arr[j+i*C] = prev;
				}
			}
			else if(empty && i != R-1)
			{
				for(int j=0;j<C;++j)
					arr[j+i*C] = arr[j+(i+1)*C];
			}
		}
		for(int i=0;i<R;++i)
		{
			empty = 1;
			for(int j=0;j<C;++j)
			{
				// check for empty
				if(arr[j+i*C] != '?')
				{
					empty = 0; break;
				}
			}
			if(!empty)
			{
				char prev = '?';
				for(int j=0;j<C;++j)
				{
					if(arr[j+i*C] == '?')
						arr[j+i*C] = prev;
					else
						prev = arr[j+i*C];
				}
				//get first
				for(int j=C-1;j>=0;--j)
				{
					if(arr[j+i*C] != '?')
					{
						prev = arr[j+i*C];
					}
					else
						arr[j+i*C] = prev;
				}
			}
			else if(empty && i != 0)
			{
				for(int j=0;j<C;++j)
					arr[j+i*C] = arr[j+(i-1)*C];
			}
		}
		cout << "Case #" << aa << ":" << endl;
		for(int i=0;i<R;++i)
		{
			char prev = arr[(i+1)*C];
			arr[(i+1)*C] = '\0';
			cout << (arr+i*C) << endl;
			arr[(i+1)*C] = prev;
		}
	}


	return 0;
}
