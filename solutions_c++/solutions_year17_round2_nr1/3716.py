#include<iostream>
#include<stdio.h>
#include<vector>
using namespace std;


int main()
{

    vector <double> v;
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int n,d;
        cin>>d>>n;
        double k[n],s[n];
        for(int j=0;j<n;j++)
        {
            cin>>k[j]>>s[j];


        }
        double min=0;
        double time;
        for(int j=0;j<n;j++)
        {
            time =(d-k[j])/s[j];
            if(time>min)
                min=time;
        }
        double ans=d/min;
        v.push_back(ans);
    }
    for(int k=0;k<v.size();k++)
    {

            //cout<<"case #"<<k+1<<": "<<v.at(k)<<endl;
            printf("Case #%d: %0.6lf\n",k+1,v.at(k));


    }
}
