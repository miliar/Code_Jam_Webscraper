#include<iostream>
#include<map>
#include<algorithm>
using namespace std;

int main()
{
	FILE *fp, *fp1;
	fp = fopen("C-large.in", "r");
	fp1 = fopen("C-large.out", "w");
	int t;
	fscanf(fp,"%d", &t);
	for (int a = 1; a <= t; a++)
	{
		map<long long, long long> m;
		long long n, k;
		fscanf(fp,"%lld %lld", &n, &k);
			m[n] = 1;
			long long left=0, right=0;
		map<long long, long long>::iterator it=m.end();
		for(;it!= m.begin();it=m.end())
		{
			it--;
			long long size = it->first;
			k -= it->second;

			if (size % 2)
			{
				m[(size - 1) / 2] += 2*m[size];
				left = (size - 1) / 2;
				right = left;
			}
			else
			{
				m[(size / 2) - 1]+=m[size];
				m[size / 2]+=m[size];
				left = (size / 2) - 1;
				right = size / 2;
			}
			if (k <= 0)
				break;
			m.erase(it);
		}
		fprintf(fp1,"Case #%d: %lld %lld\n",a, max(left, right), min(left, right));
		//printf( "%d %d\n", max(left, right), min(left, right));
	}
}
