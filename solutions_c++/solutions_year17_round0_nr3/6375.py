#include<iostream>
#include<vector>
#include<algorithm>
#include<numeric>
#include<queue>

using namespace std;

int main()
{

    int stall,bachche,pehla,dusra,chaspa, t;
    vector<pair<int, int> > bahr;
    cin>>t;
    for(int test = 1; test <= t; test++){
    cin>>stall>>bachche;
    priority_queue< int> thoda;
    thoda.push(stall);

    for(int i=0;i<bachche;i++)
    {

        stall=thoda.top();
        thoda.pop();
        if(stall%2==0)
        {

             pehla=stall/2;
             dusra= stall-pehla;
            chaspa=pehla-1;

        }
        else
        {
            pehla=stall/2+1;
            dusra= stall-pehla;
            chaspa=pehla-1;

        }
        thoda.push(chaspa);
        thoda.push(dusra);

    }
    bahr.push_back(make_pair(chaspa, dusra));

    }
    for(int i = 0; i < t; i++){
        cout<<"Case #"<<i+1<<": ";
        cout<<bahr.at(i).second<<" "<<bahr.at(i).first;
        cout<<endl;
    }
    return 0;
}


