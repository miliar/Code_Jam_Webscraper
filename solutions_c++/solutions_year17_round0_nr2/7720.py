#include <iostream>
#include <fstream>
#include <array> 
using namespace std;

int main()
{

ifstream fin;
fin.open("B-small-attempt0.in");
int test;
fin>>test;
ofstream fout;
fout.open("output.txt");
	
for(int x=0; x<test; x++)
{
	int num;
	fin>>num;
	fout<<"Case #"<<x+1<<": ";
	int a,b;
	for(int i=num; i>0; i--)
	{	
		int x=0;
		array <int,5> arr;
		int n=i;
		while(n!=0)
		{
			a=n%10;
			b=(n/10)%10;
			n=n/10;
			if(a>=b)
			{
			continue;
			}
			else
			break;
		}
		if(a>=b)
			{
			fout<<i<<endl;
			break;
			}
		
	}
	
}

}
