#include<bits/stdc++.h>
using namespace std;
int main()
{
	ifstream input;
	input.open("B-small-attempt1.in");
	ofstream output;
	output.open("udit.txt");
	long long t,v;
	input>>t;
	for(long long j=1;j<=t;j++)
    {


		long long m;
		input>>m;
		long long udit=m;
		long long k,length=0;
		string vk;
		while(m!=0)
		{
			length++;
			 if(m>1 || m<100)
			 {
			 	k=m;
			 }
			m=m/10;

		}
		long long fuck=1;;
		for(long i=0;i<length-1;i++)
		{

		    fuck=fuck*10;
		}
		fuck=k*fuck;

		long long penis=0;
		long long pussy=length;
		for(long long i=0;i<length;i++)
		{
			pussy--;
			penis=penis+k*pow(10,pussy);
		}
		//cout<<"penis= "<<penis<<endl;
		if(udit<penis)
		{
			output<<"Case #"<<j<<": "<<fuck-1<<endl;
		}
		else if(udit==penis)
		{
			output<<"Case #"<<j<<": "<<udit<<endl;
		}
		else
		{
		ostringstream convert;   // stream used for the conversion

convert << udit;      // insert the textual representation of 'Number' in the characters in the stream

vk = convert.str();
int abhi=0;
string min;
//cout<<"vklength= "<<vk.length()<<endl;
for( long long i=0;i<vk.length();i++)
{

	if(vk[i]>vk[i+1] && abhi==0 && i!=vk.length()-1 )
	{
		abhi++;
		int i_value = char(vk[i]);
		char er=char(i_value-1);
		vk[i]=er;
	}
	else if(abhi>0)
	{
		vk[i]='9';
	}
	//cout<<"abhi= "<<abhi;
}
	output<<"Case #"<<j<<": "<<vk<<endl;

		}
	}
}
