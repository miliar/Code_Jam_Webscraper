#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    string s;
    int t,k;
    cin>>t;
    int q=0;
    while(q++<t){
        cin>>s;
        for(int i=0;i<s.size()-1;i++){
            if(s[i]>s[i+1]){
                for(int j=i+1;j<s.size();j++){
                    s[j] = '0' + 9;
                }
                s[i] = s[i] - 1;
                for(int j=i;j>0;j--){
                    if(s[j]<s[j-1]){
                        s[j] = '0' + 9;
                        s[j-1] = s[j-1] - 1;
                    }
                }
                break;
            }
        }
        cout<<"Case #"<<q<<": ";
        int l;
        for(l=0;l<s.size();l++){
            if(s[l] != '0') break;
        }
        for(;l<s.size();l++){
            cout<<s[l];
        }
        cout<<endl;
    }
}

