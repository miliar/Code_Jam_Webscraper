#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int change(string &table, int range, int pos)
{

	int i=pos;
	for(i=pos; i>(pos-range) ;i--)
	{
		if(table[i]=='+')table[i]='-';
		else table[i]='+';
	}
	return 1;

}

int main(void) {
	ifstream cin("input.txt");
	ofstream cout("output.txt");


	int num;
	int range;
	cin>>num;
	int res=0;
	for(int i=1;i<=num;i++)
	{
		string temp;
		int pos=0;
		cin>>temp;
		cin>>range;
		pos=temp.size();
		while(pos>=range-1)
		{
			if(temp[pos]=='-')
				{
				change(temp,range,pos);
				res++;
				}

			pos--;
		}
		while(pos>=0)
		{
			if(temp[pos]=='-')res=-1;
			pos--;
		}
		cout<<"Case #"<<i<<": ";
		if(res==-1)cout<<"IMPOSSIBLE"<<endl;
		else cout<<res<<endl;
		res=0;
	}



	return 0;
}
