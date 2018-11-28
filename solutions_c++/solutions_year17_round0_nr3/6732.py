#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <fstream>
using namespace std;

bool sortbyd(const pair<long long,long long> &a,
                   const pair<long long,long long> &b)
{
       if (a.second != b.second) {
            return a.second > b.second;
        }
    return a.first < b.first;
}

int main()
{
    ifstream fin;
    fin.open("smallin.txt");
    ofstream fout;
    fout.open("smallout.txt");
    int t,x=1;
    fin>>t;
    while(x<=t)
    {
        long long n,k,minlast,maxlast,curr,g;
        fin>>n>>k;
        vector <pair <long long, long long > > keep;
        keep.push_back(make_pair(0,n));

        while(k--)
        {
            sort(keep.begin(),keep.end(),sortbyd);
            if(keep[0].second %2 ==0)
            {
                g=keep[0].second/2;
                curr=keep[0].first+g;
                keep[0].second=g-1;
                keep.push_back(make_pair(curr,g));
                maxlast=g;
                minlast=g-1;
            }
            else
            {
                if(keep[0].second == 1)
                {
                    //long long ki,o;
                    keep.erase(keep.begin()+0);
                    //keep.pop_front(make_pair(ki,o));
                    maxlast=0;minlast=0;
                }
                else{
                g=keep[0].second/2;
                curr=keep[0].first+g+1;
                keep[0].second=g;
                keep.push_back(make_pair(curr,g));
                maxlast=g;
                minlast=g;}
            }
        }
        //long long si=keep.size();
        //cout<<"keep size is "<<si<<endl;
        fout<<"Case #"<<x<<": "<<maxlast<<" "<<minlast<<endl;
        ++x;
    }
    return 0;
}
