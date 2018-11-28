#include<cstdio>
#include<cstring>
#include<queue>
using namespace std;
int D[101][201][101][101];
struct LIST
{
	int x, y, z, a;
	LIST(int x_, int y_, int z_, int a_) : x(x_), y(y_), z(z_), a(a_)
	{}
};
int Ans = -1;
int MAX;
queue<LIST> q;
void Attack(int x, int y, int z, int a, int v)
{
	if(z < 0) z = 0;
	if(a < 0) a = 0;
	if(z == 0)
	{
		Ans = v;
		return;
	}
	x -= a;
	if(x <= 0) return;
	if(200 < y) return;
	if(D[x][y][z][a] != MAX) return;
	q.push(LIST(x, y, z, a));
	D[x][y][z][a] = v;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		int Hd, Ad, Hk, Ak, b, d;
		scanf("%d %d %D %d %d %d", &Hd, &Ad, &Hk, &Ak, &b, &d);
		memset(D, 12, sizeof(D));
		MAX = D[0][0][0][0];
		while(!q.empty()) q.pop();
		q.push(LIST(Hd, Ad, Hk, Ak));
		D[Hd][Ad][Hk][Ak] = 0;
		Ans = -1;
		while(!q.empty() && Ans == -1)
		{
			LIST head = q.front();
			q.pop();
			int health = head.x;
			int attack = head.y;
			int opphealth = head.z;
			int oppattack = head.a;
			int v = D[health][attack][opphealth][oppattack] + 1;
			Attack(health, attack, opphealth - attack, oppattack, v);
			Attack(health, attack + b, opphealth, oppattack, v);
			Attack(Hd, attack, opphealth, oppattack, v);
			Attack(health, attack, opphealth, oppattack - d, v);
		}
		printf("Case #%d: ", t);
		if(Ans == -1) printf("IMPOSSIBLE");
		else printf("%d", Ans);
		printf("\n");
	}
}