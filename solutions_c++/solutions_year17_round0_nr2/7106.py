#include<iostream>
#include<string.h>
#include <cstdio>
using namespace std;


int flag=0;

int main()
{	
 long long int T,n,t=1;
    cin>>T;
    while(t<=T)
     {
        cin>>n;
        char arr[1000];
        if(n<10)
        cout<<"Case #"<<t<<": "<<n<<endl;
    
         else
    {   while(1){
		flag=0;
        snprintf(arr,25,"%lld",n);
        for(int k=0;k<strlen(arr)-1;k++)
            {
                if(arr[k]>arr[k+1])
                {arr[k]--;
                 for(int z=k+1;z<strlen(arr);z++)
                 	arr[z]='9';
                 	
				
				k=-1;
				continue;
				}
            }
                
                cout<<"Case #"<<t<<": ";
                for(int mn=0;mn<strlen(arr);mn++)
                {	if(arr[mn]!='0' || flag == 1)
                	{
                		flag =1;
                		cout<<arr[mn];
					}
					
					
				}
				flag =0;
				cout<<endl;
				
                    break;
             
       }
            
    }
    t++;
}
    return 0;
}
