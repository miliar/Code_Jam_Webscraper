// JBC
# include <fstream.h>
# include <stdio.h>
# include <conio.h>
# include <limits.h>
ifstream fin("small.in");
ofstream fout("output.txt");
void main()
{
 clrscr();
 int T=1;
 long int N,num,org,j;
 int i,flag=0,dig,fd;
  while(fin)
 {
  fin>>N;
  for(j=1; j<=N; ++j)
  {
     org=j;
     fd=INT_MAX;
     while(org!=0)
     {
      dig=org%10;
	if(fd>=dig)
	  {
	   flag=0;
	   fd=dig;
	   }
	 else
	  {
	   flag=1;
	   break;
	   }
       org/=10;
      }
     if(flag==0)
	 num=j;
      }
     cout<<"Case #"<<T<<": "<<num<<"\n";
     fout<<"Case #"<<T<<": "<<num<<"\n";
     ++T;
   }
 getch();
}