#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stdio.h>
#include <sstream>
#include <limits>
#include <fstream>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output_file_name.out","w",stdout);
	int t,count;
	scanf("%d\n",&t);
	count = t;
	while(t--)
	{
		string line,input;
		vector<bool> mapping;
		int length, n,flips=0,impossible=0;
        getline(cin, line);
        istringstream iss1(line);
        iss1 >> input;
        iss1 >> n;
        length = input.length();
        for(int i=0;i<length;i++)
		{
			if(input[i]=='-')
				mapping.push_back(0);
			else
				mapping.push_back(1);
		}
		
		//Make all 1's
		for(int i=0;i<=(length-n);i++)
		{
			if(mapping[i]==0)
			{
				for(int j=i;j<(i+n);j++)
					mapping[j]=!mapping[j];
				flips++;
			}
		}
		
		for(int i=0;i<length;i++)
		{
			if(mapping[i]==0)
			{
				impossible=1;
				break;
			}
		}
		
		if(impossible)
			printf("Case #%d: IMPOSSIBLE\n",count-t);
		else
			printf("Case #%d: %d\n",count-t,flips);
		
	}
}

