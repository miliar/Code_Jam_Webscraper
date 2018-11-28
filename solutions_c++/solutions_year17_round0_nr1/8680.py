#include<iostream>
using namespace std;
int main(){
    int T;
    cin>>T;
    char pancake[100][1000];
    int flipper[100];
    int counts[100];
    int length[100];
    for(int i=0;i<T;i++)
    {
        cin>>pancake[i]>>flipper[i];
        length[i]=strlen(pancake[i]);
    }
    for(int i=0;i<T;i++){
            counts[i]=0;
        for(int j=0;j<length[i];j++){
            if(pancake[i][j]=='-'){
                if(j>strlen(pancake[i])-flipper[i])
                    counts[i]=-1;
                else{
                    for(int m=0;m<flipper[i];m++){
                        pancake[i][j+m]=(pancake[i][j+m]=='-')?'+':'-';
                    }
                    counts[i]++;
                }
            }
        }
    }
    for(int i=0;i<T;i++){
        cout<<"Case #"<<i+1<<": ";
        if(counts[i]==-1)
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<counts[i]<<endl;
    }
   // cout<<strlen(pancake[0])<<flipper[0];
    return 0;
}
