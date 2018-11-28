#include <fstream.h>
#include<stdio.h>
#include<string.h>
using namespace std;
int main()
{
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    char s[1001];
	    int k,cnt=0,i,j,flag=0,m;
	    cin>>s>>k;
	    m=strlen(s);
	    for(i=0;s[i]!='\0';i++)
	    {
	        if(s[i]=='-')
	        {
	            cnt++;
	            for(j=i;j<i+k;j++)
	            {
	                if(i+k>m)
	                {
	                    break;
	                }
	                if(s[j]=='-')
	                {
	                    s[j]='+';
	                }
	                else if(s[j]=='+')
	                {
	                    s[j]='-';
	                }
	            }
	        }
	    }
	    for(i=0;s[i]!='\0';i++)
	    {
	        if(s[i]=='-')
	        {
	            flag=1;
	            break;
	        }
	    }
	    if(flag==1)
	    {
	        cout<<"IMPOSSIBLE"<<endl;
	    }
	    else
	    {
	        cout<<cnt<<endl;
	    }
	}
	return 0;
}
