#include<iostream>
#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<fstream>
#define ll long long

using namespace std;

int main()
{ll t,k,flips,A[10005],inversion,len;
  char str[10005];
  
   ifstream fin;
   ofstream fout;
   
   fin.open("Input.txt");
   fout.open("OUTPUT.txt");
   
    fin>>t;
    
     for(ll popo=1;popo<=t;popo++)
      {fin>>str>>k;
        flips=0;
         inversion=0;
          len=0;
          
           for(ll i=0;str[i]!='\0';i++)
            len++;
          
          for(ll i=0; str[i]!='\0' && str[i+k-1]!='\0' ;i++)
           {
             if( str[i]=='+' && (flips%2)==0 )
              {}
               else
                if( str[i]=='+' && (flips%2)!=0 )
                 {flips++;
                   inversion++;
                    A[i+k-1]=1;
                    // cout<<i<<" "<<flips<<"\n";
                 }
                  else
                   if(str[i]=='-' && (flips%2)==0 )
                    {flips++;
                      inversion++;
                       A[i+k-1]=1;
                       // cout<<i<<" "<<flips<<"\n";
                    }
                     else
                      if(str[i]=='-' && (flips%2)!=0)
                       {}
               
                       if(A[i]==1)
                        flips--;   
           }
          
            for(ll i=len-k+1;str[i]!='\0';i++)
             {if(str[i]=='+' && flips%2==0)
               {}
                else
                 if(str[i]=='+' && (flips%2)!=0)
                  inversion=-1;
                   else
                    if(str[i]=='-' && (flips)%2==0)
                     inversion=-1;
                      else
                       if(str[i]=='-' && (flips)%2!=0)
                        {}
                        
                        if(A[i]==1)
                         flips--;
             }
             
            for(ll i=0;i<=10005;i++)
             A[i]=0;
              flips=0;
                
               
                
                 if(inversion!=-1)
                  fout<<"Case "<<"#"<<popo<<": "<<inversion<<"\n";
                   else
                    fout<<"Case "<<"#"<<popo<<": IMPOSSIBLE\n";
                   
      }
         
		 return 0;   
}
