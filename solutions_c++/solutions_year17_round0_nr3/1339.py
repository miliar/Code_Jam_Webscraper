//
//  main.cpp
//  google cj1 q
//
//  Created by Magen on 08/04/2017.
//  Copyright © 2017 Magen. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;
typedef long long ll;
int main() {
    ios_base::sync_with_stdio(false);
    int T;
    cin>>T;
    bool first=true;
    for(int i=1;i<=T;i++)
    {
        if(first)first=false;
        else cout<<endl;
        ll n,k;
        cin>>n>>k;
        ll pos,sq;
        k--;
        ll cur=1;
        sq=1;
        ll sum=1;
        while (sum<=k) {
            cur*=2;
            sq++;
            sum+=cur;
        }
        sum-=cur;
        sq--;
        cur/=2;
        pos=k-sum+1;
        
        ll even=0;
        ll odd=0;
        ll even_size,odd_size;
        if(n%2==0)
        {
            even++;
            even_size=n;
            
        }
        else
        {
            odd++;
            odd_size=n;
        }
        
        
        for(int j=0;j<sq;j++)
        {
            ll new_even,new_odd,new_even_size,new_odd_size;
            new_odd=0;
            new_even=0;
            if(even>0)
            {
                if((even_size/2)%2!=0)
                {
                    new_odd_size=even_size/2;
                    new_even_size=new_odd_size-1;
                }
                else
                {
                    new_even_size=even_size/2;
                    new_odd_size=new_even_size-1;
                }
                if(new_even_size>0)
                    new_even+=even;
                if(new_odd_size>0)
                    new_odd+=even;
                
            }
            if(odd>0)
            {
                if(((odd_size-1)/2)%2==0)
                {
                    new_even_size=(odd_size-1)/2;
                    if(new_even_size>0)
                        new_even+=(odd*2);
                }
                else{
                    new_odd_size=(odd_size-1)/2;
                    if(new_odd_size>0)
                        new_odd+=(odd*2);
                }
            }
            
            even=new_even;
            odd=new_odd;
            even_size=new_even_size;
            odd_size=new_odd_size;
            
        }
        cout<<"Case #"<<i<<": ";
        if(odd_size>even_size)
        {
            if(pos<=odd)
            {
                cout<<odd_size/2<<" "<<odd_size/2;
            }
            else
            {
                cout<<even_size/2<<" "<<even_size/2-1;
            }
        }
        else
        {
            if(pos<=even)
            {
                cout<<even_size/2<<" "<<even_size/2-1;
            }
            else
            {
                cout<<odd_size/2<<" "<<odd_size/2;
            }
        }
        
    }
    return 0;
}
