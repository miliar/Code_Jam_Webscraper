#include <cstdio>
#include <iostream>
#include <unordered_set>
#include <string>
using namespace std;

string pancake(string& cakes, int k)
{
	int flips = 0;
	int len = cakes.size();
	for(int i=0;i<len;i++)
	{
		if(cakes[i]=='+') continue;
		else if(len-i<k) return "IMPOSSIBLE";
		else
		{
			for(int j=i;j<i+k;j++)
				cakes[j] = (cakes[j]=='-'?'+':'-');
			flips++;
		}
	}
	return to_string(flips);
}

int main()
{
	int t, k;
	string cakes;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>cakes>>k;
		string flips = pancake(cakes, k);
		cout<<"Case #"+to_string(i+1)+": "+flips<<endl;
	}
	return 0;
}

