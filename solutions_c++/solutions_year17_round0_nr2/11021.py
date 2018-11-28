#include<iostream>
#include<math.h>
using namespace std;
float build(float number);
int main()
{
    float t,number,i;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>number;
        cout<<"Case #"<<i<<": "<<build(number)<<endl;
    }

}float build(float number)
{
    float prev,now,i,n,flag=0,w1,w2;
    for(i=1;pow(10,i)<number;i++);
    n=i;
    prev = fmod(number,10);
    for(i=1;i<=n;i++)
    {
        w1=pow(10,i+1);
        w2=pow(10,i);
        now=(fmod(number,w1)-fmod(number,w2))/w2;
        if(prev<now)
            flag++;
        prev=now;
    }
    if(flag==0)
        return number;
    else
        build(number-1);
}

