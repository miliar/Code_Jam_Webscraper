#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>


using namespace std;


int main() {
    
    long long unsigned int t,n,val; cin>>t; int num=0;
    
    while(t--){
        vector <int> arr;
        cin>>n;
        while(n>9){
            val=n%10;
            n=n/10;
            if(n%10>val || val==0){
                arr.push_back(9);
                for(int i=0;i<arr.size();i++) arr[i]=9;
                n--;
            }
            else arr.push_back(val);
        }
        if(n!=0) arr.push_back(n);
        cout<<"Case #"<<++num<<": ";
        for(int i=arr.size()-1;i>=0;i--) cout<<arr[i];
        cout<<endl;
        
    }
    
    
    return 0;
}
