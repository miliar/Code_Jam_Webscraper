
#include <iostream>
 #include <sstream>
#include<string>
using namespace std;
 long long int abracadabra  =0,sum =0;
 string prev ;
bool chupa(string str,long long int n)
{
	long long int i,j;
	for(i=0;i<n-1;i++)
	{
		if(str.at(i)>str.at(i+1))
			{ return false;}	
	} 
return true;
}

bool wizardwa(string str2,string bahotbada )
{
	if(str2>=bahotbada )
	{
		return true;
	}
	return false;
}
void sahihai(string bahotbada ,long long int start, string out, long long int n,long long int k)
{
   
    if (n == 0)
    {
       if(wizardwa(out,bahotbada ))
       	{ if(sum !=0){
       			abracadabra ++;
       			cout<<"Case #"<<k<<": "<<prev<<endl;
       		}
        	return;}
        else { 
        		sum ++;
        		prev =out; return;
        	 }  }

    for (long long int i = start; i <= 9; i++)
    {
				if(abracadabra >=1){return ;}         
				string str;          
				ostringstream johncena;  
				johncena<<i;
				str=johncena.str();
        
        str =   out + str;
 
        sahihai(bahotbada ,i + 0, str, n - 1,k);
    }if(abracadabra >=1){return ;}  
     
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
   		 if(chupa(str,n)){cout<<"Case #"<<k<<": "<<str<<endl; continue;}
   		 else {
    		sahihai(str,1, "", n,k);
    		if(abracadabra ==0)
    			{
    				string jugnikardi = "";
    				for(int y =0;y<n-1;y++)
    				{
    					jugnikardi = jugnikardi + "9";
    				} cout<<"Case #"<<k<<": "<<jugnikardi<<endl;
    			}
    		abracadabra  =0;sum =0;
    	}
    
    }
}
