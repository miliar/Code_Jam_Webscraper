#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <math.h>
#include <map>
#include <functional>
#include <queue>

using namespace std;
#define LL long long
int main(int argc, char *argv[])
{
    int T;
    cin >> T;
    for (int i=0;i<T;i++)
    {
        LL N,K;
        cin >> N >> K;
        std::priority_queue<LL> q;
        q.push(N);
        LL ans = 0;
        for (LL j=0;j<K;j++)
        {
            ans = q.top(); q.pop();
            LL p1 = (ans-1)/2;
            LL p2 = (ans/2);
            if (p1>0) q.push(p1);
            if (p2>0) q.push(p2);
        }
        cout << "Case #" << (i+1) << ": " << (LL)(ans/2) << " " << (LL)((ans-1)/2) << endl;
    }




 return 0;
}
