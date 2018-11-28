#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
#include<string>
#include<cmath>
#include<climits>
#include<fstream>
#include<sstream>

#define forn(i,n) for(int i=0;i<n;i++)
#define forv(it,v,type) for(vector<type>::iterator it=v.begin();it!=v.end();it++)

using namespace std;
ifstream fin ("input.in");
ofstream fout ("output.out");


int main()
{
    int T;
    fin >> T;
    forn(i,T)
    {
    int K,N;
    fin >> N >> K;
    map<int,int> space;
    map<int,int>::iterator it;
    space[N] = 1;
    while(K--)
    {
   // cout << "New loop" << endl;
    //for (map<int,int>::iterator it2=space.begin(); it2!=space.end();it2++){
    //cout << it2->first << " => " << it2->second << '\n';
   // }

        // get the largest element that is available
    it = space.end();
    it--;
    while(it->second <1){
        space.erase(it);
        it = space.end();
        it--;
    }
    int width = it->first;
    space[width]--;
    space[(width-1)/2]++;
    space[width/2]++;
    }
    it = space.end();
    it --;
    fout << "Case #" << i+1 << ": "  << (it->first)/2 << " " << (it->first -1)/2<< endl;
    }
}
