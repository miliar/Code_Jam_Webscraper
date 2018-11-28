//  Created by Chlerry in 2017.
//  Copyright (c) 2017 Chlerry. All rights reserved.
//

#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <cstring>
#include <climits>
#include <string>
#include <vector>
#include <cmath>
#include <stack>
#include <queue>
#include <set>
#include <map>
using namespace std;
#define Size 1000010
#define ll long long
#define mk make_pair
#define pb push_back
#define mem(array, x) memset(array,x,sizeof(array))
typedef pair<int,int> P;

int main()
{
    // freopen("in.txt","r",stdin);

    int T;cin>>T;
for(int ca=0;ca<T;ca++)
{
	// cout<<"-----------------"<<endl;
	string s;cin>>s;
	// cout<<s<<endl<<endl;
	if(s.size()==1)
	{
		printf("Case #%d: ",ca+1);
		cout<<s<<endl;
		continue;
	}
	for(int i=s.size()-1;i>=0;i--)
	{
		if(s[i]<s[i-1])
		{
			for(int j=i;j<s.size();j++)
				s[j]='9';
			s[i-1]--;
			// cout<<s<<endl;
		}

	}
	printf("Case #%d: ",ca+1);
	int k=0;
	while(s[k]=='0')
		k++;
	for(int i=k;i<s.size();i++)
		cout<<s[i];
	cout<<endl;
}
    return 0;
}
