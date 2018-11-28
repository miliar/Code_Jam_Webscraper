#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<stdlib.h>
#include<iomanip>
using namespace std;

int main(){
    int TT;
    cin>>TT;
    int n,q;
    long double e[200];
    long double s[200];
    long double d[200][200];
    long double dd[200][200];
    long double ht[200][200];
    int u,v;
    for(int T=1;T<=TT;++T){
        cin>>n>>q;
        for(int i=0;i<n;++i){
            cin>>e[i]>>s[i];
        }
        for(int i=0;i<n;++i){
            for(int j=0;j<n;++j){
                cin>>d[i][j];
            }
        }
        for(int i=0;i<n;++i){
            for(int j=0;j<n;++j){
                dd[i][j]=-1;
                ht[i][j]=-1;
            }
        }
        for(int i=0;i<n;++i){
            d[i][i]=0;
            dd[i][i]=0;
            ht[i][i]=0;
        }

        bool g=true;
        for(int l=0;l<=n;++l){
            g=true;
            for(int i=0;i<n;++i){
                for(int j=0;j<n;++j){
                    for(int k=0;k<n;++k){
                        if(d[i][k]>=0&&dd[k][j]>=0){
                            long double tmp =d[i][k]+dd[k][j];
                            if(dd[i][j]<0||tmp<dd[i][j]){
                                dd[i][j]=tmp;
                                g=false;
                            }
                        }
                    }
                }
            }
            if(g)
                break;
        }
        //cout<<"dd mat"<<endl;
        //for(int i=0;i<n;++i){
        //    for(int j=0;j<n;++j){
        //        cout<<dd[i][j]<<" ";
        //    }
        //    cout<<endl;
        //}

        for(int l=0;l<=n;++l){
            g=true;
            for(int i=0;i<n;++i){
                for(int j=0;j<n;++j){
                    for(int k=0;k<n;++k){
                        if(dd[i][k]>=0&&dd[i][k]<=e[i]&&ht[k][j]>=0){
                            long double tmp =dd[i][k]/s[i]+ht[k][j];
                            if(ht[i][j]<0||tmp<ht[i][j]){
                                ht[i][j]=tmp;
                                g=false;
                            }
                        }
                    }
                }
            }
            if(g)
                break;
        }
        //cout<<"ht mat"<<endl;
        //for(int i=0;i<n;++i){
        //    for(int j=0;j<n;++j){
        //        cout<<ht[i][j]<<" ";
        //    }
        //    cout<<endl;
        //}
        cout<<"Case #"<<T<<": ";
        //cout<<"n = "<<n<<endl;
        for(int i=1;i<=q;++i){
            cin>>u>>v;
            cout<<fixed;
            cout<<setprecision(8)<<ht[u-1][v-1];
            if(i!=q)
                cout<<" ";
        }
        cout<<endl;
        
    }
    return 0;
}




//map<int,int> mp;
//for(int i=0;i<10;++i){
//    mp.insert(make_pair(i,0));
//}
//for(auto it=mp.begin();it!=mp.end();++it){
//    cout<<it->first;
//}
