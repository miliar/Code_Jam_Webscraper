#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cmath>

using namespace std;

int solve(int nbD, int nbB, int Hd, int Ad, int Hk, int Ak, int B, int D)
{
	int maxiHd = Hd;
	int nbCoups = 0;
	while(Hk > 0)
	{
		//printf("%d\n", Hk);
		if(Hk - Ad <= 0)
			Hk = 0;
		else if((nbD == 0 && Hd - Ak <= 0) || (nbD > 0 && Hd - max(Ak - D,0) <= 0))
		{
			Hd=maxiHd-Ak;
		}
		else if(nbD > 0)
		{
			Ak = max(0,Ak-D);
			Hd -=Ak;
			nbD--;
		}
		else if(nbB > 0)
		{
			Ad += B;
			Hd -= Ak;
			nbB--;
		}
		else
		{
			Hk -= Ad;
			Hd -= Ak;
		}
		
		nbCoups++;
		if(nbCoups > 5000)
			break;
	}
	return Hd > 0 ? nbCoups:5001;
}

int main()
{
	int T;
	scanf("%d", &T);
	
	for(int t = 1; t<=T; t++)
	{
		int Hd, Ad, Hk, Ak, B, D;
		scanf("%d%d%d%d%d%d", &Hd, &Ad, &Hk, &Ak, &B, &D);
		
		printf("Case #%d: ", t);
		
		//Cas particuliers : 
		if(Ad >= Hk) //one shot
		{
			printf("1\n");
			continue;
		}
		//on se fait one shot ou on loop même en prenant un debuff
		/*if(Ak - D >= Hd || (Ak-D)*2 >= Hd) //redondant
		{
			printf("IMPOSSIBLE\n");
			continue;
		}*/
		//dans tous les autres cas, au moins en mettant un debuff on a le temps de se soigner
		
		int meilleur = 99999;
		for(int nbD = 0; nbD <= 100; nbD++)
		{
			//if(nbD==0 && Ak*2 >= Hd) //loop ou oneshot
			//	continue;
			for(int nbB = 0; nbB <= 100; nbB++)
			{
				int nbCoups = solve(nbD, nbB, Hd, Ad, Hk, Ak, B, D);
				
				if(nbCoups < meilleur)
					meilleur=nbCoups;
			}
		}
		
		if(meilleur > 5000)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", meilleur);
	}
	
	return 0;
}

