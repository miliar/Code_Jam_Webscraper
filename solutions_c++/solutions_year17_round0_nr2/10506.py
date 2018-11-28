#include<iostream.h>
#include<fstream.h>
#include<conio.h>
int findtidy(int x)
{
   int t1,t2,flag=0;
	while(x!=0)
	{
	   t1=x%10;
	   x=x/10;
	   t2=x%10;
	   if(t2>t1)
	   {
	   flag=1;
	   break;
	   }
	}
	if(flag==1)
	return 0;
	return 1;
}

void main()
{
	ofstream out;
	ifstream in;
	out.open("output4.txt");
	in.open("sample1.txt");
	int s,i,j,t=0,count=1;
	clrscr();
	in>>t;
	int n[100];
	for(i=0;i<t;i++)
	in>>n[i];
	for(i=0;i<t;i++)
	{
	   for(j=n[i];j>0;j--)
	   {
	       s=findtidy(j);
	       if(s==1)
	       {
	       out<<"case #"<<count<<":"<<" "<<j<<endl;
	       count++;
	       break;
	       }
	   }
	}
	in.close();
	out.close();
}