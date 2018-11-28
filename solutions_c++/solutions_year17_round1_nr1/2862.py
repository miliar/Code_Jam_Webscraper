#include <bits/stdc++.h>
#define _CRT_SECURE_NO_DEPRECATE
#define REP(i, a, b) for (int i = int(a); i <= int(b); i++)
#define LSOne(S) (S & (-S))

using namespace std;
typedef pair<int, int> ii;
typedef pair<ii,ii> pp;



char arr[27][27];
int x[27],y[27],z[27],v[27];
int main(){
    int t,n,r,c;
    cin>>t;
    //scanf("%d",&t);
    for(int tc= 1;tc <= t;tc++){
        std::vector<std::vector<ii> > V;
        //V.clear();
        V.resize(30);
        //scanf("%d %d",&r,&c);
        cin>>r>>c;
        memset(arr,'?',sizeof(arr));
        REP(i,1,r){
            REP(j,1,c){
                cin>>arr[i][j];
                if(arr[i][j] != '?')V[arr[i][j] - 'A'].push_back(ii(i,j));
            }
        }
        REP(i,0,25){
            if(V[i].size() == 0)continue;
            int l,r,u,d;
            l = d = 150;
            r = u = -1;
            for(int j = 0;j < V[i].size();j++){
                l = min(l,V[i][j].second);
                r = max(r,V[i][j].second);
                d = min(d,V[i][j].first);
                u = max(u,V[i][j].first);
            }
            x[i] = l;y[i] = r;z[i] = u;v[i] = d;
            for(int j = d;j <= u;j++){
                for(int k = l;k <= r;k++){
                    arr[j][k] = char(i+65);
                }
            }
        }
        
        bool fl = 0;
        while(!fl){
            fl = 1;
            REP(i,1,r){
                REP(j,1,c){
                    bool zz = 0;
                    if(arr[i][j] == '?'){
                        //cerr<<i<<' '<<j<<endl;
                        if(arr[i-1][j] != '?' && !zz){
                            REP(k,x[arr[i-1][j]-'A'],y[arr[i-1][j]-'A']){
                                if(arr[i][k] != '?')zz = 1;
                            }
                            if(!zz){
                                zz = 1;
                                REP(k,x[arr[i-1][j]-'A'],y[arr[i-1][j]-'A'])arr[i][k] = arr[i-1][j];
                                z[arr[i-1][j] - 'A'] += 1;
                            }
                            else zz = 0;  
                        } 
                        if(arr[i+1][j] != '?' && !zz){
                            //if(i == 3 && j == 2)cerr<<"In2\n";
                            REP(k,x[arr[i+1][j]-'A'],y[arr[i+1][j]-'A']){
                                if(arr[i][k] != '?')zz = 1;
                            }
                            if(!zz){
                                zz = 1;
                                REP(k,x[arr[i+1][j]-'A'],y[arr[i+1][j]-'A'])arr[i][k] = arr[i+1][j];
                                v[arr[i+1][j] - 'A'] -= 1;
                            }
                            else zz = 0;
                        }
                        if(arr[i][j-1] != '?' && !zz){
                            //if(i == 3 && j == 2)cerr<<"In3\n";
                            REP(k,v[arr[i][j-1]-'A'],z[arr[i][j-1]-'A']){
                                if(arr[k][j] != '?')zz = 1;
                            }
                            if(!zz){
                                zz = 1;
                                REP(k,v[arr[i][j-1]-'A'],z[arr[i][j-1]-'A'])arr[k][j]  = arr[i][j-1];
                                y[arr[i][j-1] - 'A'] += 1;
                            } 
                            else zz = 0; 
                        }
                        if(arr[i][j+1] != '?' && !zz){
                            //if(i == 3 && j == 2)cerr<<"In\n";
                            REP(k,v[arr[i][j+1]-'A'],z[arr[i][j+1]-'A']){
                                if(arr[k][j] != '?')zz = 1;
                            }
                            if(!zz){
                                zz = 1;
                                REP(k,v[arr[i][j+1]-'A'],z[arr[i][j+1]-'A'])arr[k][j]  = arr[i][j+1];
                                x[arr[i][j+1] - 'A'] -= 1;
                            } 
                            else zz = 0; 
                        }
                        if(zz == 0)fl = 0;
                        // REP(ii,1,r){
                        //     REP(jj,1,c){
                        //         cout<<arr[ii][jj];
                        //     }
                        //     cout<<"\n";
                        // }
                        //cerr<<x[arr[i]-'A']<<' '<<y[arr[i] - 'A']
                    }
                }
            }
        }

        cout<<"Case #"<<tc<<":\n";
        REP(i,1,r){
            REP(j,1,c){
                cout<<arr[i][j];
            }
            cout<<"\n";
        }
    }
    return 0;
}