#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;
static vvi solve(vvi res,int r,int c)
{
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
		{
			if(res[i][j]!=0)
			{
				int k=j-1;
				while(k>-1&&res[i][k]==0)
				{
					res[i][k]=res[i][k+1];
					k--;
				}
			}
		}
		for(int j=1;j<c;j++)
		{
			if(res[i][j]==0)
				res[i][j]=res[i][j-1];
		}
	}
	for(int j=0;j<c;j++)
	{
		for(int i=0;i<r;i++)
		{
			int k=i-1;
			while(k>-1&&res[k][j]==0)
			{
				res[k][j]=res[k+1][j];
				k--;
			}
		}
		for(int i=1;i<r;i++)
		{
			if(res[i][j]==0)
				res[i][j]=res[i-1][j];
		}
	}
	return res;
}
int main() {
	ofstream fout;
	ifstream fin;
	fout.open("output.txt");
	fin.open("A-large.in");
	int t;
	fin >> t;
	for(int h=0;h<t;h++)
	{
		int r,c;
		fin >> r >> c;
		vvi res(r,vi(c));
		vector<char> tolet(27);
		int count=1;
		for(int i=0;i<r;i++)
		{
			string s;
			fin >> s;
			for(int j=0;j<c;j++)
			{
				if(s[j]=='?')
					continue;
				tolet[count]=s[j];
				res[i][j]=count;
				count++;
			}
		}
		res=solve(res,r,c);
		fout << "Case #" << h+1 << ":"  << endl;
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
				fout << tolet[res[i][j]];
			fout << endl;
		}
	}
	fout.close();
	fin.close();
    return 0;
}
