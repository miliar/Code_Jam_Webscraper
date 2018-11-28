#include<bits/stdc++.h>
using namespace std;

void print(int a[], int c)
{
	int i;
	for(i=0;i<c;i++)
		printf("%d", a[i]);
	printf("\n");
}

int main()
{
	int t;
	scanf("%d", &t);
	long long int n, m;
	int y = 1;
	while(t-->0)
	{
		scanf("%lld", &n);
		m = n;
		int c = 0;
		while(m>0)
		{
			c++;
			m/=10;
		}
		int a[c];
		m = n;
		int i = c-1;
		while(m>0 && i>=0)
		{
			a[i--] = m%10;
			m/=10;
		}
		for(i=1;i<c;i++)
		{
			if(a[i]<a[i-1]) break;
		}
		if(i==c) {printf("Case #%d: %lld\n", y, n);y++; continue;}
		int j = i;
		//cout<<j<<"\n";
		while(j<c)
		{
			a[j] = 9; j++;
		}
		//print(a, c);
		j = i-2;
		while(j>=0)
		{
			if(a[j]!=a[j+1]) break;
			j--;
		}

		int k;
		//print(a, c);
		a[j+1]--;
		for(k=j+2;k<=i-1;k++)
		{
			a[k] = 9;
		}

		for(i=0;i<c;i++) 
			if(a[i]!=0) break;
		printf("Case #%d: ", y);
		y++;
		while(i<c) {printf("%d", a[i]);i++;}
			printf("\n");

	}
}