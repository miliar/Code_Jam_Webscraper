#include<bits/stdc++.h>

#define ull unsigned long long int
#define lli long long int
#define li long int
#define mp make_pair
#define pb push_back
#define ft first
#define sc second

#define Tr(S) printf(S);

using namespace std;
const int MAX = 1e5+5;

vector<pair<int, pair<int,int> > > V;   //(.,(.,1)) Jamie else Cameron

int main(){
    freopen("B-large (2).in", "r", stdin);
    freopen("B-large (2).out", "w", stdout);

    int T, Ac, Aj;
    cin>>T;
    for(int z=1;z<=T;z++){
        cin>>Ac>>Aj;
        int Ccnt = 0;
        while(Ac--){
            int st,en;
            cin>>st>>en;
            Ccnt += (en - st);
            V.pb(mp(st,mp(en, 0)));
        }

        int Jcnt = 0;
        while(Aj--){
            int st,en;
            cin>>st>>en;
            Jcnt += (en - st);
            V.pb(mp(st,mp(en,1)));
        }

        sort(V.begin(), V.end());

        int ans=0;
        vector<int> Cdiff, Jdiff;
        for(int i=1;i<V.size();i++){
            if(V[i].sc.sc != V[i-1].sc.sc){
                ans += 1;
            }
            else if(V[i].sc.sc == 0){
                Cdiff.pb(V[i].ft - V[i-1].sc.ft);
            }
            else if(V[i].sc.sc == 1){
                Jdiff.pb(V[i].ft - V[i-1].sc.ft);
            }
        }

        sort(Cdiff.begin(),Cdiff.end());
        sort(Jdiff.begin(),Jdiff.end());

        Ccnt = 720 - Ccnt;
        int i;
        for(i=0;i<Cdiff.size();i++){
            if(Cdiff[i]>Ccnt)
                break;
            Ccnt -= Cdiff[i];
        }

        ans += ((Cdiff.size() - i)*2);

        Jcnt = 720 - Jcnt;
        int j;
        for(j=0;j<Jdiff.size();j++){
            if(Jdiff[j]>Jcnt)
                break;
            Jcnt -= Jdiff[j];
        }

        ans += ((Jdiff.size() - j)*2);

        int N = V.size();
        if(V[0].sc.sc != V[N-1].sc.sc){
            ans += 1;
        }
        else if(V[N-1].sc.sc == 0){
            if(1440-V[N-1].sc.ft + V[0].ft > Ccnt){
                ans += 2;
            }
        }
        else if(V[N-1].sc.sc == 1){
            if(1440-V[N-1].sc.ft + V[0].ft > Jcnt){
                ans += 2;
            }
        }


        /*cout << "Times: \n";
        for(int i=0;i<V.size();i++){
            cout << "Start time = ";
            cout << V[i].ft/60 << " : " << V[i].ft%60 << "\t";
            cout << "End time = " ;
            cout << V[i].sc.ft/60 << " : " << V[i].sc.ft%60 << "\t";
            cout << "Turn = " << V[i].sc.sc << "\n";
        }

        int prev=-1;
        int ans=0;
        for(int i=0;i<V.size();i++){
            int Turn = V[i].sc.sc;
            if(prev==-1)
                prev = V[i].sc.sc;
            else if(Turn != prev){
                prev = 1 - prev;
                ans += 1;
            }
        }*/

        cout << "Case #" << z << ": ";
        cout << ans << "\n";
        V.clear(); Cdiff.clear(); Jdiff.clear();
    }


    return 0;
}
