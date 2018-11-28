#include<iostream>
using namespace std;
void sort (int f);

int h[5000];
int main()
{
int a,b,c,d,e,f=1,g,min,max,el=0,tem;
int z;
cin>>a;
for(b=0;b<a;b++)
{
el=0;
f=1;
cin>>c>>d;
h[el]=c;
for(e=0;e<(d-1);e++)
{
if(h[el]%2==0)
{
tem=h[el];
h[f]=tem/2;
f++;
if(tem>1)
{
h[f]=(tem/2)-1;
}
else
{
h[f]=tem/2;
}
f++;
el++;
sort(f);
}
else if(h[el]%2!=0)
{
tem=h[el];
h[f]=tem/2;
f++;
h[f]=tem/2;
f++;
el++;
sort(f);
}
}
if(h[el]%2==0)
{
if(h[el]>1)
{
min=(h[el]/2)-1;
}
else
{
min=h[el]/2;
}
max=(h[el]/2);
}
else if(h[el]%2!=0)
{
min=(h[el]/2);
max=(h[el]/2);
}
cout<<"case #"<<b+1<<": "<<max<<"  "<<min<<endl;
}
return 0;
}


void sort(int f)
{
f--;
unsigned long long int a,b,c;
for(a=0;a<f;a++)
{
for(b=a;b<f;b++)
{
if(h[b]<h[b+1])
{
c=h[b];
h[b]=h[b+1];
h[b+1]=c;
}
}
}
}