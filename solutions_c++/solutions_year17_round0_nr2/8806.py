#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t,t1,len,i,j,flag;
	cin>>t;
	t1=1;
	while(t1<=t)
	{
	    cout<<"Case #"<<t1<<": ";
	    string str;
	    cin>>str;
	    len=str.length();
	    flag=0;
	    char p;
	    for(i=1;i<len;i++)
	    {
	       if(flag==1)
	       {
	           str[i]='9';
	           continue;
	       }
	       if(str[i]>=str[i-1])
	       continue;
	       else
	       {
	           str[i]='9';
	           p=str[i-1];
	           j=i-1;
	           while(p==str[j])
	           {
	               j--;
	               if(str[j]==p)
	               str[j+1]='9';
	           }
	           j++;
	           str[j]=str[j]-1;
	           flag=1;
	       }
	    }
	    t1++;flag=0;
	    for(i=0;i<len;i++)
	    {
	        if(str[i]!='0')
	        {
	            flag=1;
	            cout<<str[i];
	        }
	        else
	        {
	            if(flag)
	            cout<<str[i];
	        }
	        
	    }
	    cout<<"\n";
	}
	return 0;
}
