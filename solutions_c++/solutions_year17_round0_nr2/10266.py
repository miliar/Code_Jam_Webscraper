#include <iostream>
#include<stdio.h>
using namespace std;

int isTidy(int a[], int k)
{
	for(int i=0; i<k-1; i++)
	{
		if(a[i]<a[i+1])
			return 0;
	}
	return 1;
}

int main() {
    
	freopen("B-small-attempt2.in","r",stdin);
	freopen("a.out","w",stdout);

	// your code goes here
	long long int n, t;
	int a[20];
	int i, j;
	scanf("%lld", &t);
	for(i=0; i<t; i++)
	{
		scanf("%lld", &n);
		long long int temp = n;
		while(1)
		{
			int k=0;
			n = temp;
			while(n!=0)
			{
				a[k] = n%10;
				n = n/10;
				k++;
			}
			if(isTidy(a, k))
			{
				printf("Case #%d: %lld\n", i+1, temp);
				break;
			}
			else
			{
				temp--;
			}
		}
	}
	
	return 0;
}