#include <stdlib.h>
#include <time.h>
#include <vector>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;



const int M=50;
char array[M][M];

int main()
{
	
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	
	freopen("A-large.in","r",stdin);
	freopen("output_large.out","w",stdout);
	
	
	int T;
	cin>>T;
	
	for (int cnt=1; cnt<=T; cnt++)
	{
		int R,C;
		cin>>R>>C;
		for (int i=0; i<R; i++)
		{
			for (int j=0; j<C; j++)
			{
				cin>>array[i][j];
			}
		}
		
		
		for (int row=0; row<R; row++)
		{
			char letter='?';
			for (int col=0; col<C; col++)
			{
				if (array[row][col]!='?')
				{
					letter=array[row][col];
					break;
				}
			}
			
			if (letter!='?')
			{
				int col=0;
				while (col<C)
				{
					if (array[row][col]=='?')
					{
						array[row][col]=letter;
						col++;
					}
					else
					{
						if (array[row][col]==letter)
						{
							col++;
						}
						else
						{
							letter=array[row][col];
							col++;
						}
					}
				}
			}
		}
		
		for (int col=0; col<C; col++)
		{
			char letter='?';
			for (int row=0; row<R; row++)
			{
				if (array[row][col]!='?')
				{
					letter=array[row][col];
					break;
				}
			}
			
			if (letter!='?')
			{
				int row=0;
				while (row<R)
				{
					if (array[row][col]=='?')
					{
						array[row][col]=letter;
						row++;
					}
					else
					{
						if (array[row][col]==letter)
						{
							row++;
						}
						else
						{
							letter=array[row][col];
							row++;
						}
					}
				}
			}
		}
		
		/*for (int row=0; row<R; row++)
		{
			if (array[row][0]=='?')
			{
				int index_low=-1;
				for (int i=row+1; i<R; i++)
				{
					if (array[i][0]!='?')
					{
						index_low=i;
						break;
					}
				}
				
				if (index_low!=-1)
				{
					
				}
				int index_up=-1;
				for (int i=row-1; i>=0; i--)
				{
					if (array[i][0]!='?')
					{
						index_up=i;
						break;
					}
				}
				
				if (row-1>=0)
				{
					for (int col=0; col<C; col++)
					{
						array[row][col]=array[row-1][col];
					}
				}
				else
				{
					for (int col=0; col<C; col++)
					{
						array[row][col]=array[row+1][col];
					}
				}
			}
		}*/
		cout<<"Case #"<<cnt<<":"<<endl;
		for (int i=0; i<R; i++)
		{
			for (int j=0; j<C; j++)
			{
				cout<<array[i][j];
			}
			cout<<endl;
		}
		
	}
	
	
	
	
	
	return 0;
	
}
