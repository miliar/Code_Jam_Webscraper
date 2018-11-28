#include <iostream>
using namespace std;
char arr[32][32];
int tc,r,c;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cin>>tc;
    for(int ct=1;ct<=tc;++ct){
        cin>>r>>c;
        for(int i=0;i<r;++i){
            for(int j=0;j<c;++j){
                cin>>arr[i][j];
            }
        }
        for(int i=0;i<r;++i){
            for(int j=0;j<c;++j){
                if(j>0&&arr[i][j]=='?'&&arr[i][j-1]!='?'){
                    arr[i][j]=arr[i][j-1];
                }
            }
            for(int j=c-1;j>=0;--j){
                if(j<c-1&&arr[i][j]=='?'&&arr[i][j+1]!='?'){
                    arr[i][j]=arr[i][j+1];
                }
            }
        }
        for(int i=0;i<r;++i){
            if(i>0&&arr[i][0]=='?'&&arr[i-1][0]!='?'){
                for(int j=0;j<c;++j){
                    arr[i][j]=arr[i-1][j];
                }
            }
        }
        for(int i=r-1;i>=0;--i){
            if(i<r-1&&arr[i][0]=='?'&&arr[i+1][0]!='?'){
                for(int j=0;j<c;++j){
                    arr[i][j]=arr[i+1][j];
                }
            }
        }
        cout<<"Case #"<<ct<<":"<<endl;
        for(int i=0;i<r;++i){
            for(int j=0;j<c;++j){
                cout<<arr[i][j];
            }
            cout<<endl;
        }
    }
}

