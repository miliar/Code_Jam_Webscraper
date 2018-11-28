#include <iostream>
#include <algorithm>
#include <stdio.h>
using namespace std;

#define pi 3.14159265358979323846
struct pan
{
    double height;
    double radius;
};

bool compa(pan lhs,pan rhs)
{
    if(lhs.height*lhs.radius>rhs.height*rhs.radius)
    {
        return true;
    }

    else
        return false;

}
int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int n,k;
        cin>>n>>k;

        pan a[n];
        double max1=0;

        for(int j=0;j<n;j++)
        {
           cin>>a[j].radius;
            cin>>a[j].height;


        }

        sort(a,a+n,&compa);

        for(int j=0;j<k;j++)
        {
            max1=max(max1,a[j].radius);
        }

    pan temp=a[k-1];

    for(int j=k;j<n;j++)
    {
        if(a[j].radius>max1)
        {if(2*pi*(a[j].height*a[j].radius)+pi*(a[j].radius*a[j].radius)>=2*pi*(temp.height*temp.radius)+pi*(max1*max1))
        {
            temp=a[j];
            max1=a[j].radius;
        }}

    }



    double csa=0;

    for(int j=0;j<k-1;j++)
    {
        csa=csa+pi*(2*(a[j].height*a[j].radius));
    }

    csa=csa+pi*(2*(temp.height*temp.radius)+(max1*max1));
    printf("Case #%d: %0.8f\n",i+1,csa);}

    return 0;
}
