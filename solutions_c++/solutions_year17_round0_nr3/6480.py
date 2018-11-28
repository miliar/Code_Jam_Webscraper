//
//  main.cpp
//  Bathroom
//
//  Created by Sabita_Sant on 08/04/17.
//  Copyright © 2017 Sabita_Sant. All rights reserved.
//

#include <iostream>
using namespace std;
int main(int argc, const char * argv[]) {
    int t,i,c=0,k,j,p,q,maxp,maxq,y,z,pos;
    long n,max;
    
    cin>>t;
    while (t--) {
        c++;
        cin>>n>>k;
        bool chosen[n+2];
        chosen[0]=true;
        chosen[n+1]=true;
        for (i=1; i<n+1; i++) {
            chosen[i]=false;
        }
       
        for(j=0;j<k;j++)
        {
            
            max=0;
            maxp=0;
            maxq=0;
            p=0;
            q=0;
            for (i=0; i<n+2; i++) {
                if (chosen[i]) {
                    p=i;
                }
                else
                {
                    q=i;
                    if((q-p)>max)
                    {
                        max=q-p;
                        maxp=p;
                        maxq=q;
                    }
                }
            }
            pos=(maxp+maxq+1)/2;
            y=pos-maxp-1;
            z=maxq-pos;
            chosen[pos]=true;
            
        }
        cout<<"\nCase #"<<c<<": ";
        if (y>z) {
            cout<<y<<" "<<z;
        }
        else
            cout<<z<<" "<<y;

       
        
    }
    
    return 0;
}
