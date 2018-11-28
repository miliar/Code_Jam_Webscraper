#include <bits/stdc++.h>
using namespace std;

int main() {
	int t,q,k,cnt,f,l,i,j;
	string str;
	cin>>t;
	for(q=1;q<=t;q++)
	{
	    cin>>str>>k;
	    cnt=0;
	    f=1;
	    l=str.length();
	    for(i=0;i<=l-k;i++)
	    {
	        if(str[i]=='-')
	        {
	            cnt++;
	            for(j=i;j<i+k;j++)
	            {
	                if(str[j]=='-')
	                 str[j]='+';
	                else
	                 str[j]='-';
	            }
	        }
	    }
	    while(i<l)
	    {
	        if(str[i]=='-')
	         f=0;
	        i++;
	    }
	    if(f)
	     cout<<"Case #"<<q<<": "<<cnt<<endl;
	    else
	     cout<<"Case #"<<q<<": IMPOSSIBLE"<<endl;
	}
	return 0;
}
