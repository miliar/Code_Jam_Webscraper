#include<iostream>
#include<string>
using namespace std;
string in;
char out[25];
bool found,les;
int len;
void func(int par,int idx)
{
	if(idx==len)
	{
		found=1;
		return;
	}
	if(found) return;
	int start=in[idx]-48;
	if(les) start=9;
	for(int i=start;i>=par;i--)
	{
		if(!les&&i<in[idx]-48) les=1;
		out[idx]=i+48;
		func(i,idx+1);
		if(found) return;
	}
}
int main()
{
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,cas=1;
	cin>>T;
	while(T--)
	{
		found=0,les=0;
		cin>>in;
		len=in.length();
		if(len==1)
		{
			cout<<"Case #"<<cas<<": "<<in<<'\n';
			cas++;
			continue;
		}
		func(1,0);
		if(found)
		{
			cout<<"Case #"<<cas<<": ";
			for(int i=0;i<len;i++) cout<<out[i];
			cout<<'\n';
		}
		else
		{
			cout<<"Case #"<<cas<<": ";
			for(int i=0;i<len-1;i++) cout<<9;
			cout<<'\n';
		}
		cas++;
	}
}
