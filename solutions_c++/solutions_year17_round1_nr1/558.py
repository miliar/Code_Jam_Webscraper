#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

int main()
{
	int count;
	cin >> count;
	for(int i=1; i<=count; i++)
	{
		int r, c;
		cin >> r >> c;
		vector<string> cakes(r);

		int toFill = 0;
		for(int j=0; j<r; j++)
		{
			cin >> cakes[j];
//			for(size_t k=0; k<cakes[j].size(); k++)
//			{
//				toFill += cakes[j][k] == '?';
//			}
		}

//		while(toFill > 0)
//		{
			for(size_t a=0; a<cakes.size(); a++)
			{
				int left = 0;
				char last = '?';
				for(size_t b=0; b<cakes[a].size(); b++)
				{
					if(cakes[a][b] != '?')
					{
						for(int i=left; i<b; i++)
						{
							cakes[a][i] = cakes[a][b];
						}
						last = cakes[a][b];
						left = b+1;
					}
				}
				if(last != '?')
				{
					for(int i=left; i<cakes[a].size(); i++)
					{
						cakes[a][i] = last;
					}
				}
			}

		bool retry = true;
		while(retry)
		{
			retry = false;
			for(int i=0; i<(cakes.size()-1); i++)
			{
				if(cakes[i][0] == '?')
				{
					retry = true;
					cakes[i] = cakes[i+1];
				}
			}
			for(int i=cakes.size()-1; i>0; i--)
			{
				if(cakes[i][0] == '?')
				{
					retry = true;
					cakes[i] = cakes[i-1];
				}
			}

		}
//		}

		cout << "Case #" << i << ": " << endl;
		for(int i=0; i<cakes.size(); i++)
		{
			cout << cakes[i] << endl;
		}
	}
	return 0;
}
