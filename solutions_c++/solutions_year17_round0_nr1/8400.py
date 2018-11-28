#include<stdio.h>
#include<string.h>
#include<conio.h>
void main()
{
clrscr();
  remove("output.txt");
  freopen("sample.txt","r",stdin);
  freopen("output.txt","w",stdout);

  void apply(char s[],int id,int min);
  int T,min,i,j,k,len,time,tot;
  char s[1000];

  scanf("%d",&T);
   for(i=1;i<=T;i++)
    {
      scanf("%s %d",s,&min);
      len=strlen(s);
       time=0,tot=0;
       for(j=0;j<=(len-min);j++)
	{
	  if(s[j]=='-')
	   {
	     apply(s,j,min);
	     time++;
	   }
	   else;

	}
	   for(k=0;k<len;k++)
	    {
	     if(s[k]=='+')
	      tot++;
	     else;
	    }
	   if(tot==len)
	    printf("Case #%d: %d\n",i,time);
	   else
	    printf("Case #%d: IMPOSSIBLE\n",i);
    }
fclose(stdout);
fclose(stdin);
getch();
}
void apply(char s[],int id,int min)
{
 int i,j,k;
  for(i=id,j=1;j<=min;j++,i++)
   {
     if(s[i]=='+')
      s[i]='-';
     else if(s[i]=='-')
      s[i]='+';
   }
}