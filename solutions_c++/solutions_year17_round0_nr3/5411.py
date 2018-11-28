//
//  main.cpp
//  Problem C
//
//  Created by Twinkle Gupta on 4/7/17.
//  Copyright © 2017 Twinkle Gupta. All rights reserved.
//

#include <iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;
void display(int arr[], int n){
    for(int i = 0;i < n; i++){
        cout<<" : "<<arr[i];
    }
    cout<<endl;
}
int main() {
    int t;
    cin>>t;
    for(int i = 1;i <= t; i++){
        int n,k;
        cin>>n>>k;
        int L[n];
        int R[n];
        for(int j = 0;j < n;j++){
            L[j] = j;
            R[j] = n-1-j;
        }
        //display(L, n);
        //display(R, n);
        int ans;
        while(k--){
            int maxMin = INT_MIN, maxMax = INT_MIN;
            int posMax;
            vector<int> posMin;
            for(int j = 0; j < n; j++){
                if(min(L[j],R[j]) > maxMin) maxMin = min(L[j],R[j]);
            }
            for(int j = 0; j < n; j++){
                if(min(L[j],R[j]) == maxMin) posMin.push_back(j);
            }
            if(posMin.size() == 1) posMax = posMin[0];
            else{
                int vsize = posMin.size();
                for(int j = 0; j < vsize; j++){
                    if(max(L[posMin[j]],R[posMin[j]]) > maxMax) {
                        maxMax = max(L[posMin[j]],R[posMin[j]]);
                        posMax = posMin[j];
                    }
                }
            }
            L[posMax] = -1;
            R[posMax] = -1;
            for(int j = posMax-1; j >= 0 && R[j] != -1 ;j--){
                R[j] = posMax - 1 - j;
            }
            for(int j = posMax + 1;j < n && L[j] != -1;j++){
                L[j] = j - posMax - 1;
            }
            ans = posMax;
            //display(L, n);
            //display(R, n);

        }
        int count1 = 0, count2 = 0;
        for(int j = ans-1; j >= 0 && L[j] != -1 ; j--){
            count1++;
        }
        for(int j = ans+1; j < n && R[j] != -1; j++){
            count2++;
        }
        //cout<<ans<<count1<<count2<<endl;
    
        cout<<"Case #"<<i<<": "<<max(count1,count2)<<" "<<min(count1,count2)<<endl;
    }
    return 0;
}
