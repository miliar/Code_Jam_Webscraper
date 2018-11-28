#include<iostream>
#include<vector>
#include<queue>
#include<numeric>

using namespace std;

int main()
{

    int n,k,x,y,z, t;
    vector<pair<int, int> > vec;
    cin>>t;
    for(int ii = 1; ii <= t; ii++){
    cin>>n>>k;
    priority_queue <int> v;
    v.push(n);

    for(int i=0;i<k;i++)
    {

        n=v.top();
        v.pop();
        if(n%2==0)
        {

             x=n/2;
             y= n-x;
            z=x-1;

        }
        else
        {
            x=n/2+1;
            y= n-x;
            z=x-1;

        }
        v.push(z);
        v.push(y);

    }
    vec.push_back(make_pair(z, y));

    }
    for(int i = 0; i < t; i++){
        cout<<"Case #"<<i+1<<": ";
        cout<<vec.at(i).second<<" "<<vec.at(i).first<<endl;
    }
    return 0;
}
