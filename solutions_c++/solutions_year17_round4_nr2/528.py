#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
using namespace std;
typedef long long ll;
typedef vector<int > vi;
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
		int n,c,m;
		fin >> n >> c >> m;
		vi count(n+1);
		vi count2(c+1);
		int res=0;
		for(int i=0;i<m;i++)
		{
			int pi,bi;
			fin >> pi >> bi;
			count[pi]++;
			count2[bi]++;
			res=max(res,count2[bi]);
		}
		int sum=0;
		for(int i=1;i<n+1;i++)
		{
			sum+=count[i];
			int t=sum/i;
			if(sum%i!=0)
				t++;
			res=max(res,t);
		}
		int amount=0;
		for(int i=1;i<n+1;i++)
		{
			if(count[i]>res)
				amount+=count[i]-res;
		}
		fout << "Case #" << t+1 << ": ";
		fout << res << " " << amount << endl;
	}
	fin.close();
	fout.close();
}