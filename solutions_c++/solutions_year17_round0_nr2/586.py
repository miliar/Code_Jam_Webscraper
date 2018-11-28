#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

int main()
{
	FILE *fp, *fo;
	
	int n, m, tot, tt;
	fp = fopen("b.input", "r");
	fo = fopen("b.output", "w");
	fscanf(fp, "%d\n", &tot);
	for (tt = 1; tt <= tot; tt++)
	{
		long long n;
		int d[1001] = {0};
		long long f[30][12] = {0};
		fscanf(fp, "%I64d", &n);
		long long m = n;
		int digit = 0;
		while (m){
			
			d[digit+1] = m%10;
			m/=10;
			digit++;			
		}

		for (int i = 1; i <= digit/2; i++)
			swap(d[i], d[digit-i+1]);
			
		fprintf(fo, "Case #%d: ", tt);
		int flag = 0;
	//	printf("%d %d%d%d\n", digit, d[1], d[2], d[3]);
		for (int ll = 1; ll <= digit+1; ll++){flag = 0;
		for (int i = 2; i <= digit; i++)
		{
			if (flag)
				d[i] = 9;
			else
				if (d[i] < d[i-1])
				{
					d[i-1]--;
					d[i] = 9;
					flag = 1;
				}
		}}
		for (int i = 1; i <= digit; i++)
			if (d[i] != 0)
				fprintf(fo, "%d", d[i]);
		fprintf(fo, "\n");
	}
//	getchar();
	fclose(fp);
	fclose(fo);
	return 0;	
} 
