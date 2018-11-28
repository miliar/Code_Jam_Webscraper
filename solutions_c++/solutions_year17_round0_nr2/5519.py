#include <bits/stdc++.h>
using namespace std;
int main()
{
  int t,l=1,j;
   string s[105];
   cin>>t;
   while(t--)
   {
   	string in;
   	cin>>in;
   	int i,cnt=0;
   	for(i=in.size()-1;i>=0;i--)
   	{
   		if(i==0)
   			continue;
   		else if((in[i]-'0')<=0)
   		{
   			in[i]='9';
   			int k=in[i-1]-'0';
   			k--;
   			in[i-1]=k+'0';
   		}
   		else if((in[i]-'0')<(in[i-1]-'0'))
   		{
   			in[i]='9';
   			int k=in[i-1]-'0';
   			k--;
   			in[i-1]=k+'0';
   		}
   	} 
   	for(i=0;i<in.size();i++)
   	{
   		if(in[i]=='9')
   			cnt++;
   		else if(in[i]!='9' && cnt)
   		{
   			in[i]='9';
   			cnt++;
   		}
   }
   if(in[0]=='0')
   	in.erase(in.begin()+0);
   	s[l]=in;
   	l++;
   }
   for(j=1;j<l;j++)
   	cout<<"Case #"<<j<<": "<<s[j]<<endl;
}

