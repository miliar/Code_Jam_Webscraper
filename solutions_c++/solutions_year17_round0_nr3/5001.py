#include<iostream>
#include<vector>
using namespace std;
void rec(int t,int &max,int &min,vector<int> &v)
{
    if((t%2)==0)
    {
        max=t/2;
        min=(t/2)-1;
        v.push_back(max);
        v.push_back(min);
    }
    else
    {
        max=min=(t-1)/2;
        v.push_back(max);
        v.push_back(min);
    }
}
int main()
{
    vector<int> v;
    int n,t,k,c,max,min,m1;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        v.resize(0);
        c=1;
        cin>>t>>k;
        rec(t,max,min,v);
        while(true)
        {
            m1=v[c-1];
            if(c==k)
            {
                cout<<"Case #"<<i+1<<": "<<max<<" "<<min<<endl;
                break;
            }
            else
            {
                t=m1;
                rec(t,max,min,v);
                c++;
            }
        }
    }
}