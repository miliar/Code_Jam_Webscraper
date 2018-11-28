#include<bits/stdc++.h>
#include<cstring>
using namespace std;

void findMaxtidy(char str[] , int l)
{
	int i;
	for(i = 1;i<l;i++)
	{
		if(str[i]<str[i-1])
		{
			break;
		}
	}
	if(i==l)
	return;
	for(int j =i;j<l;j++)
	str[j] = '9';
	str[i-1]--;
//	printf("num : %s\n",str);
//	system("pause");
	findMaxtidy(str , i);
}
int main()
{
	int t,c(1);
	cin>>t;
	cin.ignore();
	while(c<=t)
	{
		char num[25]={'\0'};
		cin.getline(num , 25,'\n');
		findMaxtidy(num,strlen(num));
		int i =0;
		while(num[i]=='0')
		i++;
		string s(num);
		printf("Case #%d: %s\n",c,s.substr(i).data());
		c++;
	}
}
