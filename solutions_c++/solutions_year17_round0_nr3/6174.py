#include<bits/stdc++.h>

using namespace std;

int poweroftwo(unsigned long long int n)
{
  if (n == 0)
    return 0;
  while (n != 1)
  {
    if (n%2 != 0)
      return 0;
    n = n/2;
  }
  return 1;
}
unsigned long long int hp2(unsigned long long int n)
{
	if(poweroftwo(n))
	return n;
	unsigned long long int x=ceil(log10(n)/log10(2));
	return 1<<(x-1);
}
unsigned long long int level(unsigned long long int n)
{
	//cout<<log10(n)<<endl;
	if(n==1)
	return 0;
	else
	
	return floor(log10(n)/log10(2));
}

int main()
{	FILE *fp = fopen("output.txt" , "w+");
	int t,i;
	cin>>t;
	for(i=0;i<50;i++)
		i++;
	for(i=1;i<=t;i++){
	
	unsigned long long int a,b;
	unsigned long long int n,k;
	cin>>n>>k;
	//cout<<"Case #"<<t<<": ";
	unsigned long long int x=level(k)+1;//cout<<x<<endl;
	unsigned long long int sum=n-(1<<(x-1))+1;//cout<<sum<<endl;
	unsigned long long int base=hp2(k);//cout<<base<<endl;
	a=sum%base;
	b=sum/base;
	unsigned long long int off = k-base+1;//cout<<off<<endl;
	if(off<= a)
	b+=1;
	//cout<<b/2<<" "<<(b-1)/2<<endl;
	fprintf(fp , "Case #%d: %llu %llu\n" , i , b/2,(b-1)/2);}
	return 0;
}

