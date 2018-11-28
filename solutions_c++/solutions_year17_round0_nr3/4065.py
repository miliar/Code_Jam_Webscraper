#include <iostream>
#include <string>
#include <fstream>
#include <queue>
using namespace std;

long long n,m;


int main()
{
    int tc;

    ifstream cinn("input.txt");
    ofstream coutt("output.txt");

    cinn >> tc;


    for(int i=0; i<tc; i++){
             priority_queue<long long > q;
        cinn>> n >>m;
        q.push(n);
        for(int ii=0;ii<m-1;ii++)
        {
            long long tmp = q.top();
            q.pop();
            if(tmp%2==0)
            {

                q.push(tmp/2);
                q.push(tmp/2-1);
            }
            else {
                q.push(tmp/2);
                q.push(tmp/2);
            }
        }
        long long tmp = q.top();
        if(tmp%2==0)
        {
             coutt << "Case #" << i+1 << ": " << tmp/2<<' '<<tmp/2-1 << endl;
        }
        else
            coutt << "Case #" << i+1 << ": " << tmp/2<<' '<<tmp/2 << endl;
    }
    return 0;
}
