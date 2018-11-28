#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream cin("codein.txt");
    ofstream cout("codeout.txt");
    int t,i=0;
    cin>>t;
    while(i<t)
    {
        int n,k;
        cin>>n>>k;
        priority_queue<int > Q;
        Q.push(n);
        while(1)
        {
            n=Q.top();
            Q.pop();
            int l,r;
            if(n%2)
            {
                l=r=n/2;
            }
            else {
                l=n/2-1;
                r=n/2;
            }
            if(k==1)
            { cout<<"case #"<<i+1<<": "<<r<<" "<<l<<endl;
            break;
            }
            else
            {
                Q.push(l);
                Q.push(r);
                k--;
            }
        }
        i++;
    }
    return 0;
}
