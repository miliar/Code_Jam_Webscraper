#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <math.h>
#include <sstream>
#include <cstring>
#include <climits>
#include <ctype.h>

using namespace std;

bool isAllHappy(string s)
{
    return (s.find('-')== -1);
}

int main()
{
 freopen("input.in","r",stdin);
 freopen("output.out","w",stdout);
    int t,k;
    cin >> t;
    string s;
    vector <string> vis;
    for(int i = 1; i <= t ; i++)
    {
        vis.clear();
        cin >> s >> k;
        queue <string> pancakes;
        pancakes.push(s);
        vis.push_back(s);
        int res = 0;
        bool ck = false;
        while(!pancakes.empty())
        {
            int sz = pancakes.size();
            for(int j = 0 ; j < sz; j++)
            {
                string cur = pancakes.front();
                pancakes.pop();
                //cout << "cur: "<<cur << endl;
                if(isAllHappy(cur)){
                    ck = true;
                    break;
                }

                for(int n = 0 ;n < cur.length()-k+1;n++){
                    string flipped = cur;
                    for(int m = n ; m < n+k ; m++){
                        flipped[m] = (flipped[m]=='-')?'+':'-';
                    }
                    //cout << flipped << endl;
                    if(find(vis.begin(),vis.end(),flipped)==vis.end()){
                        pancakes.push(flipped);
                        vis.push_back(flipped);
                    }
                }
            }
            if(ck)break;
            res++;
        }
        if(ck)
            cout <<"Case #"<<i<<": "<<res<<endl;
        else
            cout <<"Case #"<<i<<": IMPOSSIBLE"<<endl;
    }

    return 0;
}
