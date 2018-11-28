#include<iostream>
#include<cstdlib>
#include<bits/stdc++.h>

using namespace std;

int sortChk(int arr[],int c)
{
	int flag = 0;
	int sav = -1;
	for(int i = c;i >= 0;i--)
	{
		if(flag == 0 && i!=0)
		{
			if(arr[i] == arr[i-1])
			{
				sav = i;
			}
			if(arr[i]>arr[i-1])
			{
				if(arr[i] == 1)
				{
					i = c;
					flag = 2;
					continue;
				}
				if(sav == -1)
					arr[i] -= 1;
				else
				{
					arr[sav] -= 1;
					i = sav;
				}	
				flag =1;
			}
		}
		else if(flag==1 || flag == 2)
		{
			arr[i] = 9;
		}
	}
	if(flag == 2)
	{
		return 0;
	}
	return 1;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int t;
	int x1  = 1;
	long long int n;
	int arr[100] = {0};
	cin >> t;
	while(t--)
	{
		int c = -1;
		cin >> n;
		while(n!=0)
		{
			int rem = n%10;
			c++;
			arr[c] = rem;
			n = n/10;
		}
		int result = sortChk(arr,c);
		if(result == 0)
			c--;
		for(int i = c;;)
		{
			if(arr[c] == 0)
			c--;
			else
			break;
		}
		printf("Case #%d: ",x1);
		x1++;
		for(int i = c;i > -1;i--)
		{
			printf("%d",arr[i]);
	 	}
		// << endl;
		printf("\n");
	}
}
