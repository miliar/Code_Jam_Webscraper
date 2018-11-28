#include<iostream>
#include<string>
using namespace std;
int main()
{
    freopen ("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
	int t;
	cin>>t;
	string s;
	for(int i=0;i<t;i++)
	{
		cin>>s;
		cout<<"Case #"<<i+1<<": ";
		int k=0;
		int flg=0;
		if(s.length()==1)
		 cout<<s;
		 else{
		 
		while(k<(s.length()-1))
		{
		
		 	if(s[k]!='1')
			 flg=1;
			 if(s[k]>s[k+1])
			 break;		
		     k++;
        }
      
        if(k==s.length()-1)
         cout<<s;
        else{
        
        if(flg==0)
        {
        	int j=1;
        	while(j<s.length())
        	{
        	
        	  cout<<"9";
        	  j++;
            }
        }
        else
        {
        	int j=k;
        	if(s[j]!='0')
        	   s[j]--;
   	        else
   	            s[j]='9';
            while(j>0)
            {
            	if(s[j-1]>s[j])
            	{
            	
            	   s[j-1]--;
            	   s[j]='9';
         	 }
         	    else
         	        break;
     	        j--;
            }
            for(int z=0;z<s.length();z++)
            {
            	if(z<=k)
            	cout<<s[z];
            	else
            	cout<<'9';
            }
        }}}
        cout<<"\n";
        
    
		     
		
	}
	fclose(stdin);
	fclose(stdout);
}

