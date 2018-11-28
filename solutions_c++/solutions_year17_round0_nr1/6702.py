#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
int main()
{
	 FILE *yyin;
	 FILE *yyout;
	yyin=fopen("A-large.in","r");
	yyout=fopen("output.txt","w");
  int t,k,temp=0,count=0,total=0;
  char s[10000];
  fscanf(yyin,"%d",&t);
  for(int i=0;i<t;i++)
  {total=0;
 fflush(stdin);
fscanf(yyin,"%s",s);
  fscanf(yyin,"%d",&k);
 	for(int j=0;s[j]!='\0';j++)
 	{
 	if(s[j]=='-')
	 {
	 	temp=1;
	 	break;
		 }	
	}
	if(temp==0)
	fprintf(yyout,"Case #%d: 0\n",i+1);
	else
	{
		for(int j=0;s[j+(k-1)]!='\0';j++)
 	{count=0;
	 if(s[j]=='-')
	 {total++;
	 	for(int l=j;count<k;l++)
	 	{
	 		count++;
	 		if(s[l]=='+')
	 		s[l]='-';
	 		else
	 		s[l]='+';
		 }
	 }
	 	
 	}
 	temp=0;
 	for(int j=0;s[j]!='\0';j++)
 	{
 		if(s[j]=='-')
	 {
	 	temp=1;
	 	break;
 	}
 }
 		if(temp==0)
	fprintf(yyout,"Case #%d: %d\n",i+1,total);
else
	fprintf(yyout,"Case #%d: IMPOSSIBLE\n",i+1);
	}
  }
  getch();
  return 0;
}
