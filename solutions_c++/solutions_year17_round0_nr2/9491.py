#include <iostream>
#include <string>
using namespace std;
int main()
{
    int t;
     cin >> t;
     while(t--){
        char arr[18];
        cin >> arr;
        int i = 0;
        while(arr[i]!='\0'){
            i++;
        }
        int arr1[i];
        for(int j=0;j<i;j++){
            arr1[j]=char(arr[j])-'0';
        }
        int equal=0,j;
        for(j=0;j<i-1;j++){
            if(arr1[j]<arr1[j+1]){
                equal=0;
                continue;
            }

            if(arr1[j]==arr1[j+1]){
                equal++;
                continue;
            }
            else{
                break;
            }


        }
        if(j!=i-1){
        arr1[j - equal]= arr1[j - equal]-1;
    
        for(int k=j+1-equal;k<i;k++){
            arr1[k]=9;
        }  
    }      

        int k;
        for(k=0;k<i;k++){
            if(arr1[k]==0){
                continue;
            }
            else break;
        }

        cout<< "Case #"<<100-t<<": ";
        for(;k<i;k++){            
            cout << arr1[k];
        }
        cout <<endl;

        


    }
}
