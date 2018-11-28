#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
#include<string>
#include<queue>

using namespace std;

int main()
{
	
	ifstream fin;
	fin.open("input.txt");
	ofstream fout;
	fout.open("output.txt");
	long long unsigned int t,n,k,ans1,ans2;
	fin >> t;
	for (long long unsigned int i = 0; i < t; i++)
	{
		priority_queue<long long unsigned int> stalls;
		fin >> n >> k;
		ans1 = (n - 1) / 2;
		ans2 = (n - 1 - (n - 1) / 2);
		stalls.push(ans1);
		stalls.push(ans2);
		for (long long unsigned j = 0; j<k - 1; j++)
		{
			unsigned long long int top = stalls.top();
			ans1 = top - 1 - (top - 1) / 2;
			ans2 = (top - 1) / 2;
			stalls.pop();
			if(ans2>0)
			stalls.push(ans2);
			if(ans1>0)
			stalls.push(ans1);
		}
		fout << "Case #" << i + 1 << ": " << max(ans1, ans2) << " " << min(ans1, ans2) << char(10);

	}

	return 0;
}
