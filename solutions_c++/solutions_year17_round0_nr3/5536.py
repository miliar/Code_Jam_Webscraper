//
//  main.cpp
//  GoogleCodeJam2017
//
//  Created by Aniket p Ghanawat on 07/04/17.
//  Copyright © 2017 Aniket P Ghanawat. All rights reserved.
//

#include <iostream>
#include <vector>
#include <unordered_map>
#include <list>
#include <algorithm>
#include <string>
#include <cmath>

#define ull unsigned long long
#define ul  unsigned long
using namespace std;

void solutionA(){
    int T,K,count;
    string S;
    unsigned long len;
    bool flg;
    cin >> T;
    for(int i = 1; i <= T; i++){
        cin >> S;
        cin >> K;
        count = 0;
        len = S.length();
        for(int l,j = 0; j < len; j+=K){
            while(S[j] == '+') j++;
            if(j<len){
                flg =false;
                for(l = 0; l < K; l++){
                    if(S[j+l] == '+') continue;
                    else flg = true;
                }
                if (flg){
                    for(l = 0; l < K; l++){
                        if(S[j+l] == '+') S[j+l] = '-';
                        else S[j+l] = '+';
                    }
                    if(j+l > len){
                        count = -1;
                        break;
                    }
                    count++;
                    j -= K;
                }
            }
        }
       // cout << S << " " << K << "\t";
        cout << "Case #"<<i<<": ";
        if(count >= 0) cout << count << endl;
        else cout << "IMPOSSIBLE" << endl;
    }
    
}


void solutionB(){
    int T;
    ull len;
    string num;
    string ans;
    cin >> T;
    for (int i = 1; i <= T; i++){
        cin >> num;
        len = int(num.length());
        ans = "";
        for(int j = 0; j < len-1; j++){
            if(num[j] > num[j+1]){
                num[j] = num[j] - 1;
                for(int l = j+1; l < len; l++) num[l] = '9';
                j = -1;
            }
            else continue;
        }
        int j = 0;
        while(num[j] == '0') j++;
        ans = num.substr(j);
        cout << "Case #"<<i<<": " << ans << endl;
    }
}
void solutionC(){
    int T;
    ull K,N,Ls,Rs,tmp;
    cin >> T;
    for(int i = 1; i <= T; i++){
        list<ull> curr;
        cin >> N;
        cin >> K;
        cout << "Case #"<<i<<": ";
        N % 2 == 0 ? (Ls = N/2 - 1),(Rs = Ls+1) : (Ls = Rs = N/2);
        curr.push_back(Ls);
        curr.push_back(Rs);
        bool flg = false;
        for(ull p = 1; p < K; p++){
            if (curr.back() == 1) {
                flg = true;
                break;
            }
            else{
                tmp = curr.back();
                curr.pop_back();
                tmp % 2 == 0 ? (Ls = tmp/2 - 1),(Rs = Ls+1) : (Ls = Rs = tmp/2);
                if(curr.front() >= max(Ls,Rs)){
                    curr.push_front(Rs);
                    curr.push_front(Ls);
                }
                else{
                    auto it = curr.begin();
                    for(; it != curr.end(); it++){
                        if(*it >= Ls){
                            curr.insert(it, Ls);
                            break;
                        }
                    }
                    for(; it != curr.end(); it++){
                        if(*it >= Rs){
                            curr.insert(it, Rs);
                            break;
                        }

                    }
                    
                }
            }
        }
        if(flg) cout << "0 0" << endl;
        else    cout << max(Ls,Rs) << " " << min(Ls,Rs) << endl;
    }
    
}

int main(int argc, const char * argv[]) {
    if (argc == 2){
        switch((int)argv[1][0]){
            case 'A':solutionA();
                break;
            case 'B':solutionB();
                break;
            case 'C':solutionC();
                break;
            default:cout << " Problem not solved yet :P";
        }
    }
    else
        cout << "Specify Problem to solve";
    return 0;
}
