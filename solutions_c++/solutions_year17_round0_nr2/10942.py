#include<iostream>
#include<fstream>
#include<stdlib.h>
#include <stdio.h>
#include<cstring>
#include<cmath>
#include<math.h>
using namespace std;
main()
{
     int t, x, n, y,x2, z, d;
     unsigned long num,len,last, h, r,j;
     bool f=false;
     cin>>t;
     for(int i=0; i<t; i++)
     {
         cin>>n;
         for(j=1; j<=n; j++)
         {
             h=j;
             last=h;
             f=false;
             x=0;
             for (len = 0; last > 0; len++) last = last / 10;
             int a[len];
             for (int l=len-1; l>=0; l--)
             {
                 y=pow(10.0,l);
                 z = h/y;
                 x2 = h / (y * 10);
                 d=z - x2*10;
                 if(d!=0&&f==false) f=true;
                 if(f) a[x++]=d;
             }
             f=true;
             for(int l=0; l<x-1&&f; l++)
             {
                if(x>1)
                {
                    if(a[l]>a[l+1]) f=false;
                }
            }
            if(f)r=j;
         }
         cout<<"Case #"<<i+1<<": "<<r<<endl;
     }
}
