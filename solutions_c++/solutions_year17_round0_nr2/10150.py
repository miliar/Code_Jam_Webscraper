#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ifstream fin("B-small-attempt1.in");
    ofstream fout("output.out");
	int t, n, m;
	fin>>t;  
	for (int i = 1; i <= t; ++i) {
    	fin>>n;
    	int r;
    	for(int j=n;j>=1;j--)
    	{
    		int a,b,c,num=j;
    		a=num/100;
    		b=(num/10)-a*10;
    		c=num%10;
    		if(c>=b&&b>=a)
			{	r=num;
				break;
			}	
		}
    	fout<< "Case #" << i << ": " << r << endl;
   }
   return 0;
}
