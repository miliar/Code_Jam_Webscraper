#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#define s(n) scanf("%d", &n)
#define s2(a,b) scanf("%d %d",&a, &b)
#define ss(n) scanf("%s",n)
#define pb push_back
#define vi vector<int>
using namespace std;
//struct node
//{
//	int k,sp;
//}ar[1002];
//bool comp(node a, node b)
//{
//	return a.k<b.k;
//}
double d,k,s,rest,sp,tmp;
int t,n,T,i;
int main()
{
	freopen("input.in","r",stdin);
	freopen("opx.txt","w",stdout);
	s(T);
	for(t=1;t<=T;t++)
	{
		cin>>d>>n;
		rest=0;
		for(i=0;i<n;i++)
		{
			cin>>k>>sp;
			tmp=d-k;
			tmp=tmp/sp;
			//cout<<tmp<<" ";
			if(tmp>rest)
			rest=tmp;
		}
		rest=d/rest;
		printf("Case #%d: %.6lf\n",t,rest);
	}
	return 0;
}
