//
//  main.cpp
//  C++_Interview
//
//  Created by Bruno Neves on 05/04/17.
//  Copyright © 2017 Snow Company. All rights reserved.
//

#include <iostream>

#include <algorithm>    // std::max
using namespace std;
#include <stdio.h>
#include <map>
#include <vector>
#include <string>
#include <unordered_set>
#include <stack>
#include <set>
#define _CRT_SECURE_NO_DEPRECATE // suppress some compilation warning messages (for VC++ users)
// Shortcuts for "common" data types in contests
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;
// To simplify repetitions/loops, Note: define your loop style and stick with it!
#define REP(i, a, b) \
for (int i = int(a); i <= int(b); i++) // a to b, and variable i is local!
#define TRvi(c, it) \
for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it) \
for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c, it) \
for (msi::iterator it = (c).begin(); it != (c).end(); it++)
#define INF 2000000000 // 2 billion
// If you need to recall how to use memset:
#define MEMSET_INF 127 // about 2B
#define MEMSET_HALF_INF 63 // about 1B
//memset(dist, MEMSET_INF, sizeof dist); // useful to initialize shortest path distances
//memset(dp_memo, -1, sizeof dp_memo); // useful to initialize DP memoization table
//memset(arr, 0, sizeof arr); // useful to clear array of integers

//Data Structure

//LinkedList:

struct node{
    node* next;
    int data;
    
};


bool hotel(vector<int> &arrive, vector<int> &depart, int K) {
    
    
    sort(arrive.begin(),arrive.end());
    sort(depart.begin(),depart.end());
    int current = 0;
    int aIndex = 0; //stores the last guy that arrived
    int dIndex = 0; // store the last guy that departed
    while(aIndex < arrive.size()){
        
        if(arrive[aIndex]<depart[dIndex]){
            aIndex++;
            current++;
        }
        else{
            dIndex++;
            current--;
        }
        if(current>K){
            return false;
        }
        
    }
    return true;
    
    
}


bool nextPermutation(vector<int>& s){
    int n = (int)s.size();
    
    int i = n-1;
    while(i>=0 && s[i-1]>=s[i]){
        i--;
    }
    //if every element at right is higher than of the left , the string is in its last permutation
    if(i<=0){
        return false;
    }
    
    
    
    
    int j = n-1;
    while(s[j]<=s[i-1]){
        j--;
    }
    int tmp = s[i-1];
    s[i-1] = s[j];
    s[j] = tmp;
    j = n-1;
    while(i<j){
        tmp = s[i];
        s[i] = s[j];
        s[j] = tmp;
    }
    return true;
}



int min(int a,int b){
   return a >= b ? b : a;
}

int max(int a,int b){
    return a>=b ? a:b;
}

void istidy(long long a){
    vector<int> p;
    while(a!=0){
        int n = a%10;
        p.push_back(n);
        a/=10;
    }
    int fim = (int)p.size()-1;
     for (int i=0;i<=fim-1;i++){
     if (p[i]<p[i+1]){
         p[i+1]--;
         for(int j=0;j<=i;j++){
             p[j] = 9;
         }
      }
     }
    if(p[fim]!=0) {
        if(fim==0)cout<< p[fim]<<endl;
        else cout << p[fim];
    }
    for(int i =fim-1;i>=0;i--){
        if(i==0)cout <<p[i]<<endl;
        else cout <<p[i];
        
        
    }
     
}

pair<int,int> getInterval(vector<int> p){
    
    
    int a1 ,d1;
    int left= -1;
    int right = -1;
    int left2 = -1;
    int right2 = -1;
    a1 = d1 = -1;
    pair<int,int> pa;
    for(int i=2;i<p.size();i++){
        int a,d;
        a = d = 0;
        left = i;
        while(i<p.size() && p[i]==0){
            a++;
            i++;
        }
        right = i;
        
        i++;
        left2 = i;
        while(i<p.size() && p[i]==0){
            i++;
            d++;
        }
        right2 = i;
        if(max(a,d)>max(a1,d1)){
         
            a1 = a;
            d1 = d;
            if(a<d){
                left = left2;
                right = right2;
            }
            pa.first = left;
            pa.second = right;
        }
        
    }
    return pa;
    
    
}

pair<int,int> lsrs(vector<int> p,int tmp){
    int ls,rs;
    pair<int,int> ans;
    ls = rs = 0;
    for(int i=tmp+1;i<p.size();i++){
        if(p[i]==0){
            rs++;
        }
        else{
            break;
        }
    }
    for(int i=tmp-1;i>=0;i--){
        if(p[i]==0){
            ls++;
        }
        else{
            break;
        }
    }
    ans.first = ls;
    ans.second = rs;
    return ans;
    
}

int main(int argc, const char * argv[]) {
    // insert code here...
    
    
    
    int t,n,k;
    int c = 1;
    cin >> t;
    while(t--){
        cin >> n;
        cin >> k;
        
        cout <<"Case #"<<c++<<": ";

        if(n==k) cout<<"0 0"<<endl;
        else{
        vector<int> p(n+3,0);
        int fim = (int)p.size()-1;
        p[1] = 1;
        p[fim]=1;
        int mid = (1+fim)/2;
        p[mid] = 1;
        k--;
        while(k--){
            
        pair<int,int> aux = getInterval(p);
        mid = (aux.first+aux.second-1)/2;
            p[mid] = 1;
            
        }
        
        pair<int,int> pa = lsrs(p, mid);
              cout << max(pa.first,pa.second)<<" "<<min(pa.first,pa.second)<<endl;
        
        
        }
    }
    
    
    return 0;
}
    
    




/*
 int t,k;
 string s;
 cin >> t;
 int c = 1;
 while(t--){
 
 cin>>s;
 cin>>k;
 int count = 0;
 int ini = 0;
 int fim = (int)s.length()-1;
 
 while(ini<fim){
 
 if(s[ini]=='-'){
 for(int j=ini;j<ini+k;j++){
 if(s[j]=='-'){
 s[j] = '+';
 }
 else{
 s[j] = '-';
 }
 }
 count++;
 }
 if(s[fim]=='-' && fim - k > ini){
 for(int j=fim;j>fim-k;j--){
 if(s[j]=='-'){
 s[j] = '+';
 }
 else{
 s[j] = '-';
 }
 
 
 }
 count++;
 }
 ini++;
 fim--;
 }
 cout << "Case #"<<c++<<": ";
 bool cond = false;
 for(int i=0;i<(int)s.length();i++){
 if(s[i]=='-'){
 cout<<"IMPOSSIBLE"<<endl;
 cond = true;
 break;
 }
 }
 if(!cond){
 cout <<count<<endl;
 }
 
 
 }
 */






/*
 int t,k;
 string s;
 cin >> t;
 int c = 1;
 while(t--){
 
 cin>>s;
 cin>>k;
 int count = 0;
 int ini = 0;
 int fim = (int)s.length()-1;
 
 while(ini<fim){
 
 if(s[ini]=='-'){
 for(int j=ini;j<ini+k;j++){
 if(s[j]=='-'){
 s[j] = '+';
 }
 else{
 s[j] = '-';
 }
 }
 count++;
 }
 if(s[fim]=='-' && fim - k > ini){
 for(int j=fim;j>fim-k;j--){
 if(s[j]=='-'){
 s[j] = '+';
 }
 else{
 s[j] = '-';
 }
 
 
 }
 count++;
 }
 ini++;
 fim--;
 }
 cout << "Case #"<<c++<<": ";
 bool cond = false;
 for(int i=0;i<(int)s.length();i++){
 if(s[i]=='-'){
 cout<<"IMPOSSIBLE"<<endl;
 cond = true;
 break;
 }
 }
 if(!cond){
 cout <<count<<endl;
 }
 
 
 }*/
