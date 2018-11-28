#include<stdio.h>
#include<string.h>
#include<conio.h>
void main()
{
clrscr();
  remove("output.txt");
  freopen("sample.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int T,n,in,p,i,k,j,fi=0,ff=0,l,r,mp;
  char s[1002];

 scanf("%d",&T);
  for(i=1;i<=T;i++)
  {
    scanf("%d %d ",&in,&p);
    n=in+2;
    s[0]='o';s[n-1]='o';
    for(j=1;j<(n-1);j++)
     s[j]='.';

    for(j=1;j<=p;j++)
     {
       fi=0;ff=0;
       int ip=0,fp=0,lar=0;
	do
	 {
	   do
	    {
	     fp++;
	    }while(s[fp]=='.');

	    if((fp-ip)>lar)
	     {
	      lar=fp-ip;
	       fi=ip;
		ff=fp;
		 ip=fp;
	     }
	    else
	     {
		ip=fp;
	     }

	   }while(ip!=(n-1));
	 mp=(lar/2)+fi;
	 s[mp]='o';
       l=0,r=0;
       if(j==p)
	{
	  for(k=mp-1;k>=0;k--)
	   {
	     if(s[k]=='o')
	     {
	      break;
	     }
	     else l++;
	   }

	  for(k=mp+1;k<=(n-1);k++)
	   {
	     if(s[k]=='o')
	     {
	      break;
	     }
	     else r++;
	   }

	 printf("Case #%d: %d %d\n",i,r,l);
	}
     }
  }
getch();
}
