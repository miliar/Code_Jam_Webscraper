
#include<iostream>
using namespace std;
int main()
{
    int t,n;
     int k=1;
    cin>>t;
    int a[1001];
    while(t--)
    {
       
        cin>>n;
        while(n>0)
        {
            int flag=1;
            int i=0,count1=0,count2=0;
            int num=n;
            while(num>0)
            {
                a[i]=num%10;
                num=num/10;
                i++;count1++;
                
            }
            for(int j=0;j<i-1;j++)
            {
                if(a[j]-a[j+1]>=0)
                {                    count2++;
                }
                else
                {
                    flag=0;
                    n=n-1;
                    break;
                }
            }
            if(flag==1)
            {
                cout<<"case #"<<k<<":"<<" ";
                for(int j=i-1;j>=0;j--)
                    cout<<a[j];
                cout<<"\n";
                
                break;
            }
            
        }
        k++;
    }
    return 0;
}
