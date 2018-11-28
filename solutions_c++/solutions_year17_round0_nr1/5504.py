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
        cin>>k;
        bool flag = true;
        int count = 0;
        for(int i=0;i<s.size();i++){

            if(s[i] == '-'){
                count++;
                if(i+k-1>=s.size()){
                        flag = false;
                        break;
                }
                for(int j=i;j<i+k;j++){
                    if(s[j] == '-') s[j] = '+';
                    else s[j] = '-';
                }
            }
        }

        if(flag){
            cout<<"Case #"<<q<<": "<<count<<endl;
        }
        else{
            cout<<"Case #"<<q<<": IMPOSSIBLE"<<endl;
        }
    }
}
