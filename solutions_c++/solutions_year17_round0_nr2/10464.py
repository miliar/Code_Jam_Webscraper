#include<iostream.h>
#include<conio.h>
#include<process.h>
#include<fstream.h>
void main()
{ int c,t,a,i,j,n,k,l;
   clrscr();
   ifstream fin;
   fin.open("Bcc.in",ios::in);
   ofstream fout;
   fout.open("SL.in",ios::out);
   fin>>t;
   if(t>100)
   exit(1);
   for(i=1;i<=t;i++)
  { fin>>n;
   if(n>1000)
   exit(1);
   for(a=n;a>0;a--)
   {j=a;
     while(j>0)
     {l=j%10;
      j=j/10;
      k=j%10;
      if(k>l)
      break;
     }
     if(j==0)

    { fout<<"Case #"<<i<<":"<<" "<<a<<"\n";
     break;}
    }
   }
 }