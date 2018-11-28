#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.txt","r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    cin>>tc;
    int cs = 0;
    while(tc--)
    {
        cs++;
        long long int n , k , temp;
        cin>>n>>k;
        priority_queue< int > PQ;
        PQ.push(n);
        for(int i = 1 ; i < k ; i++)
        {
            temp = PQ.top();
            PQ.pop();
            PQ.push(temp/2);
            temp -= temp/2;
            temp -=1;
            PQ.push(temp);
        }
        temp = PQ.top();
        cout<<"Case #"<<cs<<": "<<temp/2<<" "<< temp - temp/2 -1 <<endl;
    }
    return 0;
}
