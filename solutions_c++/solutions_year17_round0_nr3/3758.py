#include <bits/stdc++.h>

using namespace std;

const int N = 1e8+111;

int t;
int n, k;

pair<int,int> P[N];

bool cmp(pair<int,int> a, pair<int,int> b){
    if(a.first==b.first) return a.second>b.second;
    return a.first>b.first;
}

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0);
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    freopen("C-small-2-attempt3.in", "r", stdin);
    freopen("C.out", "w", stdout);
    //freopen("sub-10.in", "r", stdin);
    //freopen("sub-10.out", "w", stdout);
    cin>>t;
    for(int tt = 1; tt <= t; tt++){

        cin>>n>>k;
        P[1].first = n/2;
        P[1].second = n-n/2-1;
        int cou = 2;
        int base = 0;
        int turn = 0;
        if(k==1){
            cout<<"Case #"<<tt<<": "<<P[1].first<<" "<<P[1].second<<endl;
            continue;
        }
        while(cou<=k){

            sort(P+(1<<base),P+(1<<(base+1)),cmp);
            if(turn==0){
            for(int i = 1<<base; i < 1<<(base+1); i++){
                int x = P[i].first;
                if(x==0){
                    continue;
                }
                P[2*i].first = x/2;
                P[2*i].second = x-x/2-1;

                if(cou==k){
                    cout<<"Case #"<<tt<<": "<<P[2*i].first<<" "<<P[2*i].second<<endl;
                    cou++;
                    break;
                }

                cou++;
            }
            turn = 1-turn;
            }
            else{
            for(int i = 1<<base; i < 1<<(base+1); i++){
                int x = P[i].second;
                if(x==0){
                    continue;
                }
                P[2*i+1].first = x/2;
                P[2*i+1].second = x-x/2-1;

                if(cou==k){
                    cout<<"Case #"<<tt<<": "<<P[2*i+1].first<<" "<<P[2*i+1].second<<endl;
                    cou++;
                    break;
                }

                cou++;
            }
            turn = 1-turn;
            base++;
            }
        }
        cerr<<"Case #"<<tt<<" ok"<<endl;
    }
    return 0;
}
