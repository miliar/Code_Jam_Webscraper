#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<utility>

using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;

    fin.open("in.in");
    fout.open("out1.txt");

    vector< pair<int, char> > arr;

    int t;
    fin>>t;

    int i=0;

    int n, r, o, y, g, b, v;

    while(i<t && ++i)
    {
        fin>>n>>r>>o>>y>>g>>b>>v;

        fout<<"Case #"<<i<<": ";

        if(r>y+b || y>r+b || b>r+y )
        {
            fout<<"IMPOSSIBLE"<<endl;
            continue;
        }

        arr.push_back(make_pair(r,'R'));
        arr.push_back(make_pair(b,'B'));
        arr.push_back(make_pair(y,'Y'));

        sort(arr.begin(), arr.end());

        vector< pair<int, char> > :: iterator it;

        while(arr[1].first > arr[0].first)
        {
            fout<<arr[2].second<<arr[1].second;
            arr[2].first--;
            arr[1].first--;
        }

        while(arr[2].first > arr[1].first)
        {
            fout<<arr[2].second<<arr[1].second<<arr[2].second<<arr[0].second;
            arr[2].first -= 2;
            arr[1].first--;
        }

        while(arr[2].first>0)
        {
            fout<<arr[2].second<<arr[1].second<<arr[0].second;
            arr[2].first--;
        }
        fout<<endl;
        arr.clear();
    }
}
