#include <bits/stdc++.h>
using namespace std;

int main(int arc,char * argv[]){

    freopen("A-large.in", "r", stdin);
   freopen("A-large.out", "w", stdout);
	int  t;
	cin >> t;
	for (int k = 0; k < t; ++k)
	{   int r,c;
		cin >> r >> c;
		vector < vector <char > > a;
		int ind = 0;
		for (int i = 0; i < r; ++i)
		{
			std::vector<char> v(c);
			a.push_back(v);
			char hold = '?';
			for (int j = 0; j < c; ++j)
			{
				char temp ;
				cin >> temp;
				if (temp != '?')
  					{
  							a[i][j] = temp;
  						for (int m = j; m >-1; --m)
  						{
  							if (a[i][m] == '?')
  							a[i][m] = temp ;
  						}
  						hold = temp;
  					}

  				else 
  					a[i][j] = hold;
			}

		

		}


		
			for (int i = 0; i < r; ++i)
			{
				for (int j = 0; j < c; ++j)
				{
					if (a[i][j] !=  '?')
						for (int m = i+1; m < r; ++m)
						{
							for (int l = 0; l < c; ++l)
							{
								if (a[m][l] == '?')
									a[m][l] = a[m-1][l];
							}
						}
						for (int m = i-1; m >-1; --m)
						{
							for (int l = 0; l < c; ++l)
							{
								if (a[m][l] == '?')
									a[m][l] = a[m+1][l];
							}
						}
				}
				
			}
		
		

		





		
		cout << "Case #" << (k+1) << ": " << endl;
		for (int i = 0; i < r; ++i)
		{
			for (int j = 0; j < c; ++j)
			{
				cout << a[i][j];
			}
			cout << endl;
		}
	}
}