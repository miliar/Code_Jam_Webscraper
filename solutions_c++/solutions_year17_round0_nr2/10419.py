/*
 * codi2.cpp
 *
 *  Created on: 08-Apr-2017
 *      Author: pratik
 */
#include<iostream>

int ar[20],j,fl=1,ct=1,t;
int n;
using namespace std;

void dig(int a,int i)
{ if (a==0)
{

	return;
} j=i;
  int c;
  c = a % 10;
  ar[i]=c;
  dig(a/10,i+1);
}

void tst(int xn)
{
 int yz=xn;
 dig(yz,0);
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
    	  cout<<"Case #"<<ct<<": "<<yz<<"\n";
    	  return;
    	  }
 else
	 tst(yz-1);

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



