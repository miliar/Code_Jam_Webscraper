#include <iostream>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <sstream>
#include <vector>
#include <queue>
#include <string>
#include <stdio.h>
#include <string.h>
#include <functional>    //for hash
#include <bitset>        //for binary

using namespace std;

int main(int argc, char *argv[])
{
    freopen("input.iN","r" , stdin);
	freopen("ans.txt","w" , stdout);
	int t;
	int x;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cout<<"Case #"<<i<<": ";
		cin>>x;
		int y;
		for(y=x;y>=0;y--)
		{
			int p=y;int temp=9;
			while(p)
			{
				int q=p%10;//cout<<q<<"   "<<temp<<endl;
				if(q>temp)break;
				temp=q;
				p/=10;
			}
			if(p==0)break;
		}
		cout<<y<<endl;
	}
	
	return 0;
}
