#include <bits/stdc++.h>
#include <string>
using namespace std;
void findtidy(string str)
{
    int x = str.length();
    int a, b, place;
    int arctr = 0;
    int newar[x];
    bool flag = false;
    for (int i = 0; i < x-1; ++i)
    {
    	a = (str[i] - '0')%48;
    	b = (str[i+1] - '0')%48;
    	newar[arctr++] = a;
    	if (a > b)
    	{
    		flag = true;
    		place = i+1;
    		break;
    	}
    }
    if (flag)
    {
    	//do some
    	// printf("\nplace:%d\n", place);
    	/*for (int i = 0; i < arctr; ++i)
    	{
    		printf("%d", newar[i]);
    	}
    	printf("\n");*/
    	for (int i = place; i < x; ++i)
    	{
    		newar[i] = 9;
    	}
    	int last = place - 1;
    	int v = newar[last];
    	int nu = last;
    	while(nu>0 && v == newar[nu-1])
		{
			newar[nu] = 9;
			nu--;
		}
		newar[nu] = newar[nu] - 1;
    	for (int i = 0; i < x; ++i)
    	{
    		if (newar[i])
    		{
	    		printf("%d", newar[i]);
    		}
    	}
    	printf("\n");
    	/*
    	// for(int i = last; i > 0; i--)
    	// {
		int i;
		
		
		newar[i] = newar[i] - 1;
		for(int j = 0; j < x; ++j)
		{
			printf("%d", newar[i]);
		}
		printf("\n");*/
    	// }
    }
	else
	{
		for (int i = 0; i < arctr; ++i)
	    {
	    	printf("%d", newar[i]);
	    }
	    printf("%d ", (str[arctr]-'0')%48);
	    printf("\n");
	}
}
int main(int argc, char const *argv[])
{
	int t;
	long long int n;
	string str;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i)
	{
		scanf("%lld", &n);
		str = to_string(n);
		if (str.length() == 1)
		{
			printf("case #%d: %lld\n", i+1, n);
		}
		else
		{
			cout<<"case #"<<i+1<<": ";
			findtidy(str);
		}
	}
	return 0;
}