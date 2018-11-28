#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int t;
char A[1005];
int len;
char lasts;
main()
{
 freopen("B-large.in","r",stdin);
 freopen("B-large.out","w",stdout);
 scanf("%d\n",&t);
 for(int tests=1;tests<=t;tests++)
 {
  gets(A);
  len=strlen(A);
  lasts='0';
  //printf("%d",len);
  for(int i=0;i<len;i++)
  {
   if(A[i]<lasts)
   {
   	A[i-1]--;
   	for(int j=i;j<len;j++)
   	{
	 A[j]='9';
	}
   	for(int j=i-1;j>0;j--)
   	{
	 if(A[j]>=A[j-1]){break;}
	 else{A[j]='9';A[j-1]--;}
	}
	break;
   }
   else
   {
   	lasts=A[i];
   }
  }
  printf("Case #%d: ",tests);
  for(int i=0;i<len;i++)
  {
   if(A[i]!='0')
   {
   	for(int j=i;j<len;j++)
   	{
	   printf("%c",A[j]);
	}
   	break;
   }
  }
  printf("\n");
 }
  return 0;
}


