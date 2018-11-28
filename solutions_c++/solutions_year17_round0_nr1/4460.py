#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>
#include <queue>
#include <utility>
#include <set>
#include <bitset>
#include <stdio.h>

using namespace std;

int main(int argc, char const *argv[])
{

	int t;
	cin>>t;
	for (int i = 1; i <= t; ++i)
	{
		int n;
		string str;
		cin>>str>>n;
		// cout<<"check"<<str<<" "<<n<<endl;
		int ans=0;
		int j=0;
		while(j<str.length())
		{
			// cout<<j<<endl;
			if(str[j]=='+'){
				j++;
				continue;
			}
			else{
				if((j+n-1)<str.length()){
					int k=0;
					while(k<n && (j+k)<str.length())
					{
						if(str[j+k]=='-')
							str[j+k]='+';
						else
							str[j+k]='-';
						k++;
					}
					ans++;
					j++;
				}
				else
					break;
			}
		}
		bool isValid=true;
		for (int l = 0; l < str.length(); ++l)
		{
			if(str[l]=='-')
			{
				isValid=false;
				break;
			}
		}
		// cout<<str<<endl;
		if(isValid)
			cout<<"Case #"<<i<<": "<<ans<<endl;
		else
			cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
	}
	return 0;
}