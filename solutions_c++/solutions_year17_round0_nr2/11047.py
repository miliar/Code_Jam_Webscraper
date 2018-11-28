#include <iostream>
#include <vector>
using namespace std;


bool isvalid(int n)
{
    vector<int> v;
    int count = 0;
    int nodigit = 0;
    //cout<<"num = "<<n<<endl;
    while(n!=0)
    {

        v.push_back(n%10);
        n/=10;
    }
    //cout<<"vector elements = "<<endl;
    //for(int i = 0;i<v.size();++i)
    //    cout<<v[i]<<"\t";
    for(int i = v.size()-1;i>=1;--i)
        {
            if(v[i] <= v[i-1])
                count++;
        }
    //cout<<"count = "<<count<<endl;
    //cout<<"v.size = "<<v.size()<<endl;
    if(count == v.size()-1)
        return true;
    return false;
}

int main()
{
    int t; 
    int num;
    cin>>t;

    for(int z = 1;z<=t;++z)
    {
        
        cin>>num;
        for(int i = num;i>=1;--i)
        {
            if(isvalid(i))
              {
                     cout<<"Case #"<<z<<": "<<i<<endl;
                     break; 
              }
            
        }
    }
    return 0;
}