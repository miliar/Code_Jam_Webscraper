#include<bits/stdc++.h>

using namespace std;
struct max_min
    {
        unsigned long long int mx;
        unsigned long long int mn;
    };

max_min fun(priority_queue<unsigned long long int> &q)
{
    unsigned long long int temp;
    temp=q.top();
    q.pop();
    //unsigned long long int temp_min=0,temp_max=0;
    max_min x;
        if(temp!=0 && temp%2==0)
        {
            x.mn=temp/2-1;
            x.mx=temp/2;
        }
        else
        {
            x.mn=x.mx=temp/2;
        }
    q.push(x.mn);
    q.push(x.mx);
    return x;


}


int main()
{
    freopen("C-small-1-attempt0.in","r",stdin);
    freopen("op3.out","w",stdout);
    int t,ii=1;
    unsigned long long int n;
    cin>>t;
    while(ii<=t)
    {
        int k;
        cin>>n>>k;
        max_min x;
        x.mn=n;
        x.mx=n;
        priority_queue<unsigned long long int> q;
        q.push(n);
        for(unsigned long long i=1;i<=k;i++)
        {
            x=fun(q);
        }
        //unsigned long long int arr[]={1,8,5,6,3,4,0,9,7,2};
        //while(!q.empty())
        //{cout<<q.top()<<" ";q.pop();}
    //std::priority_queue<int, std::vector<int>, std::greater<int> > q2;


        cout<<"Case #"<<ii<<": ";
        cout<<x.mx<<" "<<x.mn;
        cout<<endl;

        ii++;
    }
}
