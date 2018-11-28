#include<iostream>
#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<fstream>
#define ll long long

using namespace std;

int main()
{ll t,len,i;
  char str[100005];
    
  ifstream fin;
  ofstream fout;
  
   fin.open("INPUT.txt");
   fout.open("OUTPUT.txt");
   
    fin>>t;
     for(ll popo=1;popo<=t;popo++)
      {fin>>str;
        len=0;
         for(i=0;str[i]!='\0';i++)
          len++;
           
           fout<<"Case #"<<popo<<": ";
           
           if(len==1)
            {fout<<str<<"\n";continue;}
          
           for(i=1;str[i]!='\0';i++)
            {if(str[i]>=str[i-1])
              continue;
               else
                break;
            }
            
             for(ll j=i;str[j]!='\0';j++)
              str[j]='9';
              
             for(ll j=i-1; j>=0&&j<len-1; j--)
              {
                   str[j]=str[j]-1;
                    if(j>0)
                     {if(str[j]>=str[j-1])
                       break;
                        else
                         str[j]='9';
                     }
                  
              }
              
              for(i=0;str[i]!='\0';i++)
               if(str[i]=='0')
                continue;
                 else
                  break;
                  
                for(ll j=i;str[j]!='\0';j++)
                 fout<<str[j];
                  fout<<"\n";
      }
        
        return 0;
    
}
