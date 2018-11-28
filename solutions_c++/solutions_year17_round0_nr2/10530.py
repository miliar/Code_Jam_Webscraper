#include<iostream>
#include<math.h>
#include<fstream>
using namespace std;

int main()
{
	ifstream in("B-small-attempt2.in");
	ofstream out("B-small-attempt2.out");
	int t;
	in>>t;
	int n[t];
	for(int i=0;i<t;i++)
	{
		in>>n[i];
	}
	int i=1;
	int t1,t2=10,t3;
	for(int j=0;j<t;j++)
	{
	while(n[j]/t2 !=0)
	{
		t2=pow(10,i);
		t1=t2*10;
		t3=pow(10,i-1);
		if((n[j] % t2)/t3 >= (n[j]%t1)/t2)
		{
			i++;
		}
		else
		{
	 	 	n[j]=n[j]-1;
			i=1;
		}
		
	}
	i=1;
	t2=10;
	out<<"Case #"<<j+1<<":\t"<<n[j]<<endl;
	}
	return 0;
}
