#include <iostream>
#include <stdio.h>
#include <conio.h>
#include <math.h>
#include <string>
#include <fstream>

using namespace std;

int q=0;

int main ()
{

int Ex=0;
//cout<<"Enter Test"<<endl;
ifstream file ("B-small-attempt1.in");
file>>Ex;
//cin>>Ex;
ofstream tile ("Output_file.in");

for (int z=1; z<=Ex; z++)
{

	string Expression;
	
	int counter=0;
	int flag = 0;
	int g=0;
	int i=0;
	
	//cout<<"Enter The Number"<<endl;
	file>>Expression;
//	cin>>;
	
 counter= Expression.length();
	
	for (int i=0; i<counter-1; i++)
	{
		
		if (Expression.at(i)>Expression.at(i+1))
		{
			 	 for (int j=0; j<counter-1; j++)
    	{
		
		if (Expression.at(j)>=Expression.at(j+1))
		{
		    Expression.at(j)= Expression.at(j)-1;
		    g=j;
		    for (int k=g+1; k<counter; k++)
		       {
				Expression.at(k) = '9';
		       }
		    break; 
		}
		
	    q++;	
	   }
		   break;
		}
		
		q++;
			
    }
    
    if (Expression.at(0)=='0')
    {
    	 Expression.erase(0,1);
    	//cout<<"abc";
	 } 
   
	
    //cout<<"Case #"<<z<<": "<<Expression<<endl;
    tile<<"Case #"<<z<<": "<<Expression<<endl;
}

file.close();
tile.close();
	return 0;
}