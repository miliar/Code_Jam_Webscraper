#include <stdio.h>

#define lo long long

lo t,n;
lo tab[110];
lo Bigind(lo bb, lo aa)
{
	lo simMax=-10, indMax=-1;
	for (lo j=bb;j<aa;j++)
	{
		if (tab[j]>=simMax) {simMax=tab[j]; indMax=j;}
	}

	return indMax;
}
int main()
{
	scanf("%lld",&t);
	for  (lo i=1;i<=t;i++)
	{
		scanf("%lld",&n);

		lo po=0;
		while(n>0)
		{
			tab[po]=n%10;
			n=n/10;
			po++;
		}

		lo bawah=0, atas=po; //atas eksklusif
		lo sim=Bigind(bawah,atas);
		while(sim!=-1)
		{
			bool cek=1;
			for (lo j=bawah;j<atas-1;j++)
			{
				if (tab[j]<tab[j+1]) {cek=0; break;}
			}
			
			if (cek) break;
		
			if (sim==bawah)
			{
				bawah++;
			}else
			{
				tab[sim]--;
				for  (lo j=sim-1;j>-1;j--)
				{
					tab[j]=9;
				}
	
				lo no=sim;
				while(tab[no]<0)
				{
					tab[no]=tab[no]+10;
					no++;
					tab[no]--;
				}
	
				atas=po;
				bawah=sim;
			}
			sim=Bigind(bawah,atas);
			
		}

		printf("Case #%lld: ",i);
		while(tab[po-1]<1) po--;
		for (lo j=po-1;j>-1;j--) printf("%lld",tab[j]);
			printf("\n");
	}
	return 0;
}