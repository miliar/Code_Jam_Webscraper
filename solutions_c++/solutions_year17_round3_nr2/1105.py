#include<cstdio>
#include<algorithm>

using namespace std;

struct act
{
	int b, e;
	bool jamie;
};

bool comp(act &a1, act &a2)
{
	return a1.b < a2.b;
}
	
int main()
{
	int t;
	scanf("%d", &t);
	for(int tt = 1; tt <= t; tt++)
	{
		int ac, aj;
		scanf("%d %d", &ac, &aj);
		int tab[1441];
		for(int i = 0; i < 1441; i++)
			tab[i] = 0;
		
		vector<act> v;
		vector<act> c;
		vector<act> j;
		int cTime = 0, jTime = 0;
		for(int i = 0; i < ac; i++)
		{
			act a;
			scanf("%d %d", &a.b, &a.e);
			a.jamie = false;
			v.push_back(a);
			c.push_back(a);
			jTime += a.e-a.b;
		}
		
		for(int i = 0; i < aj; i++)
		{
			act a;
			scanf("%d %d", &a.b, &a.e);
			a.jamie = true;
			v.push_back(a);
			j.push_back(a);
			cTime += a.e-a.b;
		}
		
		sort(v.begin(), v.end(), comp);
		
		printf("Case #%d: ", tt);
		if(ac <= 1 && aj <= 1)
			printf("2\n");
		else
		{
			if(v[1].e - v[0].b > 720 && v[0].e + 1440 - v[1].b > 720)
				printf("4\n");
			else
				printf("2\n");
		}
	}
	return 0;
}

