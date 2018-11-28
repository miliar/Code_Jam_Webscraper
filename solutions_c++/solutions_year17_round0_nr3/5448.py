#include<stdio.h>
#include<string.h>
int stall[1000002][2];
int n;

int min(int a, int b)
{
	if (a<b) return a;
	else return b;
}

int max(int a, int b)
{
	if (a>b) return a;
	else return b;
}

void stallin(int k)
{
	int min_s = -1, max_s = 9999999;
	int wh;
	// �� ���ƺ��鼭 min�� �ڽ��� ã�´�.. 
	// max�� �����س�����~~
	 
	for(int i=1; i<=n; i++)
	{
		if(stall[i][0] != -1) // �̹� ���־��~~~ 
		{
			int tmp = min(stall[i][0], stall[i][1]);
			
			if(min_s < tmp) // tmp���� min_s���� ũ�� 
			{
				min_s = tmp;
				max_s = max(stall[i][0], stall[i][1]);
				wh = i; 
			}
			else if(min_s == tmp)
			{
				if(max(stall[i][0], stall[i][1]) > max_s)
				{
					max_s = max(stall[i][0], stall[i][1]);
					wh = i;
				}
			}
		}
	}
	
	if(k == 1) //������ ����� �� �ڸ��� ã�ư���.. 
	{
		printf("%d %d\n", max_s, min_s);
		return;
	}
	
	stall[wh][0] = -1;
	stall[wh][1] = -1;
	
	// ���Ӱ� ���鼭 ���� ���Ӱ� �ڸ��� ����������. 
	
	for(int i=wh-1; i>=1; i--) //wh ��������~~~ 
	{
		if(stall[i][0] == -1) break;
		stall[i][1] = wh - i - 1;
	}
	for(int i=wh+1; i<=n; i++) //wh ����������~~~
	{
		if(stall[i][0] == -1) break;
		stall[i][0] = i - wh - 1;
	}
	
	stallin(k-1);
}

void solve(void)
{
	// small case�� ����ϰ�..
	memset(stall, 0, sizeof(int));
	
	int k;
	scanf("%d %d", &n, &k);
	
	stall[0][0] = -1;
	stall[0][1] = -1;
	
	stall[n+1][0] = -1;
	stall[n+1][1] = -1;
	
	for(int i=1; i<=n; i++) // stall �ʱ�ȭ 
	{
		stall[i][0] = i - 1;
		stall[i][1] = n - i;
	}
	
	stallin(k);
}

int main()
{
	freopen("C-small-1-attempt0.in", "r", stdin);	
	freopen("output.out", "w", stdout);
	
	int t;
	scanf("%d", &t);
	for(int i=1; i<=t; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
}
