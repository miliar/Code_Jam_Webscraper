#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;

int no(char p[])
{
    int no = 0;
    for(int i=0;p[i];i++) 
     if(p[i] == '-') 
     no++;
    return no;
}

int main()
{
 ifstream fin("A-small-attempt0.in");
 ofstream fout("A-small-out.txt");   
 int t;
  fin>>t;
  
    for(int i=1;i<=t;i++)
    {
        int count=0,slen,len;
        char p[1001];
        fin>>p>>slen;
       
        for(len=0;p[len];len++);
        
        for(int j=0;j<=len-slen+1;j++)
        {
            if(no(p) == 0) break;
            if(p[j] == '-')
            {
                count++;
                for(int k=0;k<slen;k++)
                {
                    if(p[j+k] == '-') p[j+k] = '+';
                    else p[j+k] = '-';
                }
            }
        }
        
        if(no(p) != 0) 
		fout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
	
        else 
          fout<<"Case #"<<i<<": "<<count<<endl;
		 
    }
    fout.close();
}
