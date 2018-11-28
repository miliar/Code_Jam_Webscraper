#include<bits/stdc++.h>
using namespace std;
void solve(int type)
{
    int n,k;
     cin>>n>>k;
        vector <int > v,v1;
        v.push_back(n);
        int kk=0;
        while(1)
        {
            //int r=v.size();
            while (!v.empty())
            {
                v1.push_back((v[(int)v.size()-1]-1)/2);
                v1.push_back((v[(int)v.size()-1]-1)-(v[(int)v.size()-1]-1)/2);
                kk++;
                if(kk==k)
                {
                    cout<<"Case #"<<type<<": "<<(v[(int)v.size()-1]-1)-(v[(int)v.size()-1]-1)/2<<' '<<(v[(int)v.size()-1]-1)/2<<endl;
                    return;
                }
                v.pop_back();
            }
            sort(v1.begin(),v1.end());
            while(!v1.empty())
            {
                v.push_back((v1[(int)v1.size()-1]-1)/2);
                v.push_back((v1[(int)v1.size()-1]-1)-(v1[(int)v1.size()-1]-1)/2);
                kk++;
                if(kk==k)
                {
                    cout<<"Case #"<<type<<": "<<(v1[(int)v1.size()-1]-1)-(v1[(int)v1.size()-1]-1)/2<<' '<<(v1[(int)v1.size()-1]-1)/2<<endl;
                    return;
                }
                v1.pop_back();
            }
            sort(v.begin(),v.end());
        }

}
int main()
{
    freopen("in","r",stdin);
   freopen("out","w",stdout);
    int t;
    cin>>t;
    for (int kkk=1;kkk<=t;kkk++)
    {

        solve(kkk);


    }
}
