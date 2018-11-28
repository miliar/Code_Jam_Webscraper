#include <iostream>
#include <vector>
#include <math.h>
#include <map>
#include <algorithm>
#include <string>
#include <set>
#include <fstream>
using namespace std;
#define fori(v) for(int i=0; i<v; i++)
#define forj(v) for(int j=0; j<v; j++)
#define forl(v) for(int l=0; l<v; l++)
#define fork(v) for(int k=0; k<v; k++)
#define mp(a,b) make_pair(a,b)
#define ff first
#define ss second
#define lli long long int
int main()
{
	ifstream input;
	input.open("input.txt");
	ofstream output;
	output.open("output.txt");
	int t;
	input>>t;
	forl(t)
	{
		int r,c;
		input>>r>>c;
		char arr[r][c];
		fori(r)
		{
			forj(c)
			{
				input>>arr[i][j];
			}
		}
		fori(r)
		{
			forj(c)
			{
				int from , to ;
				if(arr[i][j]!='?')
				{
					int z = i-1;
					while(z>-1 && arr[z][j]==arr[i][j])  // height of column
					--z;
					from = z+1;
					z = i;
					while(z<r && arr[z][j]==arr[i][j])
					++z;
					to = z;
					z = j;
					bool is_clear = true;     // extend from left to right
					while(is_clear)
					{
						for(int k = from ; k<to; k++)
						arr[k][z] = arr[i][j];
						++z;
						if(z>=c)
						is_clear = false;
						else
						for(int k=from; k<to; k++)
						if(arr[k][z]!='?')
						is_clear = false;
					}
					z = j;
					is_clear = true;
					while(is_clear)
					{
						for(int k = from ; k<to; k++)
						arr[k][z] = arr[i][j];
						--z;
						if(z<0)
						is_clear = false;
						else
						for(int k=from; k<to; k++)
						if(arr[k][z]!='?')
						is_clear = false;
					}
					int left, right;           // find the length of row
					z = j;
					while(z>-1 && arr[i][z]==arr[i][j])
					--z;
					left = z+1;
					z = j;
					while(z<c && arr[i][z]==arr[i][j])
					++z;
					right = z;
					is_clear = true;
					z = i;      // copy from up to down row by row
					while(is_clear)
					{
						for(int k = left ; k<right; k++)
						arr[z][k] = arr[i][j];
						++z;
						if(z>=r)
						is_clear = false;
						else
						for(int k=left; k<right; k++)
						if(arr[z][k]!='?')
						is_clear = false;
					}
					is_clear = true;
					z = i;      // copy from up to down row by row
					while(is_clear)
					{
						for(int k = left ; k<right; k++)
						arr[z][k] = arr[i][j];
						--z;
						if(z<0)
						is_clear = false;
						else
						for(int k=left; k<right; k++)
						if(arr[z][k]!='?')
						is_clear = false;
					}
				}
			}
		}	
		output<<"Case #"<<l+1<<":"<<endl;
		fori(r)
		{
			forj(c)
			output<<arr[i][j];
			output<<endl;
		}
	}
}
