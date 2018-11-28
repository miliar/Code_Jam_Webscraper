#include <bits/stdc++.h>

#define ll long long
#define de(x) cout<<#x<<": "<<x<<endl

using namespace std;

int b[1000001];

int main() {
     
    ios::sync_with_stdio(false);
    
    int t;
    cin>>t;
    int r,c;
    for(int q=1;q<=t;++q){
        cin>>r>>c;
        string a[r];
        for(int i=0;i<r;i++){
            cin>>a[i];
        }
        vector<int> vec;
        for(int i=0;i<r;i++){
            char c1='?';
            for(int j=0;j<a[i].length();j++){
                
                    if(a[i][j]!='?' && c1=='?'){
                        c1=a[i][j];
                        for(int k=0;k<j;k++){
                            a[i][k]=c1;
                        }
                    }
                    else if(a[i][j]!='?'){
                        c1=a[i][j];
                    }
                    else if(a[i][j]=='?'){
                        a[i][j]=c1;
                    }
                
            }
            if(c1=='?'){
                vec.push_back(i);
            }
        }
        int j=0;
        cout<<"Case #"<<q<<":"<<endl;
        if(vec.size()==0){
            for(int i=0;i<r;i++){
                cout<<a[i]<<endl;
            }
        }
        else{
            while(vec[j]==j){
                j++;
            }
            if(j>0){
                a[0]=a[j];
                for(int i=1;i<vec.size();i++){
                    a[vec[i]]=a[vec[i]-1];
                }
            }
            else{
                for(int i=0;i<vec.size();i++){
                    a[vec[i]]=a[vec[i]-1];
                }
            }
            for(int i=0;i<r;i++){
                cout<<a[i]<<endl;
            }
        }
    }
} 