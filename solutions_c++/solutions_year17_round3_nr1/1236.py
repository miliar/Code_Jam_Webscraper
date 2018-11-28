#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
const double pi = 3.14159265359;
int q,t,i,n,k,p;
double x,y,Arie,mx,Arie1;
pair< double,pair<float,float> > V[10001];
bool f(pair< double,pair<float,float> > A, pair< double,pair<float,float> > B)
{
    if (A.first == B.first)
        return A.second.first * A.second.first > B.second.first * B.second.first;
    return A.first < B.first;
}
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    cin>>t;
    for (int q=0;q<t;q++)
    {
        cout<<"Case #"<<q+1<<": ";
        cin>>n>>k;
        for(i=0;i<n;i++)
        {
            cin>>x>>y;
            V[i] = make_pair(-x*y,make_pair(x,y));
        }
        sort(V,V+n,f);

       /* for (i=0;i<n;i++)
        {
            cout<<-V[i].first*2<<" "<<V[i].second.first*V[i].second.first<<" "<<V[i].second.first<<" "<<V[i].second.second<<'\n';
        }
        cout<<'\n';*/
        mx = V[0].second.first;
        p= 0;
        for (i=0;i<k;i++)
        {
            if (V[i].second.first>mx)
            {
                mx =V[i].second.first;
                p = i;
            }
        }
        Arie = V[p].second.first*V[p].second.first*pi;
        for (i=0;i<k;i++)
        {
            Arie += V[i].second.second * V[i].second.first * 2 * pi;
        }

        mx = V[0].second.first;
        p= 0;
        for (i=0;i<n;i++)
        {
            if (V[i].second.first>mx)
            {
                mx =V[i].second.first;
                p = i;
            }
        }
        if (p>=k)
        {
            Arie1 = V[p].second.first*V[p].second.first*pi;
            for (i=0;i<k-1;i++)
            {
                Arie1 += V[i].second.second * V[i].second.first * 2 * pi;
            }
            Arie1 += V[p].second.second * V[p].second.first * 2 * pi;
            Arie = max (Arie1,Arie);
        }
        cout.precision(17);
        cout<<Arie<<'\n';
    }
}
