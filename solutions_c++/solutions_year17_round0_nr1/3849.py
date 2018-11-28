/**RootAccess IIT Madras*/
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <stack>

using namespace std;

#define INF 1000000007
#define pb push_back
#define rep(a,b) for(i=a;i<b;i++)

int main(int argc, char const *argv[])
{
	int t;
	cin>>t;
	for(int cas=1;cas<=t;cas++)
	{
		string s;
		cin>>s;
		int k;
		cin>>k;
		int flips = 0;
		for(int i = 0; i<= s.length()-k;i++)
		{
			if(s[i] == '+')
				continue;
			for(int j = i; j<i+k; j++)
			{
				if(s[j] == '-')
					s[j] = '+';
				else s[j] = '-';
			}
			flips++;
			//cout<<s<<endl;
		}
		int fal = 0;
		for(int i = s.length()-k; i<s.length(); i++)
			if(s[i] == '-')
				{
					fal = 1;
					break;
				}
		if(fal == 1)
			cout<<"Case #"<<cas<<": IMPOSSIBLE"<<endl;
		else
		cout<<"Case #"<<cas<<": "<<flips<<endl;

	}
	return 0;
}