#include <iostream>
#include<stdio.h>
#include<string>
using namespace std;

int main() {
	// your code goes here
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
	    string s;
	    int k,flag=0,count=0;
	    cin>>s;
	    scanf("%d",&k);
	    for(int j=s.length()-1;j>=0;j--)
	    {
	        if(j-k+1>=0){
	        if(s[j]=='-')
	        {
	            for(int l=j;l>j-k;l--)
	            {
	                if(s[l]=='-')
	                s[l]='+';
	                else
	                s[l]='-';
	            }
	            count++;
	        }
	        }
	        else if(j-k+1<0)
	        {
	            for(int l=j;l>=0;l--)
	            if(s[l]=='-')
	            flag=1;
	            break;
	        }
	    }
	    if(flag==1)
	    printf("Case #%d: IMPOSSIBLE\n",i+1);
	    else
	    printf("Case #%d: %d\n",i+1,count);
	}
	return 0;
}
