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

vector<pair<int,char>> M;

char Al[] = {'R', 'O', 'Y', 'G', 'B', 'V'};
vector<char> V;
vector<int> inp;

void pre(){
    int N = inp.size();
    inp.clear();
    for(int i=0;i<N;i+=2){
        inp.pb(i);
    }
    for(int i=1;i<N;i+=2){
        inp.pb(i);
    }
}

int main(){
    freopen("B-small-attempt2.in", "r", stdin);
    freopen("B-small-attempt2.out", "w", stdout);

    int T,N;
    bool isAns;
    cin>>T;
    for(int x=1;x<=T;x++){
        isAns = 1;
        cin>>N;
        for(int i=0;i<6;i++){
            int tmp;
            cin>>tmp;
            M.pb(mp(tmp,Al[i]));
        }

        cout << "Case #"<< x << ": ";
        sort(M.begin(),M.end());


        if(M[5].ft>(N>>1)){
            cout<<"IMPOSSIBLE\n"; isAns = 0;
            //continue;
        }

        inp.resize(N); V.resize(N);
        pre();
        //cout<<inp.size() << "<--------------------------------------\n";
        int start = 0;
        for(int i=5;i>=0;i--){
            for(int j=0;j<M[i].ft;j++){
                V[inp[start]] = M[i].sc;
                start += 1;
            }

            /*if(M[i].ft>0 && start<inp.size()){
                /*int cnt=0;
                while(M[i].ft>0){
                    V[inp[start]] = M[i].sc;
                    //cout << M[i].sc << "\tsdksjd\n";
                    M[i].ft -= 1; start += 1;
                    cnt++;
                    if(cnt>1500)
                        break;
                }
                if(cnt>1500){
                    cout << "Kaaaaaaaaaaaaaaaand ho gaya\n";
                }
            }*/
        }
        if(isAns){
            for(int i=0;i<N;i++){
                cout << V[i];
            }
            cout<<"\n";
        }

        M.clear();
        inp.clear();
        V.clear();

    }

    return 0;
}
