#include<iostream>
#include<fstream>
using namespace std;
int calc( int);
int main()
{
	ifstream textfile;
	textfile.open("input.txt");
	long long int t;
	textfile>>t;
	long N;
	for(int i=0;i<t;i++)
	{
		textfile>>N;
		if(N<10)
		{
		cout<<"Case #"<<i+1<<": "<<N <<endl;
		}
		else
		{
		cout<<"Case #"<<i+1<<": "<<calc(N) <<endl;
		}
	}
	textfile.close();
	}
int calc( int n)
{
    long long int coun,res,f2,f,j;
	for(j=1;j<=n;j++)
	{
	long long int  p =j;
     f = p%10;
     p = p/10;
	 while(p>0)
	 {
	 	f2 = p%10;
	 	p= p/10;
	 	if(f2>f)
	 	{
	 		coun = 0;
	 	break;
		}
		else
		{
			f = f2;
			f2 = p;
			coun = coun+1;
		}

	 }
	 if(coun>0)
	 {
	 	res =j;

	 }
   }
   return res;
}












