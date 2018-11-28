#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cmath>

using namespace std;

struct Inter
{
	int quel, paquet, pos, isEnd;
	
	Inter() { }
	Inter(int a, int b, int c, int d) : quel(a), paquet(b), pos(c), isEnd(d) { }
	
	bool operator < (const Inter& autre) const
	{
		if(pos == autre.pos)
		{
			return isEnd < autre.isEnd;
		}
		return pos < autre.pos;
	}
};

int main()
{
	int T;
	scanf("%d", &T);
	
	for(int t = 1; t<=T; t++)
	{	
		int N,P;
		vector<Inter> event;
		int requis[51];
		scanf("%d%d", &N, &P);
		
		for(int i= 0; i < N; i++)
		{
			scanf("%d", &requis[i]);
		}
		
		for(int i = 0;i < N; i++)
		{
			for(int j = 0; j < P; j++)
			{
				int y;
				scanf("%d", &y);
				double yy = (double)y;
				double x = (double)(requis[i]);
				int maxi = (int)(yy/(0.9 * x));
				int mini = (int)(ceil(yy/(1.1 * x)));
				
				//printf("debug : %d et %d\n", mini, maxi);
				
				if(maxi >= mini){
				event.push_back(Inter(i,j,mini,0));
				event.push_back(Inter(i,j,maxi,1));
				}
			}
		}
		sort(event.begin(), event.end());
		
		int nbDone=0;
		int toIgn[60];
		int nbDispo[60];
		
		for(int i= 0; i < N; i++)
			toIgn[i]=nbDispo[i]=0;
		
		for(int i = event.size()-1; i >= 0; i--)
		{
			if(event[i].isEnd==1)
				nbDispo[event[i].quel]++;
			bool toutDispo=true;
			for(int j = 0; j < N; j++)
			{
				if(nbDispo[j] == 0)
					toutDispo=false;
			}
			if(toutDispo)
			{
				for(int j=0; j < N; j++)
				{
					nbDispo[j]--;
					toIgn[j]++;
				}
				nbDone++;
				//nbDone+=event[i].pos;
			}
			if(event[i].isEnd==0)
			{
				if(toIgn[event[i].quel] > 0)
					toIgn[event[i].quel]--;
				else
					nbDispo[event[i].quel]--;
			}
		}
		printf("Case #%d: %d\n", t, nbDone);
	}
	
	return 0;
}

