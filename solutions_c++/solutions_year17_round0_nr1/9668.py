#include<iostream>
#include<string>
using namespace std;
int main()
{
    int t;
    cin >> t;
    for(int aa=1;aa<=t;aa++)
    {
        string s;
        cin >> s;
        int k,j=0,ans=0;
        cin >> k;
        while(j<s.length())
        {
            if(s[j]=='-')
                break;
            j++;
        }
        while(j+k<=s.length())
        {
            int i,temp,flag=0;
            ans++;
            for(i=j;i<j+k;i++)
            {
                if(s[i]=='-')
                    s[i]='+';
                else
                {
	                s[i]='-';
	                if(flag==0)	  
	                {
            	      temp=i;
            	      flag=1;	  
            	    }
            	}
	        }
            if(flag==1)		
        	    j=temp; 
            else
            {
                while(i<s.length())
                {
                    if(s[i]=='-')
                        break;
                    i++;
                }
                j=i;
            }     
	    }  
	    string temp="";
	    for(int i=0;i<s.length();i++)
	    	temp+="+";
	    cout << "Case #" << aa << ": " ;
	    if(s!=temp) cout << "IMPOSSIBLE" << endl;
	    else cout << ans <<endl;
    }
}