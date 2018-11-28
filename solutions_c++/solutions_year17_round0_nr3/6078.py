#include<iostream>
#include<vector>
#include<algorithm>
#include<numeric>
#include<queue>

using namespace std;

int main()
{

    int n,k,first,second,tag, t;
    vector<pair<int, int> > output;
    cin>>t;
    for(int test = 1; test <= t; test++){
    cin>>n>>k;
    priority_queue< int> temp;
    temp.push(n);

    for(int i=0;i<k;i++)
    {


        //sort(temp.begin(),temp.end());

        n=temp.top();
        temp.pop();
        if(n%2==0)
        {

             first=n/2;
             second= n-first;
            tag=first-1;

        }
        else
        {
            first=n/2+1;
            second= n-first;
            tag=first-1;

        }
        temp.push(tag);
        temp.push(second);

    }
    output.push_back(make_pair(tag, second));

    }
    for(int i = 0; i < t; i++){
        cout<<"Case #"<<i+1<<": ";
        cout<<output.at(i).second<<" "<<output.at(i).first;
        cout<<endl;
    }
    return 0;
}


