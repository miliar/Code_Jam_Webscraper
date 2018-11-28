#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<iostream>
#include<string>
using namespace std;
int main() 
{
	freopen("output.out", "w", stdout);
	cin.sync_with_stdio(false);
	freopen("input.in", "r", stdin);
	int testcases = 0;
	scanf("%d", &testcases);
	for (int i = 0;i < testcases;i++) 
	{
		string x;
		cin >> x;
		for (int j = x.size() - 1;j >= 1;j--) 
		{
			if (x[j] < x[j - 1])
			{
				x[j] = '9';
				x[j - 1] --;
			}
		}
		printf("Case #%d: ", i+1);
		int k = 0;
		bool flag = false;
		while (k!=x.size()) 
		{
			
			if (flag) 
			{
				cout << '9';
				k++;
				continue;
			}
			if (x[k] == '0') 
			{
				k++;
				continue;
			}
			if (x[k] == '9')
				flag = true;
			cout << x[k++];
		}
		if(i!= testcases-1)printf("\n");
	
	}
}