#include <bits/stdc++.h>
using namespace std;

struct pancake
{
    double R,H;
    bool taken = false;
};

int main()
{
    ios::sync_with_stdio(false);

    int t;
    cin>>t;
        double const PI = 3.141592653589793238462643383279502884197169399375105820974;

    for(int x=1;x<=t;x++)
    {
        int n,k;
        cin>>n>>k;

        vector<pancake*>v;
        for(int i=0; i<n; i++)
        {
            pancake* p = new pancake();
            cin>>p->R>>p->H;
            v.push_back(p);
        }

        sort(v.begin(),v.end(),[](pancake* a, pancake* b){return a->H*a->R > b->H*b->R;});


        double best = 0;

        for(int i=0;i<n;i++)
        {
            double syrup = v[i]->R * v[i]->R * PI + 2.0 * v[i]->R * v[i]->H * PI;
            int temp = k-1;
        for(int j=0; j<n && temp>0; j++)
        {
            if(i==j || v[j]->R > v[i]->R)continue;
                temp--;
                syrup+=2.0*v[j]->H*v[j]->R*PI;
        }

        best = max(best,syrup);

        }

        cout<<"Case #"<<x<<": "<<setprecision(15)<<best<<"\n";

    }




return 0;
   }

