#include <iostream>
#include<string.h>
using namespace std;

int main() {
   
    int t=0;
    long n;
    cin>>t;
    for(int i=0;i<t;i++)
    {   int p=-1,y=-1,f=0,r=-1,w;
        cin>>n;
        for(int j=n;((j>0)&&(f==0));j--)
        { p=-1;y=-1;
            if(j<10)
                {f=1;r=j;break;}
            w=j;
            while(w>0)
            {
              y=p;   
             p=w%10;
             w=w/10;
            if(y!=-1)
             {if(y>=p){f=1;}
              else {f=0;break; }
            }
            }
            r=j;
        }
        cout<<"Case #"<<(i+1)<<": "<<r<<endl;
    }
	return 0;
}
