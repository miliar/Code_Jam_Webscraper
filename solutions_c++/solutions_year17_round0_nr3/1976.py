#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <stdio.h>
#include <stdlib.h>
#include <iomanip>
#include <utility> 
using namespace std;

void solve()
{
    long long int n,k;
    cin>>n>>k;
    vector<long long int>vec;
    unordered_map<long long int, long long int> umap;
    long long int newn=n,count=1;
    long long int pos,l,r;
    for(long long int i=1;i<=k;i=i+count)
    {
        if(umap.find(newn)!=umap.end())
        {
            count=umap[newn];
        }
        pos=ceil((double)(newn)/2.0);
        l=pos-1;
        r=newn-pos;
        if(l>=r)
        {
            if(umap.find(l)==umap.end())
            {
                umap[l]=count;
                vec.push_back(l);
            }
            else
                umap[l]+=count;
            if(umap.find(r)==umap.end())
            {
                umap[r]=count;
                vec.push_back(r);
            }
            else
                umap[r]+=count;
        }
        else
        {
            if(umap.find(r)==umap.end())
            {
                umap[r]=count;
                vec.push_back(r);
            }
            else
                umap[r]+=count;
            if(umap.find(l)==umap.end())
            {
                umap[l]=count;
                vec.push_back(l);
            }
            else
                umap[l]+=count;
        }
        newn=vec[0];
        vec.erase(vec.begin()+0);
    }
    cout<<max(l,r)<<" "<<min(l,r)<<endl;
}
int main() 
{
    int t;
    cin >>t;
    for(int i=1;i<=t;i++)
    {
        cout << "Case #"<<i<<": ";
        solve();
    }
	return 0;
}
