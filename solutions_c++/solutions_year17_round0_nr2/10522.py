#include<iostream>

int ar[20],j,fl=1,ct=1,t;
long long n;
using namespace std;

void dig(long long a,int i)
{ if (a==0)
{

	return;
} j=i;
  int c;
  c = a % 10;
  ar[i]=c;
  dig(a/10,i+1);
}

void tst(long long xn)
{
 dig(xn,0);
 fl=1;
 for(int x=0;x<j;x++)
 {
	 if(x==0)
	 {if(ar[x]<ar[x+1])  {fl=0; break;}}
 else
	 {if(ar[x-1]<ar[x]||ar[x]<ar[x+1])  {fl=0; break;}}

 }
 if(fl==1)
    	  {
    	  cout<<"Case #"<<ct<<": "<<xn<<"\n";
    	  return;
    	  }
 else
	 tst(xn-1);

}

void inp(int e)
{
	if(e==0)
		return;

  	cin>>n;
    tst(n);

    ct=ct+1;
    //refsh();
    inp(e-1);
}


int main()
{
  cin>>t;
  inp(t);
  return 0;

}



