#include<iostream>
#include<cstdio>
#define lld long long int
using namespace std;

int arr[21];

int* getDigits(lld n){
    int k=0;
    while(n){
        arr[k++]=n%10;
        n=n/10;
    }
    arr[k]=-1;
    arr[20]=k-1;
return arr;
}

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=0;i<t;i++){
        lld n;
        bool isTidy=false;
        cin>>n;
        if(n/10==0){
            cout<<"Case #"<<(i+1)<<": "<<n<<endl;
        }
        else{
            getDigits(n);
            for(int j=arr[20];!isTidy;j--){
                if(j==0){
                    j=arr[20];
                }
                if(arr[j]>arr[j-1]){
                    arr[j]=arr[j]-1;
                    int k=j-1;
                    while(k>=0){
                        arr[k]=9;
                        k--;
                    }
                }
                if(arr[j]==0 && j==arr[20])
                    arr[20]=arr[20]-1;
                for(int k=arr[20];k>0;k--){
                    if(arr[k]<=arr[k-1])
                    {
                        isTidy=true;
                    }
                    else{
                        isTidy=false;
                        break;
                    }
                }
            }
            cout<<"Case #"<<(i+1)<<": ";
            for(int j=arr[20];j>=0;j--){
                cout<<arr[j];
            }
            cout<<endl;
        }
    }
return 0;
}
