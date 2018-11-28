#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(void)
{
	int a;
	FILE* fp = fopen("Output.txt", "w+");
	scanf("%d\n", &a);
	for(int x=0;x<a;x++)
	{
		long long k, n, t, temp1, temp2;
		scanf("%lld %lld", &n, &k);
		map <ll, ll, greater<ll>> len;
		len[n] = 1;
		for(int i=0;k>0;i++)
		{
			temp1 = len.begin()->first-1;
			temp2 = len.begin()->second;
			len.erase(len.begin());
			k -= temp2;
			//printf("%lld %lld %lld %lld %lld\n", k, temp1+1, max(temp1/2, temp1-temp1/2), min(temp1/2, temp1-temp1/2), temp2);
			if(k<=0) break;
			if(max(temp1/2, temp1-temp1/2)>0)
				len[max(temp1/2, temp1-temp1/2)] += temp2;
			if(min(temp1/2, temp1-temp1/2)>0)
				len[min(temp1/2, temp1-temp1/2)] += temp2;
		}
		fprintf(fp, "Case #%d: %lld %lld\n", x+1, max(temp1/2, temp1-temp1/2), min(temp1/2, temp1-temp1/2));
	}
}
