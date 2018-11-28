#include<iostream>
#include<cstdio>
using namespace std;
char m1[32][32];
char m2[32][32];
int main(){
      freopen("A-large.in","r",stdin);
    freopen("A.txt","w",stdout);
    int cas,q;
    cin>>cas;
    for(int q = 1; q <= cas; q++){
        int r,c;
        cin>>r>>c;
        for(int i = 0; i < r; i++){cin>>m1[i];}

        for(int i = 0; i < r; i++)
            for(int j = 0; j < c; j++)m2[i][j] = m1[i][j];

        for(int i = 0; i < r; i++)
            for(int j = 0; j < c; j++){

                if(m1[i][j] != '?'){
                    int left,right,up,down;
                    left = j - 1; right = j+1;
                    while(left>=0){
                        if(m2[i][left]=='?'){
                            left--;
                        }
                        else break;
                    }
                    while(right < c){
                        if(m2[i][right]=='?'){
                            right++;
                        }
                        else break;
                    }
                    for(down = i-1; down >= 0; down--){
                        bool ok = true;
                        for(int q = left+1; q < right; q++){
                            if(m2[down][q] != '?')ok = false;
                        }
                        if(!ok) break;
                    }
                    for(up = i+1; up < r; up++){
                        bool ok = true;
                        for(int q = left+1; q < right; q++){
                            if(m2[up][q] != '?')ok = false;
                        }
                        if(!ok) break;
                    }

                    for(int k = down+1; k < up; k++){
                        for(int q = left+1; q < right; q++)m2[k][q] = m1[i][j];
                    }
                }
            }
        cout<<"Case #"<<q<<":"<<endl;
        for(int i = 0 ;i < r; i++){
            for(int j = 0; j < c; j++)cout<<m2[i][j];
            cout<<endl;
        }
    }

    return 0;
}

