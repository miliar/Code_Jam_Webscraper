#include <iostream>
#include <string>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
	    string s;
	    int b=-1;
		int change=-1;
	    cin>>s;
	  
	    for(int j=0;j<(s.size()-1);j++){
                if(s[j]>s[j+1]){
	                 change=j;
	                 b=0;
	                 break;
	             }
	         }
	        
          if(change!=-1){
		   
           for(int j=change+1;j<s.size();j++)
           s[j]=57;
        
           
           for(int j=change;j>=1;j--){
             if(j==1)
               {
                   if(s[j]==s[j-1])
                   {
                       s[j]=57;s[j-1]-=1;
                       b=1;
                   }
               }
               else{
                   if(s[j]==s[j-1]){
                       s[j]=57; b=1;
                   }
                   else{
                       s[j]=57;s[j-1]-=1;b=1;break;
                   }
               }
           }
          
          if(b==0)
          s[change]-=1;
	  }
	    
	    cout<<"Case #"<<i<<": ";

	    for(int j=0;j<s.size();j++){
	        if(j==0&&s[j]==48);
	        else cout<<s[j];
	    }
	    cout<<endl;
	} 
	return 0;
}
