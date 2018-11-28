#include<stdio.h>
#include<conio.h>
#include<cstring>
#include<cmath>
#include<iostream>
#include<fstream>
using namespace std;
main()
{
	ifstream infile("B-small-attempt0.in");
	ofstream outfile;
	outfile.open("output.in");
	int T =0;
	infile>>T;
	if(T>=1 && T<=100)
	{
		for(int tc=1;tc<=T;tc++)
		{
			long long int input = 0;
			infile>>input;
			long long int answer;
			long long int temp = input;
			int count = 0;
			while(temp>0)
			{
				temp=temp/10;
				count++;
			}
			//for(int i=1000;i>=10;i/10)
			{
				//count--;
				if(count==1)
				{
					answer = input;
				}
				else
				{
					int array[count];
					int check = 0;
					while(true)
					{
						answer=0;
						check = 0;
						temp = input;
						int ccc = pow(10,count);
						if(temp%ccc == 0)
						{
							count--;
						}
						for(int j=0;j<count;j++)
						{
							array[j]=temp%10;
							temp = temp/10;
						}
						for(int k=0;k<count-1;k++)
						{
							if(array[k]>=array[k+1])
							{
								check =1;
							}
							else
							{
								check =0;
								break;
							}
						}
						if(check==1)
						{
							for(int l=count-1;l>=0;l--)
							{	
								answer=(answer*10) + array[l];
							}
							break;
						}
						input--;
					}
				}
			}
			outfile<<"Case #"<<tc<<": ";
			outfile<<answer;
			outfile<<endl;
		}
	}
	
}
