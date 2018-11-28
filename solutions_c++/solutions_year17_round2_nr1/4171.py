#include<bits/stdc++.h>
//#include<stdio.h>
//#include<conio.h>
int main()
{
   int T,N,i,j,nd;
    double D;
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
	double annie;
       double tmax=0;
       double K[1000],S[1000];
	double  t[1000];
	scanf("%lf %d",&D,&N);
	for(j=1;j<=N;j++)
	{
	 scanf("%lf %lf",&K[j],&S[j]);
	 nd=D-K[j];
	 t[j]=nd/S[j];
	 if(tmax<t[j])
	 {
	     tmax=t[j];
	 }
	}
	annie=D/tmax;
		printf("Case #%d: %lf\n",i,annie);
    }
//getch();
return 0;


}
