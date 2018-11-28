#include <iostream>
#include<math.h>
#include <fstream>
#include<algorithm>

using namespace std;
bool sol(long long x)
{
	int a[20];
	long long int t;
	int i,j;
	for(i=0;i<20;i++)
	{
		a[i]=0;
	}
	t=x;i=0;
	while(t!=0)
	{
		a[i++]=t%10;
		t=t/10;
	}
	for(j=0;j<i-1;j++)
	{
		if(a[j]<a[j+1])
			return false;
	}
	return true;
}

int main() {
	ofstream out("out1.txt");
	ifstream in("input1.txt");
	long long int n,i,counter=1,p;
	in>>p;
	while(p--){
	in>>n;
	//cout<<sol(n);/*
	for(i=n;i>=1;i--)
	{
		if(sol(i))
		break;
	}
	out<<"Case #"<<counter++<<": "<<i<<endl;}

	return 0;
}