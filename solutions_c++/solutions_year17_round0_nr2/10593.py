#include<iostream>
#include<fstream>

using namespace std;
int main()
{
 ifstream in;
 in.open("input.in");

 ofstream out("output.txt");


 int T;
 in>>T;

 int a,l;
 int ch=1,o;
 for(int i=0;i<T;i++)
 {
  in>>a;ch=1;
  while(ch==1)
  {
	int c=0,r[20];
	l=a;
	while(l>0)
	{
	  r[c]=l%10;
	  l=l/10;
	  c++;
	}
      if(c==1)
      {ch=0;}
      if(c!=1)
	for(int j=0;j<c;j++)
	{
		for(int k=c-1;k>j;k--)
		{
		       if(r[j]>=r[k])
			{ch=0;}
			else
			{ch=1;break;}
		}
		if(ch==1)
		break;
	}
	if(ch==1)
	{a=a-1;}

  }


    out<<"Case #"<<i+1<<": "<<a<<"\n";
 }
 in.close();
 out.close();
 return 0;
}
