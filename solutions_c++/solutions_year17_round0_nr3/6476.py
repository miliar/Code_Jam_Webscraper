#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
    int test;
    cin>>test;
    for(int i=0;i<test;i++)
    {
        long long int num;
        cin>>num;
        long long int stalls;
        cin>>stalls;
        vector<long long int> arr;
        arr.push_back(num);
        for(long long int j=0;j<stalls-1;j++)
        {
            sort(arr.begin(),arr.end());
            long long int kin=arr.back();
            arr.pop_back();
            if(kin%2==0)
                arr.push_back((kin/2)-1);
            else
                arr.push_back(kin/2);
            arr.push_back(kin/2);

        }
        sort(arr.begin(),arr.end());
        long long int li=arr.back();
        if(li%2==0)
            cout<<"Case #"<<i+1<<": "<<li/2<<" "<<(li/2)-1<<endl;
        else
            cout<<"Case #"<<i+1<<": "<<li/2<<" "<<li/2<<endl;
    }
    return 0;
}
