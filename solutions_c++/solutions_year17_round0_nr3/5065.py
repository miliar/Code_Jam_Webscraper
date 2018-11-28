

#include <cmath>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <iostream>
#include <string>
#include <queue>


using namespace std;

void splitStallRow(std::priority_queue<int> &q, std::string& maxMinString){
    
    int queueTop = q.top();
    q.pop();
    int max, min;
    maxMinString = "";
    if(queueTop%2 == 1){
        min = floor(queueTop/2);
        max = floor(queueTop/2);
        q.push(min);
        q.push(max);
    }
    else{
        min = (queueTop/2)-1;
        max = queueTop/2;
        q.push(min);
        q.push(max);
    }
    
    maxMinString = std::to_string(max) + " " + std::to_string(min);
    
}

std::string bathroomStalls(int N, int K){
    
    
    std::priority_queue<int> q;
    std::string maxMinString = "";
    q.push(N);
    
    for (int i=1; i<=K; i++) {
        splitStallRow(q,maxMinString);
    }
    
    return maxMinString;
}


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    
    
    int T;
    int N;
    int K;
    cin>> T;
    
    for(int i =1 ; i<=T;i++){
        cin >> N;
        cin >> K;
        cout << "Case #" << i << ": " << bathroomStalls(N, K)<< endl;
        
    }
    
    
    
    
    return 0;
}

