#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
using namespace std;
typedef long long ll;
typedef vector<int > vi;
typedef vector<vi > vvi;
typedef vector<vvi > vvvi;
static int solve(int val0,int val1,int val2,int val3,int p)
{
	vvvi vec(val1+1,vvi(val2+1,vi(val3+1)));
	for(int i=0;i<val1+1;i++)
	{
		for(int j=0;j<val2+1;j++)
		{
			for(int k=0;k<val3+1;k++)
			{
				if(i+j+k==0)
					continue;
				int val=(i+j+j+k+k+k)%p;
				if(i>0)
				{
					int t=0;
					if((val-1+p)%p==0)
						t++;
					vec[i][j][k]=max(vec[i][j][k],vec[i-1][j][k]+t);
				}
				if(j>0)
				{
					int t=0;
					if((val-2+p)%p==0)
						t++;
					vec[i][j][k]=max(vec[i][j][k],vec[i][j-1][k]+t);
				}
				if(k>0)
				{
					int t=0;
					if((val-3+p)%p==0)
						t++;
					vec[i][j][k]=max(vec[i][j][k],vec[i][j][k-1]+t);
				}
			}
		}
	}
	return vec[val1][val2][val3]+val0;
}

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("inputL.in");
	fout.open("output.txt");
	int T;
	fin >> T;
	for(int t=0;t<T;t++)
	{
		int n,p;
		fin >> n >> p;
		vi count(4);
		for(int i=0;i<n;i++)
		{
			int x;
			fin >> x;
			count[x%p]++;
		}
		int res=solve(count[0],count[1],count[2],count[3],p);
		fout << "Case #" << t+1 << ": ";
		fout << res << endl;
	}
	fin.close();
	fout.close();
}