#include <cmath>
#include <cstdio>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;



int main() {
    
    int t;
    cin >> t;
    int n;
    int k;
    for(int i = 0; i < t; i++){
        cout<<"Case #"<<i+1<<": ";
        priority_queue<int> s;
        cin >> n>>k;
        s.push(n);
        for(int j=0;j<k;j++){
            int a=s.top();
            if(j==k-1){
                if(a%2==0){
                    cout<<(a/2)<<" ";
                    cout<<(a/2-1);
                }else{
                    cout<<(a/2)<<" ";
                    cout<<(a/2);
                }
            }else{
            s.pop();
                if(a%2==0){
                    s.push(a/2);
                    s.push(a/2-1);
                }else{
                    s.push(a/2);
                    s.push(a/2);
                }
            }
        }
        cout<<endl;
    }
    
    return 0;
}


