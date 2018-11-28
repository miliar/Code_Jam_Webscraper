#include<fstream>
#include<string>

using namespace std;

char decrement(char a)
{
	switch(a)
	{
	case '9' : return '8';
	case '8' : return '7';
	case '7' : return '6';
	case '6' : return '5';
	case '5' : return '4';
	case '4' : return '3';
	case '3' : return '2';
	case '2' : return '1';
	case '1' : return '0';
	case '0' : return '9';
	default : return '9';
	}
}


int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	int t;
	fin>>t;
	for(int ca=1; ca<=t; ca++)
	{
		string num;
		fin>>num;
		int len=num.length();
		/*if(num[len-1] > '0')
			num[len-1]=decrement(num[len-1]);
		else
		{
			int i=len-1;
			while(num[i]=='0')
			{
				num[i]='9';
				i--;
			}
			num[i]=decrement(num[i]);
		}*/
		int i=len-1;
		while(i>0)
		{
			if(num[i] >= num[i-1])
			{
				i--;
				continue;
			}
			for(int j=i; j<len; j++)
				num[j]='9';
			int k=i-1;
			while(num[k]=='0')
			{
				num[k]='9';
				k--;
			}
			num[k]=decrement(num[k]);
			i--;
		}
		fout<<"Case #"<<ca<<": ";
		i=0;
		while(num[i]=='0')
			i++;
		while(i<len)
		{
			fout<<num[i];
			i++;
		}
		fout<<"\n";
	}
}