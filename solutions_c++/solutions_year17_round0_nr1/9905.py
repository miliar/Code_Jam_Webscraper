/*
 * pancake.cpp
 *
 *  Created on: 08-Apr-2017
 *      Author: user
 */
#include<iostream>
#include<stdlib.h>
using namespace std;

int flipped(string pancake)
{
	int l=pancake.length();
	for(int i=0;i<l;i++)
	{
		if(pancake[i]!='+')
			return 0;
	}
	return 1;
}
string flip_left(string pancake,int start, int k)
{
	for(int j=0;j<k;j++)
	{
		if(pancake[start+j]=='+')
			pancake[start+j]='-';
		else
			pancake[start+j]='+';
	}
	return pancake;
}
string flip_right(string pancake,int end, int k)
{
	for(int j=0;j<k;j++)
	{
		if(pancake[end-j]=='+')
			pancake[end-j]='-';
		else
			pancake[end-j]='+';
	}
	return pancake;
}
int check_pancake(string pancake,int k)
{
	int l=pancake.length(),flips=0;
	int start=0,end=l-1;
	string left_flip="",right_flip="";
	//cout<<pancake<<" "<<k<<endl;
	while(start!=end)
	{
		if(!flipped(pancake))
		{
			while(pancake[start]!='-')
				start++;

			if ((start+k)<=l) {
				pancake=flip_left(pancake,start,k);
				if(pancake==left_flip)
					return -1;
				flips++;
				int j=k;
				if((start+j)>end)
				{
					j=end+1;
					for(;j<(start+k);j++)
						if(pancake[j]=='-')
							end=j;
				}
				left_flip=pancake;
				//cout<<pancake<<endl;
			}
			else
				if(pancake==left_flip)
					return -1;
		}
		else
			return flips;
		if(!flipped(pancake))
		{
			while(pancake[end]!='-')
				end--;
			if ((end-k+1)>=0) {
				pancake=flip_right(pancake,end,k);
				if(pancake==right_flip)
					return -1;
				flips++;
				int j=k;
				if((end-j)<start)
				{
					j=start-1;
					for(;j>(end-k);j--)
						if(pancake[j]=='-')
							start=j;
				}
				right_flip=pancake;
				//cout<<pancake<<endl;
			}
			else
				if(pancake==right_flip)
					return -1;
		}
		else
			return flips;
	}
	if(flipped(pancake))
	{

		return flips;
	}
	return -1;
}

int main()
{
	int T;
	cin>>T;
	for(int t=0;t<T;t++)
	{
		int k,flips;
		string pancake;
		cin>>pancake;
		cin>>k;
		flips=check_pancake(pancake,k);
		cout<<"Case #"<<t+1<<": ";
		if(flips==-1)
			cout<<"IMPOSSIBLE";
		else
			cout<<flips;
		cout<<endl;
	}
}


