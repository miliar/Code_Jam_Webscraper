#include <iostream>
#include <string>
#include <vector>
using namespace std;
int flip;
string cake;
int answer;
int check;
int k;
vector <int>pm;
void Smile()
{
	int num,i=0;
	answer=0;
	check=0;k=0;
	pm.clear();
	
	for(int i=0;i<cake.size();i++)
	{
		if(cake[i] == '-')
		{
			answer+=1;
			if(i+flip>cake.size())
			{
				check=-1;
				break;
			}
			for(int j=i;j<i+flip;j++)
			{
				if(cake[j] == '-')
					cake[j] = '+';
				else
					cake[j] = '-';
			}
		}
	}
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testCase;
	scanf("%d",&testCase);

	for(int i=0;i<testCase;i++)
	{
		cin>>cake;
		cin>>flip;
		Smile();
		
		if(check == -1)
			cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<'\n';
		else
			cout<<"Case #"<<i+1<<": "<<answer<<'\n';

	}

	return 0;
}