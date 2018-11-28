#include <iostream>
#include <queue>
#include <algorithm>
#include <fstream>
using namespace std;

int main()
{
    ifstream fin("C-small2.in");
    ofstream fout("C.out");

    int t;
    fin>>t;

    for(long c=1;c<=t;c++)
    {

        long long n,k;

        fin>>n>>k;

       // cout<<n<<" "<<k<<endl;
        priority_queue<long long>maxHeap;
        maxHeap.push(n);
        long long l,r,temp;
        while(k>0)
        {
            k--;

            temp=maxHeap.top();
            maxHeap.pop();
            temp--;
            l=temp/2;
            r=(long long)(ceil((long double)temp/2));
           // cout<<r<<" -"<<l<<endl;
            maxHeap.push(l);
            maxHeap.push(r);
        }
        fout<<"Case #"<<c<<": "<<r<<" "<<l<<endl;
    }
    return 0;
}
