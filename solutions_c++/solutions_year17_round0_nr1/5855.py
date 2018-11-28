#include<iostream>
#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cmath>
#include<array>


using namespace std;
/*
bool isPrime(int);
void swap(int &,int &);
void quicksort(long int[],int,int);
int decto(int,int);
int todec(int,int);
*/

int main()
{
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		int flip,temp,state=0,ctr=0;
		char str[1000];
		cin>>str;
		cin>>flip;
		int len = strlen(str);
		cout<<"Case #"<<t<<": ";
		for(int i=0; i<len;i++)
		{
			if(str[i]=='-')
			{
				if(i+flip<=len)
				{
					temp = i;
					for(int j=0;j<flip;j++,i++)
					{
						switch(str[i])
						{
							case '-':
							str[i] = '+';
							break;
							case '+':
							str[i] = '-';
							break;
							default:
								;
						}
					}
					ctr++;
					for(int j=temp;j<len;j++)
					{
						if(str[j]=='-')
						{
							i=j-1;
							break;
						}
					}
				}
				else
				{
					cout<<"IMPOSSIBLE"<<endl;
					state=1;
					break;
				}
			}
		}
		if(state==0)
		{
			cout<<ctr<<endl;
		}
	}
	return 0;
}