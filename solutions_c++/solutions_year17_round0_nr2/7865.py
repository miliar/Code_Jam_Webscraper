#include <iostream>
#include <cstdio>
using namespace std;


void process(long int);
bool checkforerror(long int);
long int ansnum;
long int tempcount;
 int main( int argc, char const *argv[])
{
	long int T,num,i;
	cin>>T;
	for (i = 0; i < T; ++i)
	{
		cin>>num;
		ansnum=num;
		
		//cout<<"digits in "<<i+1<<" are "<<digitsnum<<"\n";
		process(num);
		cout<<"Case #"<<i+1<<": "<<ansnum<<"\n";
		

	}
	return 0;
}


void process(long int num){
	long int tempnum,i,j,currdigit,lefttocurr,mult=1;
	tempcount=0;
	tempnum=num;
		currdigit=tempnum%10;
		tempcount++;
		while(tempnum){
			lefttocurr=tempnum%100;
			lefttocurr/=10;
			if(lefttocurr>currdigit){
				
				for (i = 0; i < tempcount; ++i)
				{
					mult*=10;
				}
				
				for(j=0;j<(lefttocurr-currdigit);++j)
				ansnum=(num-(num%mult))-1;
					
			  	
			}
			currdigit=lefttocurr;
			tempcount++;
			tempnum/=10;
			mult=1;
		}
		if(checkforerror(ansnum)){
			process(ansnum);
		}


}
bool checkforerror(long int num){
	long int tempnum,currdigit,lefttocurr;
	tempnum=num;
		currdigit=tempnum%10;
		
		while(tempnum){
			lefttocurr=tempnum%100;
			lefttocurr/=10;
			if(lefttocurr>currdigit){
				
				return true;
			  	
			}
			currdigit=lefttocurr;
			
			tempnum/=10;
			
		}
		return false;

}