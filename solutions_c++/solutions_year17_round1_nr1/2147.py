#include <stack>
#include <iostream>
#include <string>
#include <vector>
#include <cstddef>
#include <algorithm>

using namespace std;

int main()
{
	int T, counter = 1;;
	cin >> T ;

	while(T != 0 )
	{
		int R, C;
		cin >> R >> C;
		char A[R][C], temp;// = new char [R][C];

		for(int i = 0; i < R; i++)
			for(int j = 0; j < C; j++)
			{
					cin >> temp;
			//		cout << temp; 
					A[i][j] = temp;
			}



			char Val;
			int end = C;
		for(int i = 0; i < R; i++)
		{

			for(int j = 0; j < C; j++)
			{
				//cout <<"i"<< A[i][j]  <<" - "<< i << " " << j<< endl;
					
				if(A[i][j] != '?')
				{

					Val = A[i][j];
					//cout <<"1 "<< Val  <<" - "<< i << " " << j<< endl;
					for(int k = j;k< C;k++)
					{
						if(A[i][k] == '?' || A[i][k] == Val )
						{
							//cout << "2 "<<Val  <<" - "<< i << " " << j<< endl;
							A[i][k] = Val;
						}
						else if(A[i][k] != '?')
						  break;
					}
					//cout << i << j << endl;

					 for(int k = j; k >= 0; k--)
					 {
						if(A[i][k] == '?' || A[i][k] == Val )
						{
							//cout << "3 " << Val  <<" - "<< i << " " << j<< endl;
							A[i][k] = Val;
						}
						else if(A[i][k] != '?')
						  break;
					}
				}



			}
		}		
		
		for(int i = 0; i < C; i++)
		{

			for(int j = 0; j < R; j++)
			{
				//cout << j <<"," << i << endl;
				if(A[j][i] != '?')
				{

					Val = A[j][i];
					for(int k = j;k< R;k++)
					{
						if(A[k][i] == '?' || A[k][i] == Val )
						{
							//cout << "2 "<<Val  <<" - "<< i << " " << j<< endl;
							A[k][i] = Val;
						}
						else if(A[k][i] != '?')
						  break;
					}

					for(int k = j; k >= 0; k--)
					 {
						if(A[k][i] == '?' || A[k][i] == Val )
						{
							//cout << "3 " << Val  <<" - "<< i << " " << j<< endl;
							A[k][i] = Val;
						}
						else if(A[k][i] != '?')
						  break;
					}
				}
				
			}
			//cout << endl;
		}


       cout << "Case #" <<counter++<<":"<<endl;
		for(int i = 0; i < R; i++)
			{for(int j = 0; j < C; j++)
				cout << A[i][j];
				cout << endl;
			}
	T--;
	}
	return 0;
}