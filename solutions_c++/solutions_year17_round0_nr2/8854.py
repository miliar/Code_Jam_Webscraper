#include <iostream>
#include<string.h>
#include<stdio.h>
#include<cstdlib>
#include<math.h>
using namespace std;





main()
{
    char arr[1000];
    int n,b,i,j,len,o,x,p;
 cin>>n;

    for(j=0;j<n;j++)
    {
      scanf("%s",arr);
      len=strlen(arr);
            start:
            for(i=0;i<len-1;i++)
            {
                if(arr[i]<=arr[i+1])
                    {continue;}
                else
                {
                    x=i+1;
                    arr[i]=arr[i]-1;
                     for(i;i<len-1;i++)
                    arr[i+1]='9';
                    for(p=x;p>0;p++)
                        goto start;
                }

            }

     for(i=0;i<len;i++)
    {
        if(arr[i]!='0')
        {o=i;break;}
    }
    cout<<"Case #"<<j+1<<": ";
    for(i=o;i<len;i++)
    {
       cout<<arr[i];
    }
cout<<endl;
}
}


