#include<bits/stdc++.h>
using namespace std;

#define pi 3.1415926535897932384626433

vector<pair<long long int, long long int> > v;
vector<pair<long long int, long long int> > u;

int main()
{
    std::ifstream in("in.txt");
    std::streambuf *cinbuf = std::cin.rdbuf();
    std::cin.rdbuf(in.rdbuf());

    std::ofstream out("out.txt");
    std::streambuf *coutbuf = std::cout.rdbuf();
    std::cout.rdbuf(out.rdbuf());

    long long int t,t1,n,k,i,j,x,y;
    cin>>t;
    t1 = t;
    while(t--)
    {
        cin>>n>>k;
        for(i=0;i<n;i++)
        {
            cin>>x>>y;
            v.push_back(make_pair(x,y));
        }
        sort(v.begin(),v.end());
        long double maxx = 0;
        for(i=n-1;i>=0;i--)
        {
            for(j=i-1;j>=0;j--)
            {
                u.push_back(make_pair(v[j].second*v[j].first,v[j].first));
            }
            if(u.size() >= k-1)
            {
                long double x, y = 2*v[i].second*v[i].first;
                if(u.size() > 0)
                {
                    sort(u.begin(),u.end());
                    for(j=u.size()-1;j>=u.size()-(k-1);j--)
                    {
                        y = y + 2*u[j].first;
                    }
                }
                x = pi*v[i].first*v[i].first + pi*y;
                if(x > maxx)
                {
                    maxx = x;
                }
            }
            u.clear();
        }
        cout<<setprecision(30)<<"Case #"<<t1-t<<": "<<maxx<<"\n";
        v.clear();
    }
    return(0);
}
