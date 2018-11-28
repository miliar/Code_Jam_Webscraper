#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <tuple>
#include <cmath>
using namespace std;
typedef pair<int,int> P;
typedef tuple<int,int,int> T;

vector<string> S;

void rec(int r, int R, int c, int C){
    int cnt=0;char ch;
    int CNT_R[R],CNT_C[C];
    fill(CNT_R,CNT_R+R,0);
    fill(CNT_C,CNT_C+C,0);
    for(int i=r;i<R;i++){
        for(int j=c;j<C;j++){
            if(S[i][j]!='?'){
                cnt++;
                CNT_R[i]++;
                CNT_C[j]++;
                ch=S[i][j];
            }
        }
    }
    if(cnt==1){
        for(int i=r;i<R;i++){
            for(int j=c;j<C;j++){
                S[i][j]=ch;
            }
        }
        return;
    }else{
        for(int i=r;i<R;i++){
            if(CNT_R[i]&&CNT_R[i]!=cnt){
                rec(r,i+1,c,C);
                rec(i+1,R,c,C);
                return;
            }
        }
        for(int j=c;j<C;j++){
            if(CNT_C[j]&&CNT_C[j]!=cnt){
                rec(r,R,c,j+1);
                rec(r,R,j+1,C);
                return;
            }
        }
    }
}

int main(){
    int T;
    cin>>T;
    for(int t=1;t<=T;t++){
        int R,C;
        cin>>R>>C;
        S = vector<string>(R);
        for(int i=0;i<R;i++){
            cin>>S[i];
        }
        rec(0,R,0,C);
        cout<<"Case #"<<t<<':'<<endl;
        for(int i=0;i<R;i++){
            cout<<S[i]<<endl;
        }
    }

    return 0;
}