#include<iostream>
#include<algorithm>
using namespace std;

long long a,b,aa,bb,ans1,ans2,ans110,ans15,ans12,ans11,ans210,ans25,ans22,ans21;

int check(int a,int b)
{
	long long aa,bb,ans1,ans2,ans110,ans15,ans12,ans11,ans210,ans25,ans22,ans21;
	aa=bb=ans1=ans2=ans110=ans15=ans12=ans11=ans210=ans25=ans22=ans21=0;
	aa=a,bb=b;
	if(a<0||b<0)
		return 10000;
	ans110+=a/10;
	a%=10;
	ans15+=a/5;
	a%=5;
	ans12+=a/2;
	a%=2;
	ans11+=a;
	ans210+=b/10;
	b%=10;
	ans25+=b/5;
	b%=5;
	ans22+=b/2;
	b%=2;
	ans21+=b;
	ans1=max(ans110,ans210)+max(ans15,ans25)+max(ans12,ans22)+max(ans11,ans21);
	ans2=ans110+ans15+ans11+ans12;
	bb-=aa;
	ans2+=bb/10;
	bb%=10;
	ans2+=bb/5;
	bb%=5;
	ans2+=bb/2;
	bb%=2;
	ans2+=bb;
	return min(ans2,ans1);
}

int main()
{
	cin>>a>>b;
	if(a>b)
		swap(a,b);
	cout<<min(check(a,b),check(a-6,b-14)+4);
	return 0;
}
