#include <iostream>
using namespace std;
int arr[100000000];
int check(int n){
    int count=0;
    for(int i=0;i<n-1;i++){
        if(arr[i]>arr[i+1])
        {
            count=1;
            break;
        }
    }
    if(count==0)
        return 0;
    else
        return 1;

}
void change1(int n){

           arr[n - 1] = 9;
           arr[n - 2] -= 1;
           if (arr[n - 2] < 0)
               arr[n - 2] += 10;
    if(check(n-1))
       change1(n-1);
    else {
       return;
   }
}
int main() {
    freopen("B-small-attempt3.in","r",stdin);
   freopen("output.txt","w",stdout);
    int t;
    long long int n;
    cin>>t;
    for(int i=1;i<=t;i++){
        cin>>n;
        int j=0;
        while(n>0){
            arr[j++]=n%10;
            n=n/10;
        }
        for(int k=0;k<j/2;k++){
            int t;
         //   cout<<arr[k];
            t=arr[k];
            arr[k]=arr[j-k-1];
            arr[j-k-1]=t;
         //   cout<<arr[k];
        }
       //cout<<endl;
        if(check(j)) {
            int m=0;
            int first=arr[0];
            change1(j);
           if(arr[1]==9)
                if(arr[0]>0&&arr[0]==first)
                arr[0]-=1;

            while(arr[m]==0)
                m++;
           cout << "Case #" << i << ":" << " ";
            for (int k=m; k < j; k++)
                cout << arr[k];
            cout << endl;
        }
        else {
            cout << "Case #" << i << ":" << " ";
            for (int k = 0; k < j; k++)
                cout << arr[k];
            cout << endl;
        }
    }
    return 0;
}