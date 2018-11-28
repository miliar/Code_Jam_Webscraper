#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t,T=1,i;
    freopen("out1.txt", "w" ,stdout);
    freopen("inph1.txt", "r" ,stdin);
    cin>>t;
    while(T<=t)
    {
        int n,a,b,c,d,e,f;
        cin>>n>>a>>e>>b>>d>>c>>f;
        //cout<<n<<" "<<a<<" "<<b<<" "<<c<<" "<<d<<" "<<e<<" "<<f<<" -> ";
        cout<<"Case #"<<T<<": ";
        vector < pair < int,char> > v;
        v.push_back(make_pair(a,'R'));
        v.push_back(make_pair(b,'Y'));
        v.push_back(make_pair(c,'B'));

        sort(v.begin(),v.end());

        if(a>n/2 || b>n/2 || c>n/2)
        {
            cout<<"IMPOSSIBLE"<<endl;

        }
        else{

                int r=v[0].first+v[1].first;
                int l=r-v[2].first;
                int flag=1;
                while(l--)
                {
                    if(flag==1)
                    {
                        cout<<v[1].second;
                        v[1].first--;
                        flag=0;
                    }
                    else
                    {
                        v[0].first--;
                        cout<<v[0].second;
                        flag=1;
                    }
                }
                for(i=1;i<=v[2].first;i++)
                {
                    cout<<v[2].second;
                    if(v[1].first==0)
                        cout<<v[0].second;
                    else
                    {
                        cout<<v[1].second;
                        v[1].first--;
                    }
                }
                cout<<endl;
        }
        T++;

    }

    return 0;
}
