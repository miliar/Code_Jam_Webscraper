#include<stdio.h>
#include<string.h>
#include<conio.h>
void main()
{
clrscr();
  remove("output.txt");
  freopen("sample.txt","r",stdin);
  freopen("output.txt","w",stdout);

int check(int n,int ten);
int detten(int n);
 int n,ten;
 int T,i,j,k,chek,lt;

  scanf("%d",&T);
   for(i=1;i<=T;i++)
    {
      scanf("%d",&n);
      lt=0;
      do
      {
       ten=detten(n);
       chek=check(n,ten);
	if(chek==1)
	 {
	  lt++;
	 }
	else
	 {
	  n--;
	 }
       getch();
      }while(lt==0);
     printf("Case #%d: %d\n",i,n);
    }
 getch();
}
int detten(int n)
{
 int ten=1;
int rem;
      do{
      ten=ten*10;
      rem=n/ten;
      }while(rem!=0);
      ten=ten/10;
 return ten;
}
int check(int n,int ten)
{
  int bre=0,temp,num;
  int i;
  temp=n/ten;
  for(i=ten/10;i>=1;i=i/10)
   {
     num=n/i;
     num=num%10;
     if(temp<=num)
      {temp=num;}
     else
      {bre++;break;}
   }
 if(bre==0)
  return 1;
 else
  return 0;
}