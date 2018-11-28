#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t,t1,k,i,j,len,pos,flag,c;
	cin>>t;
	t1=1;
	while(t1<=t)
	{
	    string str;
	    cin>>str;
	    cin>>k;
	    len=str.length();
	    cout<<"Case #"<<t1<<": ";
	    flag=0;c=0;
	    for(i=0;i<len;)
	    {
	        if(str[i]=='+')
	        {
	            i++;
	            continue;
	        }
	        else{j=i;
	            if(j+k-1>=len)
	            {flag=1; break;
	            }  pos=-1;c++;//cout<<c<<" "<<i<<"\n";
	            while(j<i+k){ if(str[j]=='+')  {
	                    if(pos==-1)
	                    {
	                         pos=j; }str[j]='-1'; } else  {
	                    str[j]='+';
	                }
	                j++;
	            }
	            if(pos==-1)
	            i=j;
	            else
	            i=pos;
	        }
	    }
	    if(flag==1)
	    cout<<"IMPOSSIBLE\n";
	    else
	    cout<<c<<"\n";
	    t1++;
	}
	return 0;
}
