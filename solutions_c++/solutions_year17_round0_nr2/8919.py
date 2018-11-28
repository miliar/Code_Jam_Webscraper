#include <bits/stdc++.h>
using namespace std;

int valid(string s)
{
int i;
int ans=1;
for(i=1;i<s.length();i++)
{
if(s[i]<s[i-1])
{
	ans=0;
	break;
}

return ans;

}



}



int main()
{
	
int t,i;
cin>>t;
int val=1;

string s,s1,s3,s2;
while(t--)
{

	cin>>s1;
	s2="9";
	s3="0";
	int j;
	s=s3+s1+s2;
int l=s.length();


//cout<<s<<"\n";
//for(i=2;i<4;i++)
//s[i]='9';
//cout<<s;

	//cout<<l;
for(i=l-2;i>=0;i--)
{
if(s[i]>s[i+1])
{
s[i]--;
for(j=i+1;j<=l-1;j++)
{
	s[j]='9';
}


}


}

cout<<"Case #"<<val<<": ";
for(i=1;i<l-1;i++)
{
if(s[i]!='0')
cout<<s[i];
}
val++;
cout<<"\n";
}	







}