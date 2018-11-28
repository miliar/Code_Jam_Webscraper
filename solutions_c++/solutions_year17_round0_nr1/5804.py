#include<bits/stdc++.h>
using namespace std;
char a[1005];
char b[1005];
int n;
int k;
char str1[1005];
int arr[1006];
int cooo=0;
int f(int ind)
{
	if(ind==n)
	return 0;
	cooo++;
	int j=ind;
	int h=0;
	int kk=n-1;
	while(1)
	{
		if(j==n)
		break;
		if(arr[j]!=0)
		break;
		j++;
	}
	while(1)
	{
		if(kk==ind-1)
		break;
		if(arr[kk]!=0)
		break;
		kk--;
	}
	for(int i=j;i<=kk;i++)
	{
		str1[h++]=arr[i]+48;
		
	}
	str1[h]='\0';
	string xx(str1);
	if(xx=="")
	return 0;
	int ret=INT_MAX;
	
	if(arr[ind]==0)
	{
		ret=f(ind+1);
		return ret;
	}

	for(int i=k-1;i<=k-1;i++)
	{
		int x=arr[ind];
		if(ind+i>=n)
		break;
		for(int j=ind;j<=ind+i;j++)
		{
			arr[j]=arr[j]-x;
			if(arr[j]<0)
			arr[j]+=2;
		}
		int xx=f(ind+1);
		if(xx!=INT_MAX)
		ret=min(ret,1+xx);
	}
	return ret;
}
int main()
{
freopen("A-small-attempt0.in","r",stdin);
freopen("output.txt","w",stdout);
int t;
scanf("%d",&t);
int cas=1;
while(t--){
	scanf("%s",a);
	scanf("%d",&k);
	int i,j=0;
	int l=strlen(a);
	for(i=0;i<l;i++)
	{
		if(a[i]=='+')
		a[i]='1';
		else
		a[i]='0';
		b[j++]='1';
	}
	b[j]='\0';
	if(strcmp(a,b)==0)
	{
		printf("Case #%d: ",cas++);
		printf("0\n");
		continue;
	}
	n=l;
	for(i=0;i<l;i++)
	{
		arr[i]=abs(b[i]-a[i]);
	}
	int answ=f(0);
	printf("Case #%d: ",cas++);
	if(answ!=INT_MAX)
	printf("%d\n",answ);
	else
	printf("IMPOSSIBLE\n");
	
}
	return 0;
}

