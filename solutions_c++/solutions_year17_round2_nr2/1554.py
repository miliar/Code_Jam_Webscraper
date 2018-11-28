#include <bits/stdc++.h>
using namespace std;

#define forn(i,n) for(int i=0;i<n;++i)
#define rforn(i,n) for(int i=n-1;i>=0;--i)
#define y1 gteethegrrwmjtrrtgghnrhthth
#define y2 fgntrhtrhththreggjntghnrtfg


#define ld long double

char tr(int x){
    if(x==1)
        return 'R';
    if(x==2)
        return 'Y';
    if(x==3)
        return 'O';
    if(x==4)
        return 'B';
    if(x==5)
        return 'V';
    if(x==6)
        return 'G';
}

int revv(char x){
    if(x=='R')
        return 1;
    if(x=='Y')
        return 2;
    if(x=='O')
        return 3;
    if(x=='B')
        return 4;
    if(x=='V')
        return 5;
    if(x=='G')
        return 6;
}


set<pair<int,char> > q;
int a[9];


int main(){

    ifstream cin("input.txt");
    ofstream cout("output.txt");
/*
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
*/
    int t;
    cin>>t;

    ld d;
    int n;

    ld k,s;
    ld maxTime;
    ld cTime;

   // cout<<fixed<<setprecision(8);

   // int r,o,y,g,b,v;




    for(int i=1;i<=t;++i){
        cin>>n;
        int c =0;
        cin>>a[1]>>a[3]>>a[2]>>a[6]>>a[4]>>a[5];

        int prev = -1;
        string res;
        cout<<"Case #"<<i<<": ";
        if(a[1]>a[2]+a[4] || a[2]>a[1]+a[4] || a[4]>a[1]+a[2]) {
            cout<<"IMPOSSIBLE\n";
            continue;
        }

        int l =a[1]+a[2]+a[4];
      //  cout<<a[1]<<a[2]<<a[4]<<'\n';
        for(int j=0;j<l;++j){
            if(prev!=1 && (a[1]>=a[2] || prev == 2)&& (a[1]>=a[4] || prev == 4)){
                res.push_back(tr(1));
                --a[1];
                prev = 1;
                continue;
            }
            if(prev!=2 && (a[2]>=a[4] || prev == 4)){
                res.push_back(tr(2));

                --a[2];
                prev = 2;
                continue;
            }
            res.push_back(tr(4));
            --a[4];
            prev = 4;

        }



        if(res[l-1]==res[0])
            swap(res[l-1],res[l-2]);
        if(res[0] == res[l-1] || res[l-2] == res[ (2*l-3)%l] || a[1]!=0 || a[2]!=0||a[4]!=0){
            cout<<"IMPOSSIBLE\n";
            continue;
        }


        cout<<res<<'\n';


        /*
        for(int j=1;j<=6;++j){
           // cin>>a[j];
            c+=(a[j]>0);
        }
        cout<<"Case #"<<i<<": ";
        if(c==1)
        {
            cout<<"IMPOSSIBLE\n";
            continue;
        }

        if(c==2){
            int x,y;
            for(int i=1;i<=6;++i)
                for(int j=i+1;j<=6;++j){
                    if(a[i]>0 && a[j]>0)
                    {
                        x=i;y=j;
                    }
                }

            if(x&y!=0 || a[x]!=a[y])
                cout<<"IMPOSSIBLE\n";

            else
                for(int i=0;i<n/2;++i)
                    cout<<tr(x)<<tr(y)<<'\n';

            continue;
        }

        string res;

        q.insert(make_pair(-a[1],1));
        q.insert(make_pair(-a[2],2));
        q.insert(make_pair(-a[4],4));

        int l = a[1]+a[2]+a[4];

        if(a[1] < a[7^1]+1 || a[2]<a[7^2]+1 || a[4]<a[7^4]+1){
            cout<<"IMPOSSIBLE\n";
            continue;
        }
        a[1]-=a[7^1];
        a[2]-=a[7^2];
        a[4]-=a[7^4];

        for(int i=0;i<l;++i){
            auto g = q.begin();
            q.erase(q.begin());
            if(g.first == 1){
                res.push_back(rev(g.second));
                for(int i=0;i<a[g.second ^ 7];++i){
                    res.push_back(rev(g.second^7));
                    res.push_back(rev(g.second));
                }
            }
        }*/

    }
}
