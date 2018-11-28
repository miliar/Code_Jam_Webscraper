#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <list>
#include <stack>
#include <set>


using namespace std;

int main()
{
	int T=0;
	cin>>T;
	for(int t=1; t<=T; t++)
	{
		cout<<"Case #"<<t<<": \n";

		int R=0;
		int C=0;
		
		cin>>R;
		cin>>C;
		char arr[R][C] ={0};

		for( int i=0; i<R; i++)
		{
			for(int j=0; j<C; j++)
			{
				cin>>arr[i][j];
			}
		}
		/*
		for( int i=0; i<R; i++)
		{
			for(int j=0; j<C; j++)
			{
				cout<<arr[i][j];
			}
			cout<<"\n";
		}
		*/

		for(int i=0; i<R; i++)
		{
			bool finds = false;
			for(int j=0; j<C; j++)
			{
				if(arr[i][j] != '?')
				{
					//handle right 
					char tmp=arr[i][j];
					for(int a=j+1; arr[i][a] == '?' && a<C; a++)
					{
						arr[i][a]=tmp;
					}

					for(int a=j-1; arr[i][a] == '?' && a>=0; a--)
					{
						arr[i][a] = tmp;
					}


					finds = true;
				}
			}

		}

		for( int i=0; i<C; i++)
		{
			bool finds = false;
			for(int j=0; j<R; j++)
			{
				if(arr[j][i] != '?')
				{
					char tmp = arr[j][i];
					for(int a=j+1; arr[a][i] == '?' && a<R; a++)
						arr[a][i] = tmp;
					for(int a=j-1; arr[a][i] == '?' && a>=0 ;a--)
						arr[a][i] = tmp;

					finds = true;
				}
			}
		}


		for( int i=0; i<R; i++)
		{
			for(int j=0; j<C; j++)
			{
				cout<<arr[i][j];
			}
			cout<<"\n";
		}

		//cout<<"\n";
	}

	return 0;
}


