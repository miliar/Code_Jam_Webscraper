#include<iostream>
#include<fstream>
using namespace std;

bool is_tidy(int num)
{
	int arr[4]={0,0,0,0};
	int i=3;
	bool flag=true;
	while (num>0)
	{
		arr[i]=num%10;
		num=num/10;
		i--;
	}
	for (int j = 0; j < 3; j++)
	{
		if (arr[j]>arr[j+1])
		{
			flag=false;
			break;
		}
	}
	return flag;
}

int main()
{
	ifstream fin;
	ofstream fout;
	int t=0,n,ans;
	fin.open("B-small-attempt1.in");
	fout.open("abc1.in");
	fin>>t;
	for (int i = 0; i < t; i++)
	{
		fin>>n;
		for (int j = 1; j <= n; j++)
		{
			if (is_tidy(j))
			{
				ans=j;
			}
		}
		fout <<"Case #"<<i+1<<": "<<ans<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}