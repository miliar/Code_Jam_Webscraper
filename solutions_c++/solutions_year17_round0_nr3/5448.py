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
	// 다 돌아보면서 min인 자식을 찾는다.. 
	// max도 저장해놔야지~~
	 
	for(int i=1; i<=n; i++)
	{
		if(stall[i][0] != -1) // 이미 차있어요~~~ 
		{
			int tmp = min(stall[i][0], stall[i][1]);
			
			if(min_s < tmp) // tmp값이 min_s보다 크면 
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
	
	if(k == 1) //마지막 놈까지 지 자리를 찾아갔지.. 
	{
		printf("%d %d\n", max_s, min_s);
		return;
	}
	
	stall[wh][0] = -1;
	stall[wh][1] = -1;
	
	// 새롭게 돌면서 이제 새롭게 자리를 지정해주자. 
	
	for(int i=wh-1; i>=1; i--) //wh 왼쪽으로~~~ 
	{
		if(stall[i][0] == -1) break;
		stall[i][1] = wh - i - 1;
	}
	for(int i=wh+1; i<=n; i++) //wh 오른쪽으로~~~
	{
		if(stall[i][0] == -1) break;
		stall[i][0] = i - wh - 1;
	}
	
	stallin(k-1);
}

void solve(void)
{
	// small case만 통과하게..
	memset(stall, 0, sizeof(int));
	
	int k;
	scanf("%d %d", &n, &k);
	
	stall[0][0] = -1;
	stall[0][1] = -1;
	
	stall[n+1][0] = -1;
	stall[n+1][1] = -1;
	
	for(int i=1; i<=n; i++) // stall 초기화 
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
