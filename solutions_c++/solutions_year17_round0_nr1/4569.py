#include <bits/stdc++.h>
#include <iostream>
#include <algorithm>
using namespace std;
char fn(char a)
{
	char x;
	if(a=='+'){ x= '-' ;}
	if(a=='-'){ x= '+' ;}
	return x;
}
int main()
{
	int t,i,p;
	cin >> t;
	for(i=1;i<=t;i++)
	{
		string x;
		int k;
		cin >> x >> k;
		int j=0;
		int count=0;
		while((j+k-1)!=x.length())
		{
			if(x[j]=='-')
			{
			   count++;
			   for(p=0;p<k;p++){ x[j+p]=fn(x[j+p]);}
			}
			j++;
		}
		int q=x.length()-1;
		int num=0;
		for(p=0;p<k;p++){ if(x[q-p] == '-'){ num=1;break;}}
		if(num==0){cout << "Case #" <<i<<": "<< count << endl;}
		else{cout << "Case #" <<i<<": "<< "IMPOSSIBLE" << endl;}
	}
	return 0;
}