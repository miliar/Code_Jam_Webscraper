#include<cstdio>

/*

99999�� �ٲ��� �ϴµ�..
for���� �ѹ� �� ������ �ϳ�;;

*/

void solve(void)
{
	long long int n;
	scanf("%lld", &n);

	int len, arr[20] = {0};
	
	for(int i=0; ; i++)
	{
		arr[i] = n % 10; // ���� ������� ���±�.. 
		n /= 10;
		if(n == 0)
		{
			len = i;
			break;
		}
	}
	
	for(int x=0; x<=len; x++)
	{
		for(int i=len; i>0; i--)
		{
			if(arr[i] > arr[i-1])
			{
				//�׵ڿ������ ���.. 9�� �ȴ�..
				arr[i]--;
	
				for(int j=i-1; j>=0; j--) 
				{
					arr[j] = 9;
				}
				
				break;
			}
		}
	}
	
	for(int i=len; i>=0; i--)
	{
		if(!(i == len && arr[i] == 0)) printf("%d", arr[i]);
	}
	
	puts("");
	
}

int main()
{
	freopen("B-large.in", "r", stdin);	
	freopen("output.out", "w", stdout);
	
	int t;
	scanf("%d", &t);
	for(int i=1; i<=t; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
}
