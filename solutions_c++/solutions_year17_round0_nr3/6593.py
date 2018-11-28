#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("C-small.in.txt","r",stdin);
    freopen("outC.txt","w",stdout);
    long long int T;
    unsigned long long int N,K;


    cin>>T;

    for(long long int I=1;I<=T;I++)
    {
        priority_queue<unsigned long long int>Q;
        cin>>N>>K;
        Q.push(N);
        while(K--)
        {
            unsigned long long int Top=Q.top();
            Q.pop();
            if(Top%2==0)
            {
                Q.push(Top/2);
                Q.push((Top/2)-1);
                if(K==0) { cout<<"Case #"<<I<<": "<<Top/2<<" "<<Top/2-1<<endl; break; }
            }
            else
            {
                Q.push(Top/2);
                Q.push(Top/2);
                if(K==0) { cout<<"Case #"<<I<<": "<<Top/2<<" "<<Top/2<<endl; break; }
            }
        }
    }
    return 0;
}

