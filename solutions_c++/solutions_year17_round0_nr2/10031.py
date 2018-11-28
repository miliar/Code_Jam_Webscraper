#include <iostream>
#include <fstream>
#include <array> 
using namespace std;

int main()
{
int cases;
long int no;
long int itr;
ifstream finput;
finput.open("B-small-attempt0.in");
finput>>cases;
ofstream foutput;
foutput.open("output.out");
	
for(int x=0; x<cases; x++)
{
	finput>>no;
	foutput<<"Case #"<<x+1<<": ";
	int temp1,temp2;
    itr=no;
	while( itr>0 )
	{	
		int x=0;
		array <int,5> array1;
		long int len=itr;
		while(len!=0)
		{	temp1=len%10;
			temp2=(len/10)%10;
			len=len/10;
			if(temp1>=temp2)
			{
			continue;
			}
			else
			break;
		}
		if(temp1>=temp2)
			{
			foutput<<itr<<endl;
			break;
			}
		itr--;
	}}
	return 0;}
