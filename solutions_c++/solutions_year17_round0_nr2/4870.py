
#include <iostream>
 #include <sstream>
#include<string>
using namespace std;
 long long int plusit  =0,sum =0;
 string prev ;
bool isright(string str,long long int n)
{
	long long int i,j;
	for(i=0;i<n-1;i++)
	{
		if(str.at(i)>str.at(i+1))
			{ return false;}	
	} 
return true;
}

bool lexographicorder(string str2,string lamba)
{
	if(str2>=lamba)
	{
		return true;
	}
	return false;
}
void checkitbro(string lamba,long long int start, string out, long long int n,long long int k)
{
   
    if (n == 0)
    {
       if(lexographicorder(out,lamba))
       	{ if(sum !=0){
       			plusit ++;
       			cout<<"Case #"<<k<<": "<<prev<<endl;
       		}
        	return;}
        else { 
        		sum ++;
        		prev =out; return;
        	 }  }

    for (long long int i = start; i <= 9; i++)
    {
				if(plusit >=1){return ;}         
				string str;          
				ostringstream chemp;  
				chemp<<i;
				str=chemp.str();
        
        str =   out + str;
 
        checkitbro(lamba,i + 0, str, n - 1,k);
    }if(plusit >=1){return ;}  
     
}

 
 int main()
{
	long long int t;
	cin>>t;
	long long int k=0;
	while(t--)
	{
		k++;
	    long long int i,j;
    	string str;
    	cin>>str;
   		 int n = str.length();
   		 if(isright(str,n)){cout<<"Case #"<<k<<": "<<str<<endl; continue;}
   		 else {
    		checkitbro(str,1, "", n,k);
    		if(plusit ==0)
    			{
    				string newstringval = "";
    				for(int y =0;y<n-1;y++)
    				{
    					newstringval = newstringval + "9";
    				} cout<<"Case #"<<k<<": "<<newstringval<<endl;
    			}
    		plusit  =0;sum =0;
    	}
    
    }
}