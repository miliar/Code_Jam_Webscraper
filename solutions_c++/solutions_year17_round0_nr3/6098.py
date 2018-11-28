#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
        long long int t,l=1,k,temp,temp1,temp2;
        long long unsigned int n;
        cin>>t;
        while(t--)
        {
            cin>>n>>k;
            priority_queue<long long unsigned int> p;
            p.push(n);
            k--;
            while(k--)
            {
                temp=p.top();
                if(temp%2==0)
                {
                   temp1=temp/2;
                   temp2=temp1-1;
                }
                else
                {
                    temp1=temp/2;
                    temp2=temp1;
                }
                p.pop();
                p.push(temp1);
                p.push(temp2);
            }
            temp=p.top();
            if(temp%2==0)
                {
                   temp1=temp/2;
                   temp2=temp1-1;
                }
                else
                {
                    temp1=temp/2;
                    temp2=temp1;
                }
            cout<<"Case #"<<l<<": "<<temp1<<" "<<temp2<<endl;
            l++;
        }
    return 0;
}
