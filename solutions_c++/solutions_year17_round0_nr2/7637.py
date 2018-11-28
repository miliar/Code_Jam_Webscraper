#include<bits/stdc++.h>
using namespace std;

int main(){
    freopen("Blarge.txt", "r", stdin);
    freopen("Blarge_out.txt", "w", stdout);
    int T;
    cin>>T;
    for(int t=1 ; t<=T ; ++t){
        long long in, cpy;
        vector<int> arr;
        cin>>in;
        cout<<"Case #"<<t<<": ";
        cpy = in;
        while(in){
            arr.push_back(in%10);
            in /= 10;
        }
        reverse(arr.begin(), arr.end());
        int pos = -1;
        for(int i=1 ; i<arr.size() ; ++i)
            if(arr[i]<arr[i-1]){
                pos = i-1;
                break;
            }
        if(pos == -1){
            cout<<cpy<<endl;
            continue;
        }
        while(pos>=1 && arr[pos] == arr[pos-1])
            pos--;
        arr[pos]--;
        for(int i=pos+1 ; i<arr.size() ; ++i)
            arr[i] = 9;
        in = 0;
        for(int i=0 ; i<arr.size() ; ++i){
            in *= 10LL;
            in += arr[i];
        }
        cout<<in<<endl;
    }
}
