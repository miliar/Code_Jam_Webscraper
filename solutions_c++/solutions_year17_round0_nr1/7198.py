#include <iostream>
#include<bits/stdc++.h>
#include<vector>
#include<math.h>
using namespace std;
int main()
{
int k2,i3,f1,f,i2,j2,ans,mn,w,a1,l,i,k,t,x,c,j;
string s;
scanf("%d",&t);
x=1;
while(t--)
{
a1=0;
cin>>s>>k;
mn=0;
int imp=0;
l=s.size();
for(i=0;i<l;i++)
{
if(s[i]=='-')
mn++;
}
i=0;
while(i<l && s[i]=='+')
i++;
j=l-1;
while(j>=0 && s[j]=='+')
j--;
if(i>=j)

{
if(mn)
printf("Case #%d: IMPOSSIBLE",x);
else
printf("Case #%d: 0",x);
printf("\n");
x++;
}







else
{
for(k2=i;k2<=j;k2++)
{
if(s[k2]=='+')
break;
}
if(k2>j)
{
if((j-i+1)%k==0)
{
printf("Case #%d: %d",x,(j-i+1)/k);
x++;
printf("\n");
}
else{
printf("Case #%d: IMPOSSIBLE",x);
x++;
printf("\n");
}

}

else{
while(i<j){
i2=i;
j2=j;

w=i;
f=0;
f1=0;
while(w<=i2+k-1 && w<=j)
{
if(s[w]=='+' && !f)
{i=w;
f=1;
}

s[w]=(s[w]=='-')?'+':'-';
w++;
f1=1;
}
if(f1)
a1++;
while(i<l &&  i<=j  && s[i]=='+')
i++;
if(i>j || i>=l)
break;
c=0;
i3=i;

for(;i3<=j;i3++)
{
if(s[i3]=='+')
break;
c++;

}

if(i3>j)
{if(c%k)
{imp=1;
break;
}
else
{
a1+=(c/k);
break;

}
}
i2=i;
w=j;
f=0;
f1=0;

while(w>=j2-k+1 && w>=i)
{
if(s[w]=='+' && !f)
{j=w;
f=1;
}

s[w]=(s[w]=='-')?'+':'-';
w--;
f1=1;

}
if(f1)
a1++;
while(j>=0  && j>=i && s[j]=='+')
j--;
j2=j;


if(i>j || i>=l)
{
break;
}
for(w=i;w<=j;w++)
{
if(s[w]=='+')
break;

}
c=0;
i3=i;

for(;i3<=j;i3++)
{
if(s[i3]=='+')
break;
c++;

}


if(i3>j)
{if(c%k)
{imp=1;
break;
}
else
{
a1+=(c/k);
break;

}
}
if(j-i<k)
{
a1=0;
imp=1;
break;
}



}

if(!imp)
printf("Case #%d: %d",x,a1);
else
printf("Case #%d: IMPOSSIBLE",x);
printf("\n");
	 x++;
}

}

}
	return 0;
}

