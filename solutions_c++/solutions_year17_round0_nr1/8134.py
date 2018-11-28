#include <iostream>
using namespace std;

int check (string s,int k)
{
    int len = s.length();
    int ct=0;
    int st=0;
    while (st<=len-1)
    {
       // cout<<st<<" "<<s<<"\n";
        while (s[st] =='+' && st<=len-1)
        st++;
        if (st==len)
        return ct;
        if (st+k-1>len-1)
        return -1;
        for (int i=0;i<k;i++)
        s[st+i]=(s[st+i]=='+'?'-':'+');
        ct++;
    }
    return ct;
}

int main() {
	// your code goes here
	string s,s1;
	int items;
	int k;
	cin>>items;
	for (int i=0;i<items;i++)
	{
	    cin>>s;
	    cin>>k;
	    int ct = check(s,k);
	    s1 = s;
	    int len = s.length();
	    for (int j=0;j<len;j++)
	    s1[j]=s[len-1-j];
	    int ct1=check(s1,k);
	    ct = ct>ct1?ct:ct1;
	    //cout<<"\nabc"<<ct<<" "<<ct1<<"\n";
	    if (ct==-1)
	    cout<<"Case #"<<i+1<<": IMPOSSIBLE\n";
	    else
	    cout<<"Case #"<<i+1<<": "<<ct<<"\n";
	    
	}
	return 0;
}
