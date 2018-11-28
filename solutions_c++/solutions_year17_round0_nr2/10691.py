#include<iostream>
#include<string.h>
#include <cstdio>
using namespace std;


int flag=1;

int main()
{
    long long int T,n,t=1;
    cin>>T;
    while(t<=T)
     {
        cin>>n;
        long long int nn=n;
        char arr[1000];
        if(n<10)
        cout<<"Case #"<<t<<": "<<n<<endl;
    
         else
    {   while(n>9){flag=1;
        nn=n;
        while(nn>9)
            {	
			
                if(nn%10<(nn/10)%10)
                {	flag=0;
              		  break;
				}
                nn=nn/10;
            }
                if(flag){
                cout<<"Case #"<<t<<": "<<n<<endl;
                    break;}
            n--;
       }
            if(!flag)
            cout<<"Case #"<<t<<": "<<9<<endl;
    }
    t++;
}
    return 0;
}
