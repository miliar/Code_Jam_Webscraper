#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int n;
        cin>>n;
        int p;
        cin>>p;
        vector<int> a;
        a.push_back(n);
        for(int j=0;j<p-1;j++)
        {
            sort(a.begin(),a.end());
            int k=a.back();
            a.pop_back();
            if(k%2==0)
                a.push_back((k/2)-1);
            else
                a.push_back(k/2);
            a.push_back(k/2);

        }
        sort(a.begin(),a.end());
        int l=a.back();
        if(l%2==0)
            cout<<"Case #"<<i+1<<": "<<l/2<<" "<<(l/2)-1<<endl;
        else
            cout<<"Case #"<<i+1<<": "<<l/2<<" "<<l/2<<endl;
    }
    return 0;
}
