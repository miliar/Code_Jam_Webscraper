#include<iostream>
#include<vector>
using namespace std;
int main(){
    int t;
    cin>>t;
    for(int k=0;k<t;k++){
        long long int n;
        vector<int> arr;
        cin>>n;
        while(n>0){
            arr.push_back(n%10);
            n/=10;
        }
        for(int i=0;i<arr.size()-1;i++){
            if(arr[i]<arr[i+1]){
                int j = i;
                while(j>=0&&arr[j]!=9){
                    arr[j]=9;
                    j--;
                }
                arr[i+1]--;
            }
        }
        int j = arr.size()-1;
        if(arr[j]==0)
            j--;
        cout<<"Case #"<<k+1<<": ";
        while(j>=0){
            cout<<arr[j];
            j--;
        }

        cout<<endl;
    }
}
