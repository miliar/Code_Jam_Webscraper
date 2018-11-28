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
		string s;
		int k = 0;
		cin >> s>>k;
		int times = 0;
		int size = s.size();
		for (int i = 0;i <= size-k;i++) 
		{
			if (s[i] == '-') 
			{
				times++;
				for (int j = i;j < i + k&&j<size;j++) 
				{
					if (s[j] == '-')s[j] = '+';
					else s[j] = '-';
				}
			}
		}
		printf("Case #%d: ", i+1);
		bool flag = true;
		for (int t = 1;t < k;t++)
		{
			if (s[size - t] != '+')
			{
				flag = false;break;
			}
		}
		if (flag)
			printf("%d", times);
		else printf("IMPOSSIBLE");
		if(i!= testcases-1)printf("\n");
	}
}