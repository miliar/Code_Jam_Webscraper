#include<cstdio>

int n, a, b;
int Heap[2001000], size;
void swap(int &a, int &b){int c = a; a = b; b = c;}

void Up(int p)
{
	if (p == 1 || Heap[p] <= Heap[p >> 1]) return;
	swap(Heap[p], Heap[p >> 1]);
	Up(p >> 1);
}

void Down(int p)
{
	int son = p * 2;
	if (son > size) return;
	if (son < size && Heap[son] < Heap[son + 1]) son++;
	if (Heap[p] >= Heap[son]) return;
	swap(Heap[p], Heap[son]);
	Down(son);
}

int main()
{
//	freopen("C.in", "r", stdin);
//	freopen("C.out", "w", stdout);
	scanf("%d", &n);
	for (int I = 1; I <= n; I++)
	{
		scanf("%d%d", &a, &b);
		size = 1;
		Heap[1] = a;
		for (int i = 1; i < b; i++)
		{
			int x, y;
			if (Heap[1] == 1)
			{
				Heap[1] = Heap[size--];
				Down(1);
				continue;
			}
			x = Heap[1] / 2;
			y = Heap[1] - x - 1;
			Heap[1] = x;
			Down(1);
			if (!y) continue;
			Heap[++size] = y;
			Up(y);
		}
		int x, y;
		x = Heap[1] / 2;
		y = Heap[1] - x - 1;
		if (x < y) swap(x, y);
		printf("Case #%d: %d %d\n", I, x, y);
	}
	return 0;
}
