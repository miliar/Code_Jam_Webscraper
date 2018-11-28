#include <iostream>
#include <vector>
using namespace std;

int N,K;

int update(int arr[][2], bool exist[]){
    int maxminlr = 0;
    int lind=0;
    for(int k=0;k<N+1;k++){
        if(exist[k]){
            lind=k;
        }
        arr[k][0]=k-lind;
    }
    
    int rind=N+1;
    for(int k=N+1;k>0;k--){
        if(exist[k]){
            rind=k;
        }
        arr[k][1]=rind-k;
        maxminlr = max(maxminlr, min(arr[k][0], arr[k][1]));
    }
    return maxminlr;
}

int main(){
    int T;
    cin>>T;

    for(int i=0;i<T;i++){
        cin>>N>>K;
        
        
        bool exist[1003]={};
        int arr[1003][2]={};
        
        
        
        exist[0]=exist[N+1]=true;
        int lasti=0;
        for(int c=0;c<K;c++){
            
            int maxminlr = update(arr, exist);

            vector<int> sets;
            int maxmaxlr = 0;
            
            for(int k=1;k<N+1;k++){
                if(maxminlr == min(arr[k][0], arr[k][1])){
                    sets.push_back(k);
                    maxmaxlr = max(maxmaxlr, max(arr[k][0], arr[k][1]));
                }
            }
            if(sets.size()==1){
                exist[sets[0]]=true;
                lasti = sets[0];
            }
            else {
                for(int k=0;k<sets.size();k++){
                    if(maxmaxlr == max(arr[sets[k]][0], arr[sets[k]][1])){
                        exist[sets[k]]=true;
                        lasti = sets[k];
                        break;
                    }
                }
            }
            
            //for(int x=0;x<N+2;x++){
                //if(exist[x])cout<<0;
                //else cout<<'.';
            //}
            //cout<<endl;
        }
        
        //update(arr, exist);
        cout<<"Case #"<<i+1<<": "<<max(arr[lasti][0], arr[lasti][1])-1<<" "<<min(arr[lasti][0], arr[lasti][1])-1<<endl;
        

    }
    return 0;
}
