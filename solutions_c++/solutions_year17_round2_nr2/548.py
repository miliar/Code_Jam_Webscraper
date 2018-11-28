#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<stdlib.h>
using namespace std;

int main(){
    int TT;
    cin>>TT;
    int n;
    int r,o,y,g,b,v;
    for(int T=1;T<=TT;++T){
        cin>>n>>r>>o>>y>>g>>b>>v;
        cout<<"Case #"<<T<<": ";
        int p[3];
        p[0]=r;
        p[1]=y;
        p[2]=b;
        char a[3]={'R','Y','B'};
        //cout<<a[0]<<" "<<a[1]<<" "<<a[2]<<endl;
        //cout<<p[0]<<" "<<p[1]<<" "<<p[2]<<endl;

        for(int i=0;i<3;++i){
            for(int j=i+1;j<3;++j){
                if(p[i]<p[j]){
                    char tc=a[i];
                    a[i]=a[j];
                    a[j]=tc;
                    int tp=p[i];
                    p[i]=p[j];
                    p[j]=tp;
                }
            }
        }
        if(p[1]+p[2]<p[0]){
            cout<<"IMPOSSIBLE";
        }
        else{
            vector<char> v;
            int s=p[2]+p[1]-p[0];
            p[2]-=s;
            for(int i=0;i<p[0];++i){
                cout<<a[0];
                if(p[1]>0){
                    cout<<a[1];
                    --p[1];
                }
                else{
                    cout<<a[2];
                    --p[2];
                }
                if(s>0){
                    cout<<a[2];
                    --s;
                }
            }
        }
        //cout<<a[0]<<" "<<a[1]<<" "<<a[2]<<endl;
        //cout<<p[0]<<" "<<p[1]<<" "<<p[2]<<endl;
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
