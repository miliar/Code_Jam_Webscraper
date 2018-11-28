#include<bits/stdc++.h>
using namespace std;
char a[12];
char b[12];
int n;
int k;
char str1[12];
map < string , int> dp;
int arr[1006];
int cooo=0;
int f(int ind,int arr[12])
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
		//xx+=(char)(arr[i]+48);
	}
	str1[h]='\0';
	string xx(str1);
	if(xx=="")
	return 0;
	int ret=dp[xx];
	if(ret!=0)
	return ret;
	ret=INT_MAX;
	//for(int i=0;i<a.size();i++)
	//printf("%d ",arr[i]);
	///printf("\n");
	if(arr[ind]==0)
	{
		ret=f(ind+1,arr);
		dp[xx]=ret;
		return ret;
	}
	int brr[50];
	
	
	//for(int i=0;i<a.size();i++)
	//brr[i]=arr[i];
	for(int i=k-1;i<=k-1;i++)
	{
		for(int j=0;j<n;j++)
		brr[j]=arr[j];
		int x=brr[ind];
		if(ind+i>=n)
		break;
		for(int j=ind;j<=ind+i;j++)
		{
			brr[j]=brr[j]-x;
			if(brr[j]<0)
			brr[j]+=2;
		}
		int xx=f(ind+1,brr);
		if(xx!=INT_MAX)
		ret=min(ret,1+xx);
	}
	dp[xx]=ret;
	return ret;
}
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
int t;
scanf("%d",&t);
int cs=1;
while(t--){
	dp.clear();
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
		printf("Case #%d: ",cs++);
		printf("0\n");
		continue;
	}
	n=l;
	for(i=0;i<l;i++)
	{
		arr[i]=abs(a[i]-b[i]);
	}
	//for(i=0;i<=1000000;i++)
	//dp[i]=-1;
	int answ=f(0,arr);
	//for(i=0;i<n;i++)
	//printf("%d ",dp[i]);
	//printf("\n");
	printf("Case #%d: ",cs++);
	if(answ==INT_MAX)
	printf("IMPOSSIBLE\n");
	else
	printf("%d\n",answ);
}
	return 0;
}

