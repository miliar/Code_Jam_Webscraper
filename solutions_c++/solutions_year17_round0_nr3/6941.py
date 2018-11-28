#include <bits/stdc++.h>
#include<fstream>
#define li long long int
#define chal(n) for(li i=0;i<n; ++i)
#define ot(n) cout<<n<<"\n"
#define INF 1000000009
#define ld long double
#define ii pair<li, li>
using namespace std;

int main()
{
    li t;
    cin>>t;
    for(li tt=1; tt<=t; ++tt)
    {
        li n, k;
        cin>>n>>k;
        cout<<"Case #"<<tt<<": ";

		  priority_queue<li>q;
            	q.push(n);
           	 li co=0;
            	li ptr=0;
            while(!q.empty())
            {
                li te=q.top();
                if(te<=1)
                    break;
                q.pop();
                co++;
                if(co==k)
                {
                    li d=(te-1)/2;
                    li e=te-d-1;
                    cout<<max(d,e)<<" "<<min(d,e);
                    ptr++;
                    break;
                }
                else
                {
                    li d=(te-1)/2;
                    li e=te-d-1;
                    q.push(d);
                    q.push(e);

                }
            }
            if(ptr==0)
                cout<<"0 0";




    if(tt!=t)
        cout<<endl;
    }
    exit(0);
}
