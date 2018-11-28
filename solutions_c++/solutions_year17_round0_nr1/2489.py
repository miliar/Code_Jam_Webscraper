#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <queue>
#include <functional>
#include <list>
#include <set>
#include <sstream>
#define ll long long
#define INF 1000000007

using namespace std;

int main()
{
	ios::sync_with_stdio(false);

	//while(cin>>n)

	int T;
	cin>>T;
	for(int cas=1;cas<=T;cas++)
	{
		string s;
		int n, ans=0;
		cin>>s>>n;

		for(int i=0; i+n-1<s.length(); i++)
		{
			if(s[i] == '-')
			{
				for(int j=0; j<n; j++)
				{
					if(s[i+j]=='-')
						s[i+j]='+';
					else
						s[i+j]='-';
				}
				ans++;
			}
		}
		for(int i=0; i<s.length(); i++)
			if(s[i]=='-')
				ans=-1;
		cout<<"Case #"<<cas<<": ";
		if(ans != -1)
			cout<<ans<<endl;
		else 
			cout<<"IMPOSSIBLE"<<endl;

		//cout<<"Case "<<cas<<": ";
	}

	return 0;
}
