#include <iostream>
#include<list>
using namespace std;

int main()
{
    int testcases;
    cin>>testcases;
    for(int t=1;t<=testcases;t++){
    unsigned long long int num,k;
    cin>>num>>k;
    while(num>1000 && k>1){
        if(k%2==1 && num%2==0)
        {
            num=num-1;
        }
        else{
        num=num/2;
        k=k/2;
        }

    }
    if(k==1){
         if(num%2==0)
    {
        cout<<"Case #"<<t<<": "<<num/2<<" "<<num/2 -1<<endl;
    }
    else{
        cout<<"Case #"<<t<<": "<<num/2<<" "<<num/2<<endl;
    }
    }
    else{
    long long int arr[num+2]={};
    arr[0]=1;
    long long int z=0;
    long long int ab,prev;
    arr[num+1]=1;
    while(z!=k-1){
    long long int diff=-1;
    long long int beg=0;
    for(long long int i=1;i<num+2;i++){
        if(arr[i]!=0){
        prev=beg;
        beg=i;
        if((beg-prev)>diff)
        {
        diff=beg-prev;
        ab=prev;
        }
        }
    }

    diff=diff/2;
    z++;

    arr[ab+diff]=1;

    }
    long long int ma=-1;
    long long int ct=0;
    for(long long int i=0;i<num+2;i++) {
        if(arr[i]==0)
        {
            ct++;
        }
        else{

            if(ct>ma)
            {
                ma=ct;

            }
            ct=0;
        }

    }

    if(ma%2==0){
        cout<<"Case #"<<t<<": "<<ma/2<<" "<<ma/2 -1<<endl;
    }
    else{
        cout<<"Case #"<<t<<": "<<ma/2<<" "<<ma/2<<endl;
    }
    }
    }
    return 0;
}