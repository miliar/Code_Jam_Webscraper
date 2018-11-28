#include<bits/stdc++.h>
using namespace std;
#define ll long long
string s;
void recur(string& s,int pos)
{

if(pos==0)
if(s.size()>1 && s[pos]>s[pos+1])
s[pos]=s[pos]-1;



if(s[pos]<s[pos-1])
{s[pos]=9+48;
s[pos-1]=s[pos-1]-1;
}


if(pos>0)
recur(s,pos-1);
//cout << s[pos]<<" " ;
}





int main()
{freopen ("large_output.txt","w",stdout);
freopen ("large_input.txt","r",stdin);
int t;
cin >> t;
int cases=t;
while(t--)
{
	//cout << "Case #"<<case-t+1<<": " ;


	int flag=0;
	cout << "Case #" << cases-t << ": " ;
	cin >> s;
	recur(s,s.size()-1);
	for(int i=0;i<s.size() && s.size()>1;i++)
	{
		if(flag==9)
		s[i]=9+48;
		if(s[i]==9+48)
		flag=9;
	}/*
	flag=0;
	for(int i=0;i<s.size();i++)
	{
	if(s[i]==0 && flag==0)
	continue;
	if(s[i]!=0 && flag==0)
	flag=1;
	cout << s[i];
}
cout << endl;*/
s.erase(0, min(s.find_first_not_of('0'), s.size()-1));
cout << s <<endl;
}

}




