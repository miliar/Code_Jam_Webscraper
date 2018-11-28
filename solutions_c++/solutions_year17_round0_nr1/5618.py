#include <iostream>
#include <cstring>
using namespace std;

int main() {
    int t;
    
    cin>>t;
    for(int x=1;x<=t;x++)
    {   char s[1010];
    int i,j,k,p;
        cin>>s>>k;
        int len=strlen(s);
	int count=0;
        for(i=0;s[i]!='\0';i++)
            {	
                if(s[i]=='-')
                {	if((len-i)>=k)
        			{
        				count++;
        		            for(j=i,p=1;p<=k;j++,p++)
        		            {
        		                if(s[j]=='-')
        		                    s[j]='+';
        		                else
        		                    s[j]='-';
        		            }
        		       
        		                
        		            i=j-k;
			}
		else
			{
			count=-1;
			goto jump;
			}                 
                }
            }
            jump:
	
	if(count==-1)
		cout<<"case #"<<x<<": "<<"IMPOSSIBLE"<<endl;
	else
        cout<<"case #"<<x<<": "<<count<<endl;

    }
	return 0;
}
