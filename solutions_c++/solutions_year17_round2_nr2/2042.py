#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <stdio.h>
#define lld long long int
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int test=1;test<=t;test++)
    {
    	int n,r,o,y,g,b,v;
    	cin>>n>>r>>o>>y>>g>>b>>v;
    	string flag="";
    	for(int a=0;a<n;a++)
    		flag.push_back('a');

    	vector<pair<int,char>>data;
    	data.push_back(make_pair(r,'r'));
    	data.push_back(make_pair(y,'y'));
    	data.push_back(make_pair(b,'b'));
    	sort(data.rbegin(),data.rend());
    	if(data[0].first>data[1].first+data[2].first)
    	{
    		printf("Case #%d: IMPOSSIBLE\n",test);
    		continue;
    	}
    	int count=0;
		int put=data[0].first;
		char ch=data[0].second;
		int pos=0;
		while(put>0)
		{
			flag[pos]=ch;
			put--;
			pos+=2;
			count++;
		}
		data.erase(data.begin());
		int col1=data[0].first,col2=data[1].first;
		char e=data[0].second,f=data[1].second;
		pos=n-1;
		while(count<n)
		{
			if(col1>0 && flag[pos]=='a')
			{
				count++;
				col1--;
				flag[pos]=e;
				pos--;
			}
			if(col2>0 && flag[pos]=='a')
			{
				count++;
				col2--;
				flag[pos]=f;
				pos--;
			}
			if(flag[pos]!='a')
				pos--;
			if(col1<=0 && col2<=0)
				break;
		}
		cout<<"Case #"<<test<<": "<<flag<<"\n";
	}
}