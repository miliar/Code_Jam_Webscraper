#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <stdlib.h>

using namespace std;

int main()
{
    ifstream input("B-large.in");
    ofstream output("B.out");
    string line;
    long t=0;
    input>>line;
    t=strtol(line.c_str(),NULL,10);
   // cout<<t<<endl;
    for(int k=1;k<=t;k++)
    {
        long long num;
        input>>line;
        num=strtoll(line.c_str(),NULL,10);
        vector<int>arr;
        while(num>0)
        {
            arr.push_back(num%10);
            num/=10;
        }
        reverse(arr.begin(),arr.end());
        for(int i=arr.size()-1;i>0;i--)
        {
            if(arr[i]<arr[i-1] || arr[i]==0)
            {
                for(int j=arr.size()-1;j>=i;j--)
                arr[j]=9;
                arr[i-1]--;
                //i=arr.size()-1;
            }
        }
        output<<"Case #"<<k<<": ";
        for(int i=0;i<arr.size();i++)
        {
            if(arr[i]!=0)
                output<<arr[i];
        }
        output<<endl;
    }
    return 0;
}
