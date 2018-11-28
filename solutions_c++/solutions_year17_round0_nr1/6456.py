#include<stdio.h>
int main(void)
{
int t,i;
scanf("%d",&t);

  for(i=0;i<t;i++)
  {
    int n,j,k;
    int c=0;
    char a[1001];
    scanf("%s%d",a,&n);
    //printf("%d",n);
    //printf("%sfan\n",a);
int flag=1;

    for(j=0;a[j]!='\0';++j);
  //  printf("%d  ",j);
  for(k=0;k<j-n+1;k++)
  {
  int ch=0;
  if(a[k]=='-')
  {while(ch<n)
    {
    if(a[ch+k]=='-')
    a[ch+k]='+';
    else a[ch+k]='-';
    ++ch;

  } ++c;}


  }
//  printf("  %s  ",a);
  for(k=0;k<j;k++)
  {
//printf("    hi   ");
  if(a[k]=='-'){flag=0;break;}
  }
//  printf(" %df  ",flag);
  if (flag==0) printf("Case #%d: IMPOSSIBLE\n",i+1);
  else printf("Case #%d: %d\n",i+1,c);
}
  return 0;
  }
