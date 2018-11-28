
// just use a heap of pair with size of the index of the gap and the size of the gap to the left as the second parameter(highest gap at the top, for equal gaps lowest index to the left)
#include<iostream> 
//#include<queue>
using namespace std;

void updateAllPrevColsWithVal(char** grid, int row, int endCol)
{
	for(int col=0; col<endCol; ++col)
		grid[row][col]=grid[row][endCol];
}

void updateAllColsWithRowOneAbove(char** grid, int destinationRow, int r, int c)
{
	if(destinationRow==0)
		cout<<"error from updateAllColsWithRowOneAbove";
	for(int i=0; i<c; ++i)
		grid[destinationRow][i]=grid[destinationRow-1][i];
}

void updateAllRowsAboveWithCurRowValues(char** grid, int sourceRow, int r, int c)
{
	for(int i=0; i<sourceRow; ++i)
		for(int j=0; j<c; ++j)
			grid[i][j]=grid[sourceRow][j];
}

int main()  
{
	int r, c;
	int t;
	cin>>t;
	for(int i=1; i<=t; ++i)	
	{
		cin >> r>> c;
		char** grid=new char*[r];
		bool noIniFound=true;
		bool markedForUpdateOfAllRowsAboveWithCurRowValues=false;
		for(int i=0; i<r; ++i)
		{
			char prevIni='?';
			grid[i]=new char[c];
			for(int j=0; j<c; ++j)
			{	
				cin>>grid[i][j];
				if(grid[i][j]!='?')
				{
					if(noIniFound)
					{
						noIniFound=false;
						if(i>0)
							markedForUpdateOfAllRowsAboveWithCurRowValues=true;
					}
					if(prevIni=='?')
					{
						updateAllPrevColsWithVal(grid, i, j);
					}
					prevIni=grid[i][j];
				}
				else
				{
					grid[i][j]=prevIni;
				}
			}
			// no values in this row but at least some value found previously
			if(prevIni=='?' && !noIniFound)
				updateAllColsWithRowOneAbove(grid, i, r, c);
			if(markedForUpdateOfAllRowsAboveWithCurRowValues && i>0)
			{
				updateAllRowsAboveWithCurRowValues(grid, i, r, c);
				markedForUpdateOfAllRowsAboveWithCurRowValues=false;
			}
			
		}
		
		cout << "Case #" << i << ": "<<endl;
		for(int i=0; i<r; ++i)
		{
			for(int j=0; j<c; ++j)
				cout<<grid[i][j];
			cout<<endl;
		}
	
	}
	return 0;
}

