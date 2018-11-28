#include <cstdio>
#include <cstring>
#include <cassert>

char intToColor[] = "ROYGBV";

int otherColor(int p)
{
	return (p + 3) % 6;
}

bool primary(int p)
{
	return p % 2 == 0;
}

bool valid(int a, int b)
{
	if(a == b) return false;
	if(primary(a))
		return primary(b) || (!primary(b) && b == otherColor(a));
	else return b == otherColor(a); 
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		int N, count[6];
		scanf("%d", &N);
		for(int i = 0; i < 6; i++)
			scanf("%d", count + i);
		
		int buf[1002];
		int count2[6];
		for(int i = 0; i < 6; i++)
			count2[i] = count[i];
		
		if(count[0] > N / 2 || count[2] > N / 2 || count[4] > N / 2)
		{
			printf("Case #%d: IMPOSSIBLE\n", t);
			continue;
		}
		
		buf[0] = 0;
		if(count[2] > count[0])
			buf[0] = 2;
		if(count[4] > count[0] && count[4] > count[2])
			buf[0] = 4;
		count[buf[0]]--;
		
		for(int i = 1; i < N; i++)
		{
			if(primary(buf[i - 1]))
			{
				// has associated secondary
				if(count[otherColor(buf[i - 1])] > 0)
				{
					buf[i] = otherColor(buf[i - 1]);
					count[buf[i]]--;
				}
				else
				{
					int best = -1;
					buf[i] = 0;
					for(int j = 0; j < 6; j += 2)
						if(count[j] > 0 && count[j] > best)
						{
							if(buf[i - 1] != j && (i < N - 1 || (i == N - 1 && buf[0] != j)))
							{
								best = count[j];
								buf[i] = j;
							}
						}
					
					if(best != -1)
						count[buf[i]]--;
					else
					{
						// Find the only one remaining
						for(int j = 0; j < 6; j+= 2)
						{
							if(count[j] == 1)
							{
								best = 1;
								buf[i] = j;
								count[j]--;
								break;
							}
						}
						
						if(best == -1)
						{
							printf("Case #%d: IMPOSSIBLE\n", t);
							goto endLoop;
						}
						
						bool done = false;
						for(int j = i - 1; j > 0; j--)
						{
							if(valid(buf[i], buf[j - 1]) && valid(buf[i], buf[j]))
							{
								int tmp = buf[i];
								done = true;
								for(int k = i; k > j; k--)
									buf[k] = buf[k - 1];
								buf[j] = tmp;
								break;
							}
						}
						
						// int counter = 0;
						// while(counter <= N && !valid(buf[N - 1], buf[N - 2]) || !valid(buf[N - 1], buf[0]))
						// {
						// 	counter++;
						// 	for(int j = N - 2; j > 0; j--)
						// 	{
						// 		if(valid(buf[N - 1], buf[i - 1]) && valid(buf[N - 1], buf[i]))
						// 		{
						// 			int tmp = buf[N - 1];
						// 			for(int k = N - 1; k > i; k--)
						// 				buf[k] = buf[k - 1];
						// 			buf[i] = tmp;
						// 			break;
						// 		}
						// 	}
						// }
						
						if(!done)
						{
							printf("Case #%d: IMPOSSIBLE\n", t);
							goto endLoop;
						}
					}
				}
			}
			// secondary
			else
			{
				if(count[otherColor(buf[i - 1])] <= 0)
				{
					printf("Case #%d: IMPOSSIBLE\n", t);
					goto endLoop;
				}
				else
				{
					buf[i] = otherColor(buf[i - 1]);
					count[buf[i]]--;
				}
			}
			
		}
		
		if(!valid(buf[N - 1], buf[0]) || !valid(buf[N - 2], buf[N - 1]))
		{
			printf("Case #%d: IMPOSSIBLE\n", t);
			goto endLoop;
		}
		
		printf("Case #%d: ", t);
		for(int i = 0; i < N; i++)
			putchar(intToColor[buf[i]]);
		putchar('\n');
		
endLoop:;
	}
}
