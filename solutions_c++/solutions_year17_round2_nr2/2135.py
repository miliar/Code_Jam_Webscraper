#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define speed std::ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
//#define int long long
using namespace std;
vector<char> ans;
int arr[5];
char ar[5];
int main()
{
    freopen("bha.in","r",stdin);
    freopen("out4.txt","w",stdout);
    int t,c=1,d,n,r,o,y,g,b,v;;
    cin>>t;
    while(t--)
    {
        cout<<"Case #"<<c<<": ";
        c++;

        cin>>n>>r>>o>>y>>g>>b>>v;
        pair<int,char> prr[3];
        prr[0]=mp(r,'R');
        prr[1]=mp(y,'Y');
        prr[2]=mp(b,'B');
        sort(prr,prr+3);

        int cnt=1;
        int maxx=prr[2].first;
        if(prr[1].first==maxx){
           cnt++;
        }
        if(prr[0].first==maxx)
            cnt++;
        if(cnt==3){
            for(int i=1;i<=maxx;i++){
                cout<<"RBY";
            }
            cout<<endl;
        }

        else if(cnt==2){
            for(int i=1;i<=prr[0].first;i++){
                cout<<prr[2].second<<prr[1].second<<prr[0].second;
                maxx--;
            }
            for(int i=1;i<=maxx;i++){
                cout<<prr[2].second<<prr[1].second;
            }
            cout<<endl;

        }
        else{
            if(prr[0].first+prr[1].first<maxx)cout<<"IMPOSSIBLE";
            else{
                int l=(maxx-prr[1].first);
                int sec=0;
                for(int i=1;i<=prr[0].first-l;i++){
                    cout<<prr[2].second<<prr[1].second<<prr[0].second;
                    sec++;
                }
                for(int i=sec+1;i<=prr[1].first;i++){
                    cout<<prr[2].second<<prr[1].second;
                }
                for(int i=1;i<=l;i++){
                    cout<<prr[2].second<<prr[0].second;
                }

            }
            cout<<endl;
        }
    }
    return 0;
}
