#include <iostream>
using namespace std;

int main() {
    int t,flag,i,j,k,count,pos;
    long long n,result,temp,temp2;
    int arr[20];
    cin>>t;
    k=1;
    while(t>0)
    {
        cin>>n;
        temp=n;
        i=0;
        while(temp>0)
        {
            arr[i]=temp%10;
            temp=temp/10;
            i++;
        }
        flag=0;
        for(j=0;j<i-1;j++)
        {
            if(arr[j]<arr[j+1])
            {
            flag=1;
            break;
            }
        }
        if(flag==1 && n>=100)
        {
        count=1;
        for(j=1;j<i-1;j++)
        {
            if(arr[j]<=arr[j+1])
            {
            count++;
            pos=j;
            }
            else
            {
            pos=j;
            break;
            }
        }
        if(arr[pos]>arr[pos+1])
        {
        temp=0;
        for(j=i-1;j>pos;j--)
        {
            temp=temp*10+arr[j];
        }
        for(j=0;j<=pos;j++)
        {
            temp=temp*10;
        }
        temp2=1;
        for(j=0;j<count;j++)
        {
        temp2=temp2*10;
        }
        temp2=temp2*arr[pos];
        result=temp+temp2-1;
        }
        else
        {
            for(j=0;j<=pos;j++)
        {
            arr[j]=0;
        }
        temp=0;
        for(j=i-1;j>=0;j--)
        {
            temp=temp*10+arr[j];
        }
           result=temp-1; 
        }
        }
        else if(flag=1 && n>=10 && n<100)
        {
            temp=n%10;
            result=n-(temp+1);
        }
        else
        result=n;
        cout<<"Case #"<<k<<": "<<result<<endl;
        t--;
        k++;
    }
    
	// your code goes here
	return 0;
}
