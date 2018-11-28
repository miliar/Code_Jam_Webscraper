#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;



int main() {
    
    int n;
    cin >> n;
    long long m;
    for(int i = 0; i < n; i++){
        vector<int> s;
        cin >> m;
        int size=0;
        while (m>0){
            s.push_back(m%10);
            cerr<<m%10<<endl;
            m=m/10;
            size++;
        }
        
        for (int j=0;j<size-1;j++){
            if(s[size-1-j]>s[size-j-2]){
                int b=j;
                if(0!=b&&s[size-1-b]==s[size-b]){
                    while(0!=b&&s[size-1-b]==s[size-b]){
                        s[size-1-b]=s[size-1-b]-1; 
                        b--;
                    }
                    s[size-b-1]=s[size-b-1]-1; 
                    cerr<<"b= "<<b<<endl;
                    cerr<<s[size-1]<<endl;
                }else{
                    s[size-1-j]=s[size-1-j]-1;
                }
                for(int a=0;a<size-b-1;a++){
                    s[a]=9;
                }
                break;
            }
        }
        for (int j=0;j<size;j++){
            bool zero=false;
            if(zero||s[size-j-1]!=0){
                cout<<s[size-j-1];
                zero=true;
            }
        }
        cout<<endl;
    }
    
    return 0;
}


