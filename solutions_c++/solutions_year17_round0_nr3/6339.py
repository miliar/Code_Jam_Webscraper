#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <queue>
#include <bits/stdc++.h>
using namespace std;

int main(){
    //freopen("Input.txt", "r", stdin);
    freopen("C-small-2-attempt0.in", "r", stdin);
    //freopen("C-large.in", "r", stdin);
    freopen("OutputC.txt", "w", stdout);

    int T;
    cin>>T;
    unsigned long long N,K;
    for(int i=1;i<=T;i++){
        priority_queue<int> elements;
        cin>>N>>K;
        if(N == K)
            cout<<"Case #"<<i<<": 0 0"<<endl;
        else{
            elements.push(N);
            int temp , mid;
            for(int j=0;j<K-1;j++){
                temp = elements.top();
                elements.pop();
                mid = (temp-1)/2;
                elements.push(mid);
                elements.push(temp-mid-1);
            }
            temp = elements.top();
            elements.pop();
            mid = (temp-1)/2;
            //elements.push(mid);
            //elements.push(temp-mid-1);
            int left = mid, right = temp-mid-1;
            cout<<"Case #"<<i<<": "<<max(left,right)<<" "<<min(left,right)<<endl;
        }
    }
    return 0;
}

