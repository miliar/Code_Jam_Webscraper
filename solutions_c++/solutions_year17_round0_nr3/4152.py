#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <queue>

using namespace std;

int main()
{
    ifstream in;
    ofstream out;
    in.open("inputSmallb.txt");
    out.open("outputSmallb.txt");
    int t,cases=0;
    in>>t;
    while(t--)
    {
        cases++;
        long long int n,k;
        in>>n>>k;
        priority_queue<long long int> pq;
        pq.push(n);
        long long int j,temp,a,b;
        for(j=0;j<k;j++)
        {
            temp = pq.top();
            pq.pop();
            a = temp/2;
            b = temp-a-1;
            pq.push(a);
            pq.push(b);
        }
        out<<"Case #"<<cases<<": "<<a<<" "<<b<<endl;
    }
    return 0;
}
