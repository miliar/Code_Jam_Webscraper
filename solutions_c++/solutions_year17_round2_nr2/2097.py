#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair

typedef long long int ll;
using namespace std;
ll k[1005],s[1005];
int main()
{

    freopen("B.in","r",stdin);
    freopen("out.txt","w",stdout);

    ll t,kk=0,d,n;
    cin>>t;
    while(t--)
    {

        kk++;

        ll n,r,o,y,g,b,v;
        cin>>n>>r>>o>>y>>g>>b>>v;
        pair<int,char> p[3];
        p[0]=mp(r,'R');
        p[1]=mp(y,'Y');
        p[2]=mp(b,'B');
        sort(p,p+3);
        //cout<<p[0].first<<" hey  ";
        cout<<"Case #"<<kk<<": ";
        int cnt=1;
        int maxx=p[2].first;
        if(p[1].first==maxx){
           cnt++;
        }
        if(p[0].first==maxx)
            cnt++;
        if(cnt==3){
            for(int i=1;i<=maxx;i++){
                cout<<"RBY";
            }
            cout<<endl;
        }

        else if(cnt==2){
            for(int i=1;i<=p[0].first;i++){
                cout<<p[2].second<<p[1].second<<p[0].second;
                maxx--;
            }
            for(int i=1;i<=maxx;i++){
                cout<<p[2].second<<p[1].second;
            }
            cout<<endl;

        }
        else{
            if(p[0].first+p[1].first<maxx)cout<<"IMPOSSIBLE";
            else{
                int left=(maxx-p[1].first);
                int sec=0;
                for(int i=1;i<=p[0].first-left;i++){
                    cout<<p[2].second<<p[1].second<<p[0].second;
                    sec++;
                }
                for(int i=sec+1;i<=p[1].first;i++){
                    cout<<p[2].second<<p[1].second;
                }
                for(int i=1;i<=left;i++){
                    cout<<p[2].second<<p[0].second;
                }

            }
            cout<<endl;
        }
    }
    return 0;
}
