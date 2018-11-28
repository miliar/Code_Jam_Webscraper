#include<iostream>
#include<stdio.h>
#include <fstream>

using namespace std;

int isdescending(int a[18], int p) 
    {
        for (int i=0;i<p-1;i++) 
	        {
                if (a[i]<a[i+1]) 			
                    return 0;            
            }
        return 1;
   }
int main()
  {
  	ofstream myfile;
  	long int n[100],temp;
  	int a[18],p,t,c=0,i=0,output=1;
  	cin>>t; 	
  	while(t--)
  	    {
  	      cin>>n[c]; 
		  c++;	
		}
  	while(c--)
  	{	  	     	
  	    while(n[i]>0)
  	    {
  	    	p=0;
  	    	temp=n[i];
  	    	while(temp>0)
  	    	   { 	    	   	    
  	    	    	a[p]=temp%10;
  	    	    	
  	    	    	temp=temp/10;
  	    	    	p++;
			   }			
  	    	if(isdescending(a,p)==1||p==1)
  	    	   {
  	    	        //cout<<"case #"<<output++<<":"<<n[i]<<"\n";
  	    	        myfile.open ("output.txt");
                    myfile<<"case #"<<output++<<": "<<n[i]<<" ";
                    myfile.close();
					break;	
			   }
			n[i]--;
		}
		i++;
   }
  }
