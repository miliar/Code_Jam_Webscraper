#include<iostream>
#include<vector>
#define INF 0x3f3f3f3f
using namespace std;
int main(){
    int t, n, temp, pre, y;
    vector<int> vec;
    cin>>t;
    for(int ii = 1; ii <= t; ii++){
        cin>>n;
        temp = n;
        pre = INF;
        int i = 1;
        while(temp){
            y = temp%10;
            temp = temp/10;
            if(y > pre){
                temp = n = n-1;
                pre = INF;
            }
            else{
                pre = y;
            }
        }
        vec.push_back(n);
    }
    for(int i = 0; i < vec.size(); i++){
        cout<<"Case #"<<i+1<<": "<<vec.at(i)<<endl;
    }
}
