#include <cstdlib>
#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	
	for(int t = 1; t<= T; t++)
	{
		long long nb;
		scanf("%lld", &nb);
		int tab[20];
		
		int N=0;
		long long cp = nb;
		while(cp > 0)
		{
			tab[N]=cp%10;
			N++;
			cp/=10;
		}
		
		int rtab[20];
		for(int i= 0; i < N; i++)
			rtab[N-1-i]=tab[i];
		
		long long maxi=0;
		for(int i = 1; i < N; i++)
			maxi=maxi*10+9;
		
		bool ok=true;
		for(int i = 1; i < N; i++)
		{
			if(tab[i-1]<tab[i])
				ok=false;
		}
		if(ok)
			maxi=nb;
		
		for(int i = 0; i < N; i++)
		{
			if((i>0&&rtab[i]<=rtab[i-1]))
				break;
			if((i==0 && rtab[i]==1) || rtab[i]==0)
				continue;
			long long curr = 0;
			for(int j = 0; j < i; j++)
				curr = 10*curr+rtab[j];
			curr = 10*curr + (rtab[i]-1);
			for(int j = i+1; j < N; j++)
				curr = 10*curr + 9;
			if(curr > maxi)
				maxi=curr;
			//hypo : strict plus petit en i, 9..9 après, id avant
		}
		
		printf("Case #%d: %lld\n", t, maxi);
	}
	
	return 0;
}

