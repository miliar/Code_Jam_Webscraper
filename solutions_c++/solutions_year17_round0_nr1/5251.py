#include<cstdio>
#include<cstring>

void solve(void)
{
	// string�� 1000������ ����
	char pancake[1001];
	int k, len, cnt = 0;
	
	scanf("%s", pancake);
	scanf("%d", &k);
	
	len = strlen(pancake);
	
	int front_idx = 0, last_idx = len - 1;
	
	while(1) 
	{
		if(pancake[front_idx] != '-') //-�� ã�Ƴ�����.. 
		{
			for(int i=front_idx+1; i<len; i++)
			{
				if(pancake[i] == '-')
				{
					front_idx = i;
					break;
				}
			}
		}
		
		if(pancake[front_idx] != '-')
		{
			printf("%d\n", cnt);
			return;
		}
		
		if(pancake[last_idx] != '-')
		{
			for(int i=last_idx - 1; i>=0; i--)
			{
				if(pancake[i] == '-')
				{
					last_idx = i;
					break;
				} 
			}
		}
		
		//front_idx���� kĭ��ŭ �����µ�.. �̰� ��찡 ������.
		
		//front_idx + k - 1 < last_idx - k + 1
		//front_idx + k >= last_idx - k //���ͼ�Ʈ �ϴ� ���̴�.. 
		
		if(last_idx - front_idx > k - 1)
		{
			for(int i=0; i<k; i++) //��������̱� 
			{
				if(pancake[front_idx + i] == '+') pancake[front_idx+i] = '-';
				else pancake[front_idx + i] = '+';
			}
			
			front_idx++;

			for(int i=0; i<k; i++)
			{
				if(pancake[last_idx - i] == '+') pancake[last_idx-i] = '-';
				else pancake[last_idx - i] = '+';
			}

			last_idx--;

			cnt += 2;
		}
		else // ���࿡ ���ͼ�Ʈ �ع�����.. 
		{
			if(last_idx - front_idx == k - 1) // ��? �̻��� ���� �������� �ƴϳ�? 
			{
				for(int i=front_idx; i<=last_idx; i++)
				{
					if(pancake[i] != '-')
					{
						puts("IMPOSSIBLE");
						return;
					}
				}
				
				printf("%d\n", ++cnt);
				return;
			}
			else if(last_idx - front_idx < k - 1) // impossible 
			{
				puts("IMPOSSIBLE");
				return;
			}
		}
	}
}

int main()
{
	freopen("A-large.in", "r", stdin);	
	freopen("output.out", "w", stdout);
	
	int t;
	scanf("%d", &t);
	for(int i=1; i<=t; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
}
