#include<stdio.h>
#include<iostream>
#include<string.h>
#include <fstream>
using namespace std;



long long middle(long long n,long long k)
{
    if(k==1)return n-1;
    else{
        if(k%2==0)
            return middle(n/2,k/2);
        else{
            if(n%2==0)
                return middle(n/2-1,k/2);
            else
                return middle(n/2,k/2);
        }
    }
}
    
        
int main() {
   ifstream fin ("C-large.in");
    ofstream fout ("C_large_output.txt");
     
	int t;
        long long n,k,x,y,z;
        fin>>t;
	for (int j = 1; j <= t; j++) 
        {
                fin>>n>>k;       
                x=middle(n,k);
                if(x%2==1)
                {
                    y=(x+1)/2;
                    z=(x-1)/2;
                }
                else
                {
                    y=x/2;
                    z=x/2;
                }
                             
                fout<<"Case #"<<j<<": "<<y<<" "<<z<<endl;
               
		
	}
        fout.close();
}

