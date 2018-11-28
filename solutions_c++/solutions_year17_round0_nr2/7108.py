#include <iostream>
#include <algorithm>
#include <string>
#include <fstream>
#include <iostream>
using namespace std;
string num;
char inputString[100];
void testCase()
{
	int i=0;
	int check=0;
	while(i<num.size()) // 앞에 숫자 0이면 출력 안하면됨.
	{
		if(check==0)
		{
			if(num[i]>num[i+1] && (i+1 != num.size()))
			{
				num[i] -= 1;
				check=-1;
			}
		}
		else		
			num[i]=57;		
		i++;
	}
	for(i=0;i<num.size()-1;i++)
	{
		if(num[i] > num[i+1])
		{
			testCase();
			break;
		}
	}

}
int main(void)	
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	int zeroCheck=0;
	scanf("%d",&n);
	for(int i=0;i<n;i++)
	{
		printf("Case #%d: ",i+1);
		cin>>num;
		testCase();
		for(int j=0;j<num.size();j++)
		{
			if(num[j]-48 == 0 && zeroCheck==0)
			{}
			else
			{
				zeroCheck=-1;
				printf("%d",num[j]-48);
			}
		}
		cout<<'\n';
		zeroCheck=0;
	}

	return 0;
}