#include <bits/stdc++.h>
using namespace std;

void displayVec(vector<int>&arr){
    for(vector<int>::iterator it=arr.begin();it!=arr.end();++it)
        cout<<(*it)<<" ";
    cout<<endl;
}
long long int getNum(vector<int>&arr,int sz){
    long long int res=0;
    for(int i=sz-1;i>=0;i--)
        res=(res*10)+arr[i];
    return res;
}
int main(){
    int tests,r,n,i;
    long long int el;
    vector<int> arr;
    scanf("%d",&tests);
    for (int test=0;test<tests;++test){
        scanf("%lld",&el);
        n=0;
        while(el>0){
            arr.push_back(el%10);
            el/=10;
            n++;
        }
        //displayVec(arr);
        i=n-1;
        while(i>0 && arr[i]<=arr[i-1])
            i--;
        if(i!=0){
             //cout<<"i is "<<i<<endl;
            while(i<n-1 && arr[i]==arr[i+1])
                i++;
            //cout<<"enhanced i is "<<i<<endl;
            for(int j=0;j<i;j++)
                arr[j]=9;
            arr[i]--;
        }
        //displayVec(arr);
        arr.clear();
        cout<<"Case #"<<test+1<<": "<<getNum(arr,n)<<"\n";
    }
}
