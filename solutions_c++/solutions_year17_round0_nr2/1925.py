#include<bits/stdc++.h>
using namespace std;
int main(void)
{
	int a;
	FILE* fp = fopen("Output.txt", "w+");
	scanf("%d\n", &a);
	for(int x=0;x<a;x++)
	{
		long long n, m, i;
		scanf("%lld", &n);
		string str1 = to_string(n), str2 = to_string(m=n);
		for(i=0;i<str1.size()-1;i++)
			if(str1[i]>str1[i+1])
				break;
		if(i<str1.size()-1)
		{
			while(str1[i-1] == str1[i])
				i--;
			i = pow(10, str1.size()-i-1);
			n -= n%i+1;
		}
		fprintf(fp, "Case #%d: %lld\n", x+1, n);
	}
}
