#include <iostream>
using namespace std;
int check(long long int n)
{long long int i=0,j,k=0,a[20]={0},f=0;
   while(n)
   {a[k++]= n%10;
   n/=10;
    }
    for(i=k-1;i>-1;i--)
    {j=i-1;
     if(a[j]>=a[i]) 
      f=1;
      else {f=0;break;}
    }
    if(f==1)
    return f;
    else return f;
    
}
int main() {int p,t,c;
   long long int n,s;
    cin>>t;
    p=1;
    while(p<=t)
    {
        cin>>n;
        for( s=n;;s--)
        {c=check(s);
        if(c==1)break;
        }
        cout<<"case #"<<p<<": "<<s<<endl;
        p++;
        
    }return 0;
}
    