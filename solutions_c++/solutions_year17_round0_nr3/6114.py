#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <fstream>  // includes cin to read from stdin and cout to write to stdout

#include <string>
#include <vector>
#include <algorithm>
#include <assert.h>
using namespace std;  // since cin and cout are both in namespace std, this saves some text



static pair<int, int> solve(int N, int V);

int main() {
    int tc, N, K;
    
    ifstream file("./a.txt");
    ofstream ofile("./o.txt");
    file >> tc;  // read t. cin knows that t is an int, so it reads it as such.
    
    for (int i = 1; i <= tc; ++i)
    {
        
        file >> N >> K;
        
        auto v = solve(N, K);
        
        cout << "Case #" << i << ": " << v.first << " " << v.second << endl;
        ofile << "Case #" << i << ": "  << v.first << " " << v.second << endl;
        
    }
    return 0;
}

int left(int N)
{
    return N/2;
}

int right(int N)
{
    return N - 1 - (N/2);
}

int set(vector<int>& v, int start, int cur)
{
    int length = cur-start;
    for(int i = 0; i< length; i++)
    {
        v[cur] = left(v[start+i]);
        if(++cur == v.size()) return -1;
        
        v[cur] = right(v[start+i]);
        if(++cur == v.size()) return -1;

    }
    
    return cur;
}

pair<int, int> solve(int N, int V)
{
    vector<int> buff(N);
    
    int prev = 0;
    int cur = 1;
    buff[0]=N;
    
    if(N > 1)
    {
        do
        {
            int cur_uj = set(buff, prev, cur);
            prev=cur;
            cur=cur_uj;
        }
        while(cur !=-1);
    }
    sort(buff.rbegin(), buff.rend());

    int M = buff[V-1];
    
    return {M/2, (M-1)/2};
}


