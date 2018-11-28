#include <iostream>
#include<bits/stdc++.h>
#include<vector>
#include<math.h>
using namespace std;

int main()
{
	int c,i2,j2,r,i,l,pre,p,d1,k,j,t,n;
char x,a[30][30],s2[30];

scanf("%d",&t);
int x1=1;
while(t--)
{
scanf("%d %d",&r,&c);
for(i=0;i<r;i++)
{

scanf("%s",s2);


for(j=0;j<c;j++)
a[i][j]=s2[j];
}




int f=0;

for(i=0;i<r;i++)
{
x='#';

for(j=0;j<c;j++)

{
if(a[i][j]!='?')
x=a[i][j];
else{
if(x!='#')
a[i][j]=x;





}





}



}









for(i=0;i<r;i++)
{
x='#';

for(j=c-1;j>=0;j--)

{
if(a[i][j]!='?')
x=a[i][j];
else{
if(x!='#')
a[i][j]=x;





}





}



}












for(j=0;j<c;j++)
{
x='#';

for(i=0;i<r;i++)

{
if(a[i][j]!='?')
x=a[i][j];
else{
if(x!='#')
a[i][j]=x;





}





}



}




for(j=0;j<c;j++)
{
x='#';

for(i=r-1;i>=0;i--)

{
if(a[i][j]!='?')
x=a[i][j];
else{
if(x!='#')
a[i][j]=x;





}





}



}





printf("Case #%d:",x1);
printf("\n");



for(i=0;i<r;i++)
{
{
for(j=0;j<c;j++)
cout<<a[i][j];
}
cout<<"\n";
}

	    
x1++;

}
	return 0;
}

