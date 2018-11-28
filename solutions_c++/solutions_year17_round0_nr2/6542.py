#include<iostream>
#include<math.h>
#include<cmath>
using namespace std;
int main(){
  long int t,n;
  cin>>t;
  int iteration=1;
  while(iteration<=t){
    cin>>n;
    int arr[20],size=0;
    int divider=10;
    while((n/divider)!=0){
      arr[size++]=(n%divider);
      n=(n/divider);
    }
    arr[size++]=n;
    for(int i=size-1;i>0;i--){
      // cout<<"main loop"<<endl;
      if(arr[i]>arr[i-1]){
        // cout<<"condn true"<<endl;
        arr[i]--;
        if(arr[i]<arr[i+1] && i+1!=size){
            int value=arr[i+1],itr=i+1;
            // cout<<itr<<endl;
            while(itr<size && arr[itr]==value){
              itr++;
            }
            // cout<<itr<<endl;
            arr[itr-1]--;
            for(int j=itr-2;j>=0;j--){
              arr[j]=9;
            }

        }
        else{
          for(int j=i-1;j>=0;j--){
            arr[j]=9;
          }
        }

      }
    }

    long int newno=0;
    for(int i=size-1;i>=0;i--){
      // cout<<arr[i]<<" ";
      newno=newno*10+arr[i];
      // cout<<newno<<endl;
    }
    // cout<<endl;
    cout<<"case #"<<iteration++<<": "<<newno<<endl;
  }
  return 0;
}
