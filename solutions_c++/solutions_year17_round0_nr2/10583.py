#include<iostream>
#include<fstream>

using namespace std;
int main()
{
 int num,num0,ch=1,T;
 fstream in;
 in.open("B-small-attempt1.in");

 ofstream out("output.txt");
 in>>T;

 for(int i=0;i<T;i++)
 {
  in>>num;ch=1;
  while(ch==1)
  {
	int c=0,r[20];
	num0=num;
	while(num0>0)
	{
	  r[c]=num0%10;
	  num0/=10;
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
	{num=num-1;}

  }


    out<<"Case #"<<i+1<<": "<<num<<"\n";
 }
 in.close();
 out.close();
 return 0;
}

