#include <iostream>
#include <vector>

using namespace std;

int main(){
    int tt;
    cin>>tt;
    for(int t=1;t<=tt;t++){
        int r,c;
        cin>>r>>c;
        char arr[r][c];
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                cin>>arr[i][j];
            }
        }
        bool onceMore=true;
        cout<<"Case #"<<t<<":"<<endl;
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                for(int k=j;k>=0;k--){
                    if(arr[i][k]!='?'){
                        arr[i][j]=arr[i][k];
                        break;
                    }
                }
                for(int k=j;k<c;k++){
                    if(arr[i][k]!='?'){
                        arr[i][j]=arr[i][k];
                        break;
                    }
                }
            }
        }
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                for(int k=i;k>=0;k--){
                    if(arr[k][j]!='?'){
                        arr[i][j]=arr[k][j];
                        break;
                    }
                }
                for(int k=i;k<r;k++){
                    if(arr[k][j]!='?'){
                        arr[i][j]=arr[k][j];
                        break;
                    }
                }
            }
        }
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++)cout<<arr[i][j];
            cout<<endl;
        }
    }
    return 0;
}