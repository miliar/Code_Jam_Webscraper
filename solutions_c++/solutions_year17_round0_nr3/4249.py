#include <bits/stdc++.h>
#include <string>
using namespace std;
bool comp(unsigned long long a,unsigned long long b)
{
    return a<b;
}
int main()
{
    int t;
    cin>>t;
    for(int j=1;j<=t;j++)
    {
    	unsigned long long n,k;
        cin>>n>>k;
        vector<double> arr;
        arr.push_back(n);
        for(unsigned long long i=1;i<k;i++)
        {
            double temp=arr.front();
            pop_heap(arr.begin(),arr.end(),comp);
            arr.pop_back();
            arr.push_back(ceil((temp-1)/(double)2));
            push_heap(arr.begin(),arr.end(),comp);
            arr.push_back(floor((temp-1)/(double)2));
            push_heap(arr.begin(),arr.end(),comp);
            /*for(int l=0;l<arr.size();l++)
                cout<<arr[l]<<" ";
            cout<<endl;*/
        }
        unsigned long long temp=arr.front();
        cout<<"Case #"<<j<<": "<<ceil((temp-1)/(double)2)<<" "<<floor((temp-1)/(double)2)<<endl;
    }
    return 0;
}