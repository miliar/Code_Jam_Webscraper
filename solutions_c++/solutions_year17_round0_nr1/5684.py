#include <iostream>
using namespace std;
int main() { int n,j,l,i,t,p,k,q,min_p;
   char s[1002];
    cin>>t;
    n=1;
    while(n<=t)
    {   
      int count=0;
      cin>>s;
      cin>>k;
      min_p=0;
      for(l=0;s[l]!='\0';l++);
    for(i=0;i<l;i++)
    { q=1;p=q+k;
      j=i;
      if(j==l-k)
        {while(j<l)
          { if(s[j++]=='-')
           min_p++;
          }
        if(min_p%k==0)
        {if(s[--j]=='-')
          count++;break;
        }
        else {count=-1;break;}
       }
        if(s[i]=='-')
     
       {
        while(q<p)
        {if(s[j]=='+')s[j]='-';
          else if(s[j]=='-')s[j]='+';
          q++;j++; 
         }count++;
        }
      
    } if(count==-1)
        cout<<"case #"<<n<<": IMPOSSIBLE"<<endl;
    else
    cout<<"case #"<<n<<": "<<count<<endl;
        n++;
        
    }return 0;
}