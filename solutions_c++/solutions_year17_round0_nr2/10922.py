#include<iostream>
using namespace std;

int t,x,y;
int a[100];
int b[100];
int ones,tens,huns;

void getinput()
{
	cin>>t;
	for(int i=0;i<t;i++)
		cin>>a[i];
}

void findlastno()
{
	for(int i=0;i<t;i++)
	{
		x=a[i];
		
		LABEL:
		ones=x%10;
		tens=(x/10)%10;
		huns=(x/100)%10;
		
		if(x/10==0)
			{
				b[i]=x;
			}
		else if(x==1000)	
			b[i]=999;
		else if(((ones>tens)&&(tens>huns))||((ones>=tens)&&(tens>=huns)))
			{
				b[i]=x;	
			}
		else 
			{
				x--;
				goto LABEL;
			}
	}
	}


void output()
{
	for(int i=0;i<t;i++)
		cout<<endl<<"Case #"<<i+1<<": "<<b[i];
}

int main()
{
	getinput();
	findlastno();
	output();
	return 0;
}
