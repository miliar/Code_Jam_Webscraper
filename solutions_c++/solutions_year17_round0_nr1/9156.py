#include<iostream>
#include<stdio.h>
#include <fstream>
#include<string.h>

using namespace std;

int check(char str[1010])
    {
    	for(int i=0;i<strlen(str);i++)
    	   {
    	   	 if(str[i]=='-')
    	   	   return 0;
		   }
		return 1;
	}

int main()
  {
  	ofstream myfile;
    int t,o[100],l,k,c=0,i=0,p[100],m;
    char s[100][1010];
  	cin>>t; 	 	
  	while(t>0)
  	    {
  	      scanf("%s",s[c]) ;
  	      cin>>p[c];	      
		  c++;	
		  --t;		  
		}
  	while(c--)
  	    {	 
  	        l=strlen(s[i]);
  	        k=0;
  	        o[i]=0;	        
  	        while(l>=p[i])
  	            {
  	              	
  	            	if(s[i][k]=='-')
  	            	  {
  	            	  	for(m=0;m <p[i];m++)
  	            	  	    {
  	            	  	        if(s[i][k+m]=='-')
  	            	  	            s[i][k+m]='+';
  	            	  	        else
  	            	  	            s[i][k+m]='-';	
							}
  	            	  	o[i]++;
					  }
					k++;
  	            	l--;
				}
  	        if(check(s[i]))  	          
  	            {		
				  	myfile.open ("output.txt");	  
				    cout<<"case #"<<i+1<<": "<<o[i]<<"\n\n";
  	          	    myfile<<"case #"<<i+1<<": "<<o[i]<<"\n\n";
  	          	    myfile.close();
  	            }
  	        else
  	            {	
				  	myfile.open ("output.txt");		  
				    cout<<"case #"<<i+1<<": IMPOSSIBLE\n\n";
  	          	    myfile<<"case #"<<i+1<<": IMPOSSIBLE\n\n";
  	          	    myfile.close();
  	            }
  	        i++;
        }
 }
